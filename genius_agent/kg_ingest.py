"""Native epistemic-graph ingestion for Genius Agent search results (documents + typed nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. Genius Agent is a search engine: it issues
web-search queries (DuckDuckGo / Google / Bing / Searxng) and crawls the hits to markdown. This
module natively pushes that harvest into the ONE epistemic-graph knowledge graph in the modality
that fits — **documents** (the retrieved text worth semantic search) plus the **typed OWL nodes**
that give it structure (`:SearchQuery`, `:SearchResult`, `:SearchProvider`, `:WebPage`) and links,
through the required ``agent_utilities.knowledge_graph.memory.native_ingest`` authority — the one
connector write path; there is no self-contained fallback transaction here.

The MCP tool surface exposes these as best-effort tools that must never raise on an
unreachable/misconfigured KG stack, so ``ingest_entities`` / ``ingest_documents`` stay
**best-effort**: they return ``None`` (never raise) for empty input or when the shared
primitive reports :class:`NativeIngestError` (no reachable engine, or a malformed record).
Node ids follow ``genius:<class>:<externalId>``; every ``node_type`` matches a class the
package's ``ontology_providers`` ``genius.ttl`` federates.
"""

from __future__ import annotations

import hashlib
import logging
from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    NativeIngestError,
    ingest_documents as _native_ingest_documents,
    ingest_entities as _native_ingest_entities,
)

logger = logging.getLogger("genius_agent.kg")

