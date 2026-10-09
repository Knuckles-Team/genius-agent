"""Native epistemic-graph ingestion for Genius search — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` / ``map_search_results`` /
``ingest_search_results`` / ``ingest_crawled_pages`` seams against a fake ``agent_connector_sdk``
ingest transport (no engine required), asserting the records/relationships the SDK's own request
builder assembled and the search-result -> :SearchQuery/:SearchResult/:WebPage/:Document mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.

Unlike most fleet connectors, ``genius_agent.kg_ingest`` is a **best-effort** surface (its MCP
tools must never raise when the KG stack is down), so it converts ``IngestError`` into ``None``
rather than propagating it — those semantics are exercised explicitly below. Every public
function is async; the fake transport is injected through the ``ingest=`` keyword so tests never
touch the SDK's process-global facade.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest

from genius_agent.kg_ingest import (
    ingest_crawled_pages,
    ingest_documents,
    ingest_entities,
    ingest_search_results,
    map_search_results,
)


class _FakeTransport:
    def __init__(self, *, fail: bool = False) -> None:
        self.requests: list[Any] = []
        self._fail = fail

    async def source_status(self, connector: str, stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: Any) -> Any:
        if self._fail:
            raise IngestError("synthetic transport failure")
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, data: Any) -> Any:
        raise AssertionError("this connector's ingestion carries no media")


@pytest.fixture
def ingest():
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


@pytest.fixture
def failing_ingest():
    transport = _FakeTransport(fail=True)
    return KnowledgeIngest(transport, loop=None), transport


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    res = await ingest_entities(
        [
            {"id": "a", "node_type": "SearchQuery", "queryText": "q"},
            {"id": "b", "node_type": "SearchProvider", "providerName": "duckduckgo"},
        ],
        [{"source": "a", "target": "b", "relationship": "answeredBy"}],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(transport.requests[0].records) == 2
    assert len(transport.requests[0].relationships) == 1


@pytest.mark.asyncio
async def test_ingest_documents_submits_records(ingest):
    service, transport = ingest
    res = await ingest_documents(
        [{"id": "genius:document:1", "text": "hello world", "title": "t"}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    assert len(transport.requests[0].records) == 1


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


@pytest.mark.asyncio
async def test_ingest_search_results_end_to_end(ingest):
    service, transport = ingest
    res = await ingest_search_results(
        "cilium ebpf",
        [{"title": "Cilium", "link": "https://cilium.io", "snippet": "eBPF mesh"}],
        provider="duckduckgo",
        ingest=service,
    )
    assert res is not None
    assert res["documents"] == 1
    # query + provider + result + webpage all written
    assert res["nodes"] == 4
    # two submit() calls: entities+relationships, then documents
    assert len(transport.requests) == 2


@pytest.mark.asyncio
async def test_ingest_crawled_pages_maps_webpage_and_document(ingest):
    service, transport = ingest
    res = await ingest_crawled_pages(
        [
            {
                "url": "https://docs.example.com/g",
                "markdown": "# Guide\nbody",
                "title": "Guide",
            }
        ],
        ingest=service,
    )
    assert res is not None
    assert res["nodes"] == 1
    assert res["documents"] == 1


@pytest.mark.asyncio
async def test_ingest_noops_without_engine_failure(failing_ingest):
    service, _transport = failing_ingest
    assert (
        await ingest_entities(
            [{"id": "a", "node_type": "SearchQuery"}], ingest=service
        )
        is None
    )


@pytest.mark.asyncio
async def test_ingest_empty_is_noop(ingest):
    service, _transport = ingest
    assert await ingest_entities([], ingest=service) is None
    assert await ingest_search_results("q", [], ingest=service) is None
    assert await ingest_crawled_pages([], ingest=service) is None
