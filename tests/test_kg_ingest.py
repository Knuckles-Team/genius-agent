"""Native epistemic-graph ingestion for Genius search — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` / ``map_search_results`` /
``ingest_search_results`` / ``ingest_crawled_pages`` seams with a fake engine client (no
engine required), asserting the txn add_node/commit + edge calls and the search-result →
:SearchQuery/:SearchResult/:WebPage/:Document mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from genius_agent.kg_ingest import (
    ingest_crawled_pages,
    ingest_documents,
    ingest_entities,
    ingest_search_results,
    map_search_results,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def commit(self, txn):
        self.committed = True
        return True


class _FakeEdges:
    def __init__(self):
        self.edges = []

    def add(self, src, dst, props):
        self.edges.append((src, dst, props))


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()
        self.edges = _FakeEdges()


def test_ingest_entities_writes_nodes_and_edges_with_provenance():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "type": "SearchQuery", "queryText": "q"},
            {"id": "b", "type": "SearchProvider", "providerName": "duckduckgo"},
        ],
        [{"source": "a", "target": "b", "type": "answeredBy"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    assert c.txn.nodes["a"]["source"] == "genius-agent"
    assert c.txn.nodes["a"]["domain"] == "genius"
    assert c.edges.edges == [("a", "b", {"type": "answeredBy"})]


def test_ingest_documents_stamps_type_and_text():
    c = _FakeClient()
    res = ingest_documents(
        [{"id": "genius:document:1", "text": "hello world", "title": "t"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["genius:document:1"]
    assert node["type"] == "Document"
    assert node["text"] == "hello world"
    assert "created_at" in node


def test_map_search_results_shapes():
    entities, rels, docs = map_search_results(
        "openraft consensus",
        [
            {"title": "openraft", "link": "https://gh/openraft", "snippet": "raft lib"},
            {"title": "no url", "snippet": "skipped"},
        ],
        provider="DuckDuckGo",
    )
    types = {e["type"] for e in entities}
    assert {"SearchProvider", "SearchQuery", "SearchResult", "WebPage"} <= types
    # provider is normalized to lowercase
    prov = next(e for e in entities if e["type"] == "SearchProvider")
    assert prov["providerName"] == "duckduckgo"
    # the URL-less hit is dropped -> exactly one SearchResult / WebPage / Document
    assert sum(1 for e in entities if e["type"] == "SearchResult") == 1
    assert len(docs) == 1
    result = next(e for e in entities if e["type"] == "SearchResult")
    assert result["rank"] == 1
    assert result["sourceUrl"] == "https://gh/openraft"
    rel_types = {r["type"] for r in rels}
    assert {"answeredBy", "hasResult", "pointsToPage", "hasContent"} <= rel_types


def test_ingest_search_results_end_to_end():
    c = _FakeClient()
    res = ingest_search_results(
        "cilium ebpf",
        [{"title": "Cilium", "link": "https://cilium.io", "snippet": "eBPF mesh"}],
        provider="duckduckgo",
        client=c,
        graph="__commons__",
    )
    assert res is not None
    assert res["documents"] == 1
    # query + provider + result + webpage all written
    assert res["nodes"] == 4
    assert any(n["type"] == "Document" for n in c.txn.nodes.values())
    assert any(n.get("sourceUrl") == "https://cilium.io" for n in c.txn.nodes.values())


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
        graph="__commons__",
    )
    assert res is not None
    assert res["nodes"] == 1
    assert res["documents"] == 1
    page = next(n for n in c.txn.nodes.values() if n["type"] == "WebPage")
    assert page["sourceUrl"] == "https://docs.example.com/g"


def test_ingest_noops_without_engine():
    assert ingest_entities([{"id": "a", "type": "SearchQuery"}]) is None


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_search_results("q", [], client=_FakeClient()) is None
    assert ingest_crawled_pages([], client=_FakeClient()) is None