_SOURCE = "genius-agent"
_DOMAIN = "genius"


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph. Best-effort, never raises.

    ``entities``: ``[{"id":..., "node_type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "relationship":<link>}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None`` (empty input / no reachable engine /
    malformed record). ``client``/``graph`` may be injected (tests); otherwise the
    process-owned governed authority is resolved on demand.
    """
    if not entities:
        return None
    try:
        return _native_ingest_entities(
            entities,
            relationships,
            source=source,
            domain=domain,
            client=client,
            graph=graph,
        )
    except NativeIngestError as exc:
        logger.debug("KG ingest unavailable/failed: %s", exc)
        return None


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as shared ``:Document`` nodes. Best-effort.

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:..., ...props}``.
    """
    if not documents:
        return None
    try:
        return _native_ingest_documents(
            documents, source=source, domain=domain, client=client, graph=graph
        )
    except NativeIngestError as exc:
        logger.debug("KG ingest unavailable/failed: %s", exc)
        return None


# --------------------------------------------------------------------------- #
# domain mappers — search results / crawled pages -> typed nodes + documents
# --------------------------------------------------------------------------- #
def _hash(value: str) -> str:
    return hashlib.sha1(
        value.encode("utf-8", "replace"), usedforsecurity=False
    ).hexdigest()[:16]


def _norm_result(raw: dict[str, Any]) -> dict[str, Any]:
    """Normalize a provider result to ``{title, url, snippet}`` (fields vary by provider)."""
    return {
        "title": raw.get("title") or raw.get("Text") or raw.get("name"),
        "url": raw.get("link")
        or raw.get("url")
        or raw.get("FirstURL")
        or raw.get("href"),
        "snippet": raw.get("snippet") or raw.get("body") or raw.get("Text") or "",
    }


def map_search_results(
    query: str,
    results: list[dict[str, Any]],
    *,
    provider: str = "duckduckgo",
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Map a query + its provider results to ``(entities, relationships, documents)``.

    Emits one ``:SearchQuery`` (linked ``:answeredBy`` its ``:SearchProvider``), a
    ``:SearchResult`` per hit (``:hasResult`` from the query, ``:pointsToPage`` to a
    ``:WebPage``), and a shared ``:Document`` carrying each hit's title+snippet text
    (``:hasContent``). Pure/offline — the ingest split lets tests assert the mapping.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    documents: list[dict[str, Any]] = []
    if not query:
        return entities, relationships, documents

    prov = (provider or "duckduckgo").strip().lower()
    prov_id = f"genius:searchprovider:{prov}"
    query_id = f"genius:searchquery:{_hash(prov + '|' + query)}"

    entities.append(
        {
            "id": prov_id,
            "node_type": "SearchProvider",
            "name": prov,
            "providerName": prov,
            "externalToolId": prov,
        }
    )
    entities.append(
        {
            "id": query_id,
            "node_type": "SearchQuery",
            "name": query,
            "queryText": query,
            "resultCount": len([r for r in (results or []) if r]),
            "externalToolId": _hash(prov + "|" + query),
        }
    )
    relationships.append(
        {"source": query_id, "target": prov_id, "relationship": "answeredBy"}
    )

    for i, raw in enumerate(results or [], start=1):
        norm = _norm_result(raw)
        url = norm["url"]
        if not url:
            continue
        uh = _hash(url)
        result_id = f"genius:searchresult:{_hash(query_id + '|' + url)}"
        page_id = f"genius:webpage:{uh}"
        doc_id = f"genius:document:{_hash('result|' + result_id)}"

        entities.append(
            {
                "id": result_id,
                "node_type": "SearchResult",
                "name": norm["title"] or url,
                "rank": i,
                "snippet": norm["snippet"],
                "sourceUrl": url,
                "externalToolId": _hash(query_id + "|" + url),
            }
        )
        entities.append(
            {
                "id": page_id,
                "node_type": "WebPage",
                "name": norm["title"] or url,
                "sourceUrl": url,
                "externalToolId": uh,
            }
        )
        relationships.append(
            {"source": query_id, "target": result_id, "relationship": "hasResult"}
        )
        relationships.append(
            {"source": result_id, "target": page_id, "relationship": "pointsToPage"}
        )

        text = "\n".join(t for t in (norm["title"], norm["snippet"]) if t).strip()
        if text:
            documents.append(
                {
                    "id": doc_id,
                    "text": text,
                    "title": norm["title"] or url,
                    "source_uri": url,
                    "query": query,
                    "provider": prov,
                }
            )
            relationships.append(
                {"source": result_id, "target": doc_id, "relationship": "hasContent"}
            )

    return entities, relationships, documents


def ingest_search_results(
    query: str,
    results: list[dict[str, Any]],
    *,
    provider: str = "duckduckgo",
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map + ingest one query's search results (typed nodes + ranked links + documents).

    Returns aggregated ``{"nodes":n, "edges":m, "documents":d}`` or ``None`` (no hits).
    """
    if not query or not results:
        return None
    entities, relationships, documents = map_search_results(
        query, results, provider=provider
    )
    if not entities:
        return None
    ent_res = ingest_entities(entities, relationships, client=client, graph=graph)
    doc_res = ingest_documents(documents, client=client, graph=graph)
    if ent_res is None and doc_res is None:
        return None
    return {
        "nodes": (ent_res or {}).get("nodes", 0),
        "edges": (ent_res or {}).get("edges", 0),
        "documents": (doc_res or {}).get("nodes", 0),
    }


def ingest_crawled_pages(
    pages: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map crawled markdown pages -> ``:WebPage`` nodes + shared ``:Document`` text.

    Each page: ``{"url":..., "markdown"|"text"|"content":..., "title"?:...}``.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    documents: list[dict[str, Any]] = []
    for page in pages or []:
        url = page.get("url") or page.get("source_uri")
        text = page.get("markdown") or page.get("text") or page.get("content")
        if not url:
            continue
        uh = _hash(url)
        page_id = f"genius:webpage:{uh}"
        title = page.get("title") or url
        entities.append(
            {
                "id": page_id,
                "node_type": "WebPage",
                "name": title,
                "sourceUrl": url,
                "externalToolId": uh,
            }
        )
        if text:
            doc_id = f"genius:document:{_hash('page|' + url)}"
            documents.append(
                {
                    "id": doc_id,
                    "text": text,
                    "title": title,
                    "source_uri": url,
                }
            )
            relationships.append(
                {"source": page_id, "target": doc_id, "relationship": "hasContent"}
            )
    if not entities:
        return None
    ent_res = ingest_entities(entities, relationships, client=client, graph=graph)
    doc_res = ingest_documents(documents, client=client, graph=graph)
    if ent_res is None and doc_res is None:
        return None
    return {
        "nodes": (ent_res or {}).get("nodes", 0),
        "edges": (ent_res or {}).get("edges", 0),
        "documents": (doc_res or {}).get("nodes", 0),
    }


# --------------------------------------------------------------------------- #
# Wire-First fetch flow — run the real web-search dispatcher and push the harvest
# --------------------------------------------------------------------------- #
def _run_web_search(query: str, max_results: int) -> tuple[str, list[dict[str, Any]]]:
    """Invoke the universal web-search dispatcher; return ``(provider, results)``.

    Uses the same provider-selection env vars as the ``web-search`` skill dispatcher
    (SEARXNG_URL / GOOGLE_API_KEY+GOOGLE_CX / BING_API_KEY, else DuckDuckGo). Returns
    ``("", [])`` when the skill scripts are not importable/runnable.
    """
    import importlib.util
    import json
    import os
    import subprocess
    import sys

    spec = importlib.util.find_spec("universal_skills")
    if spec is None or not spec.submodule_search_locations:
        logger.debug("web-search: universal_skills not importable")
        return "", []
    base = spec.submodule_search_locations[0]
    scripts = os.path.join(base, "research", "web-search", "scripts")

    provider_script = "search_duckduckgo.py"
    provider = "duckduckgo"
    if os.environ.get("SEARXNG_URL"):
        provider_script, provider = "search_searxng.py", "searxng"
    elif os.environ.get("GOOGLE_API_KEY") and os.environ.get("GOOGLE_CX"):
        provider_script, provider = "search_google.py", "google"
    elif os.environ.get("BING_API_KEY"):
        provider_script, provider = "search_bing.py", "bing"

    path = os.path.join(scripts, provider_script)
    if not os.path.exists(path):
        return "", []
    try:
        proc = subprocess.run(
            [
                sys.executable,
                path,
                "--query",
                query,
                "--max-results",
                str(max_results),
                "--json",
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
        results = json.loads(proc.stdout) if proc.stdout.strip() else []
        if not isinstance(results, list):
            results = []
        return provider, results
    except Exception as e:  # noqa: BLE001 — search is best-effort
        logger.debug("web-search dispatch failed: %s", e)
        return "", []


def genius_ingest_search(
    query: str,
    *,
    max_results: int = 10,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, Any] | None:
    """Wire-First: run a real web search for ``query`` and ingest its results into the KG.

    Lists via the real search provider (the same dispatcher the ``web-search`` skill uses),
    maps the hits to ``:SearchQuery``/``:SearchResult``/``:WebPage`` + ``:Document`` nodes,
    and pushes them through the fast engine client. Best-effort: returns
    ``{"query":..., "provider":..., "results":n, "ingested":None|{...}}``; ``ingested`` is
    ``None`` when no engine is reachable (search still runs).
    """
    provider, results = _run_web_search(query, max_results)
    ingested = (
        ingest_search_results(
            query,
            results,
            provider=provider or "duckduckgo",
            client=client,
            graph=graph,
        )
        if results
        else None
    )
    return {
        "query": query,
        "provider": provider or "duckduckgo",
        "results": len(results),
        "ingested": ingested,
    }
