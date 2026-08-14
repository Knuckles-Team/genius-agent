"""Native epistemic-graph ingestion for Genius search — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` / ``map_search_results`` /
``ingest_search_results`` / ``ingest_crawled_pages`` seams with a fake ChangeEnvelope-capable
engine client (no engine required), asserting the committed nodes/edges and the search-result ->
:SearchQuery/:SearchResult/:WebPage/:Document mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.

The fake client mirrors agent-utilities' own sanctioned test double
(``agent-utilities/tests/knowledge_graph/test_native_ingest.py``) — the ``txn``-only fake is
retired; ``native_ingest`` now hard-requires an injected client exposing
``.changes``/``.nodes``/``.rdf``/``.supports()``. Unlike most fleet connectors,
``genius_agent.kg_ingest`` is a **best-effort** surface (its MCP tools must never raise when the
KG stack is down), so it converts ``NativeIngestError`` into ``None`` rather than propagating it
— those semantics are exercised explicitly below.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest
from agent_utilities.knowledge_graph.core.session import GraphSession, use_session
from agent_utilities.models.company_brain import ActorType
from agent_utilities.security.brain_context import ActorContext, use_actor

from genius_agent.kg_ingest import (
    ingest_crawled_pages,
    ingest_documents,
    ingest_entities,
    ingest_search_results,
    map_search_results,
)


@pytest.fixture(autouse=True)
def _no_runtime_username_collision(monkeypatch):
    """Neutralize a host-specific false positive in the shared privacy gate.

    ``PersistencePrivacyGuard`` derives its identity deny-terms from the runtime
    host's OS username/home-dir-name/hostname (``agent_utilities.security.
    persistence_privacy._runtime_deny_terms``). On a host where one of those
    happens to equal ``"genius"`` (this package's own id/domain prefix, e.g.
    ``genius:searchquery:...``, ``domain="genius"``), every identifier this
    module writes would be rejected as an unsafe identity purely because it
    contains the *deployment host's* username -- a coincidence unrelated to
    the ingest mapping under test. Neutralize it so these tests exercise the
    mapping, not whichever host happens to run them.
    """
    import agent_utilities.security.persistence_privacy as _privacy

    monkeypatch.setattr(_privacy, "_runtime_deny_terms", lambda: ())


@pytest.fixture(autouse=True)
def _governed_session():
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="graph:opaque:synthetic",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"


def test_ingest_entities_writes_nodes_and_edges_with_provenance():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "SearchQuery", "queryText": "q"},
            {"id": "b", "node_type": "SearchProvider", "providerName": "duckduckgo"},
        ],
        [{"source": "a", "target": "b", "relationship": "answeredBy"}],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert set(c.nodes.values) == {"a", "b"}
    assert c.nodes.values["a"]["source"] == "genius-agent"
    assert c.nodes.values["a"]["domain"] == "genius"
    assert c.changes.edges == [("a", "b", {"relationship": "answeredBy"})]


def test_ingest_documents_stamps_type_and_text():
    c = _FakeClient()
    res = ingest_documents(
        [{"id": "genius:document:1", "text": "hello world", "title": "t"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["genius:document:1"]
    assert node["node_type"] == "Document"
    assert node["text"] == "hello world"
    assert "content_hash" in node


def test_map_search_results_shapes():
    entities, rels, docs = map_search_results(
        "openraft consensus",
        [
            {"title": "openraft", "link": "https://gh/openraft", "snippet": "raft lib"},
            {"title": "no url", "snippet": "skipped"},
        ],
        provider="DuckDuckGo",
    )
    types = {e["node_type"] for e in entities}
    assert {"SearchProvider", "SearchQuery", "SearchResult", "WebPage"} <= types
    # provider is normalized to lowercase
    prov = next(e for e in entities if e["node_type"] == "SearchProvider")
    assert prov["providerName"] == "duckduckgo"
    # the URL-less hit is dropped -> exactly one SearchResult / WebPage / Document
    assert sum(1 for e in entities if e["node_type"] == "SearchResult") == 1
    assert len(docs) == 1
    result = next(e for e in entities if e["node_type"] == "SearchResult")
    assert result["rank"] == 1
    assert result["sourceUrl"] == "https://gh/openraft"
    rel_types = {r["relationship"] for r in rels}
    assert {"answeredBy", "hasResult", "pointsToPage", "hasContent"} <= rel_types


def test_ingest_search_results_end_to_end():
    c = _FakeClient()
    res = ingest_search_results(
        "cilium ebpf",
        [{"title": "Cilium", "link": "https://cilium.io", "snippet": "eBPF mesh"}],
        provider="duckduckgo",
        client=c,
    )
    assert res is not None
    assert res["documents"] == 1
    # query + provider + result + webpage all written
    assert res["nodes"] == 4
    assert any(n["node_type"] == "Document" for n in c.nodes.values.values())
    assert any(
        n.get("sourceUrl") == "https://cilium.io" for n in c.nodes.values.values()
    )


def test_ingest_crawled_pages_maps_webpage_and_document():
    c = _FakeClient()
    res = ingest_crawled_pages(
        [
            {
                "url": "https://docs.example.com/g",
                "markdown": "# Guide\nbody",
                "title": "Guide",
            }
        ],
        client=c,
    )
    assert res is not None
    assert res["nodes"] == 1
    assert res["documents"] == 1
    page = next(n for n in c.nodes.values.values() if n["node_type"] == "WebPage")
    assert page["sourceUrl"] == "https://docs.example.com/g"


def test_ingest_noops_without_engine():
    assert ingest_entities([{"id": "a", "node_type": "SearchQuery"}]) is None


def test_ingest_rejects_retired_structural_alias_as_noop():
    # genius_agent's tool surface is best-effort (never raises): a malformed record
    # (the retired ``type`` alias instead of canonical ``node_type``) is reported
    # back as a clean no-op rather than propagating NativeIngestError.
    c = _FakeClient()
    assert ingest_entities([{"id": "a", "type": "SearchQuery"}], client=c) is None
    assert c.changes.applied == []


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_search_results("q", [], client=_FakeClient()) is None
    assert ingest_crawled_pages([], client=_FakeClient()) is None
