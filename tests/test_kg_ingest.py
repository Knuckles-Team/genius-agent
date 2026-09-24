"""Native epistemic-graph ingestion for Genius search — Wire-First coverage.

Exercises the pure mapping seam (``map_search_results``) and the best-effort
no-op guarantee of ``ingest_entities``/``ingest_documents``/``ingest_search_results``/
``ingest_crawled_pages`` — genius_agent's MCP tools must never raise when the KG
stack is down. CONCEPT:AU-KG.ingest.enterprise-source-extractor.

SDK GAP (EH-481/SDK-GAPS.md): ``_native_ingest_entities``/``_native_ingest_documents``
are stubs (no SDK equivalent yet for the old dependency-injected
``agent_utilities.knowledge_graph.memory.native_ingest`` ChangeEnvelope mapper — see
``genius_agent/kg_ingest.py``'s module docstring). Every ``ingest_*`` call below is
therefore exercised for its no-op contract rather than real graph writes; the DI-based
``_FakeClient`` coverage of the retired real-mapping path is dropped with it.
"""

from __future__ import annotations

from typing import Any

from genius_agent.kg_ingest import (
    ingest_crawled_pages,
    ingest_documents,
    ingest_entities,
    ingest_search_results,
    map_search_results,
)


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


def test_ingest_entities_noops_with_no_ingest_primitive():
    res = ingest_entities(
        [
            {"id": "a", "node_type": "SearchQuery", "queryText": "q"},
            {"id": "b", "node_type": "SearchProvider", "providerName": "duckduckgo"},
        ],
        [{"source": "a", "target": "b", "relationship": "answeredBy"}],
    )
    assert res is None


def test_ingest_documents_noops_with_no_ingest_primitive():
    res = ingest_documents(
        [{"id": "genius:document:1", "text": "hello world", "title": "t"}],
    )
    assert res is None


def test_ingest_search_results_noops_with_no_ingest_primitive():
    res = ingest_search_results(
        "cilium ebpf",
        [{"title": "Cilium", "link": "https://cilium.io", "snippet": "eBPF mesh"}],
        provider="duckduckgo",
    )
    # The mapping still runs (there were hits), but nothing was actually written --
    # both the entities and documents commit degrade to None with no primitive wired.
    assert res is None


def test_ingest_crawled_pages_noops_with_no_ingest_primitive():
    res = ingest_crawled_pages(
        [
            {
                "url": "https://docs.example.com/g",
                "markdown": "# Guide\nbody",
                "title": "Guide",
            }
        ],
    )
    assert res is None


def test_ingest_noops_without_engine():
    assert ingest_entities([{"id": "a", "node_type": "SearchQuery"}]) is None


def test_ingest_primitive_failure_is_a_clean_noop(monkeypatch):
    # genius_agent's tool surface is best-effort (never raises): any failure from
    # the ingest primitive (today: always, since it is a stub) degrades to a clean
    # no-op rather than propagating.
    import genius_agent.kg_ingest as kg_ingest

    def _boom(*args: Any, **kwargs: Any):
        raise RuntimeError("engine unreachable")

    monkeypatch.setattr(kg_ingest, "_native_ingest_entities", _boom)
    assert ingest_entities([{"id": "a", "node_type": "SearchQuery"}]) is None


def test_ingest_empty_is_noop():
    assert ingest_entities([]) is None
    assert ingest_search_results("q", []) is None
    assert ingest_crawled_pages([]) is None
