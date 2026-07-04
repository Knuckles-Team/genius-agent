"""Native epistemic-graph ingestion for Genius Agent search results (documents + typed nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. Genius Agent is a search engine: it issues
web-search queries (DuckDuckGo / Google / Bing / Searxng) and crawls the hits to markdown. This
module natively pushes that harvest into the ONE epistemic-graph knowledge graph in the modality
that fits — **documents** (the retrieved text worth semantic search) plus the **typed OWL nodes**
that give it structure (`:SearchQuery`, `:SearchResult`, `:SearchProvider`, `:WebPage`) and links.

It is a thin mapper over the shared write primitive
``agent_utilities.knowledge_graph.memory.native_ingest`` — imported GUARDED (try/except). When the
primitive is not present in the installed ``agent_utilities`` (it is newer than the pinned wheel),
a self-contained txn fallback over the lightweight ``GraphComputeEngine()._client`` is used — the
same fast client the blob ``MediaStore`` uses, NOT the heavy in-process ingestion engine.

Everything is best-effort and dependency-/engine-guarded: with no KG stack or no reachable engine
every entry point **no-ops** (returns ``None``), so Genius keeps working with zero KG
infrastructure. Node ids follow ``genius:<class>:<externalId>``; every ``type`` matches a class the
package's ``ontology_providers`` ``genius.ttl`` federates.
"""

from __future__ import annotations

import hashlib
import logging
import time
from typing import Any

logger = logging.getLogger("genius_agent.kg")

_SOURCE = "genius-agent"
_DOMAIN = "genius"
_DEFAULT_GRAPH = "__commons__"


# --------------------------------------------------------------------------- #
# write path — prefer the shared primitive, fall back to a self-contained txn
# --------------------------------------------------------------------------- #
def _primitive() -> Any | None:
    """Return the shared ``native_ingest`` module, or ``None`` if unavailable."""
    try:
        from agent_utilities.knowledge_graph.memory import (  # type: ignore
            native_ingest,
        )

        return native_ingest
    except Exception as e:  # noqa: BLE001 — primitive newer than installed wheel
        logger.debug("native_ingest primitive unavailable: %s", e)
        return None


def _client() -> tuple[Any | None, str]:
    """Return ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        graph = getattr(engine, "graph_name", None) or _DEFAULT_GRAPH
        return client, graph
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _fallback_write(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
    *,
    client: Any | None,
    graph: str | None,
) -> dict[str, int] | None:
    """Self-contained txn write, mirroring the shared primitive's node/edge dance."""
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if client is None:
        client, graph = _client()
    if client is None:
        return None
    graph = graph or _DEFAULT_GRAPH

    try:
        txn = client.txn.begin(graph=graph)
        for ent in entities:
            props = {k: v for k, v in ent.items() if k != "id" and v is not None}
            props.setdefault("source", _SOURCE)
            props.setdefault("domain", _DOMAIN)
            client.txn.add_node(txn, ent["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest: wrote %d nodes, %d edges", len(entities), edges)
    return {"nodes": len(entities), "edges": edges}


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph.

    ``entities``: ``[{"id":..., "type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "type":rel}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None``. Prefers the shared primitive; falls
    back to a self-contained txn. ``client``/``graph`` may be injected (tests).
    """
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    prim = _primitive()
    if prim is not None and client is None:
        return prim.ingest_entities(
            entities, relationships, source=source, domain=domain
        )
    return _fallback_write(entities, relationships, client=client, graph=graph)


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as shared ``:Document`` nodes (semantic-search fodder).

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:..., ...props}``.
    Prefers the shared primitive; falls back to a self-contained txn that stamps
    ``type=Document`` + ``created_at``.
    """
    prim = _primitive()
    if prim is not None and client is None:
        return prim.ingest_documents(documents, source=source, domain=domain)

    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    nodes: list[dict[str, Any]] = []
    for doc in documents or []:
        did = doc.get("id")
        text = doc.get("text") or doc.get("content")
        if not did or not text:
            continue
        node = {k: v for k, v in doc.items() if k != "content" and v is not None}
        node["id"] = did
        node["type"] = "Document"
        node["text"] = text
        node.setdefault("created_at", now)
        nodes.append(node)
    return _fallback_write(nodes, None, client=client, graph=graph)


# --------------------------------------------------------------------------- #
# domain mappers — search results / crawled pages -> typed nodes + documents
# --------------------------------------------------------------------------- #
def _hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8", "replace")).hexdigest()[:16]


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
            "type": "SearchProvider",
            "name": prov,
            "providerName": prov,
            "externalToolId": prov,
        }
    )
    entities.append(
        {
            "id": query_id,
            "type": "SearchQuery",
            "name": query,
            "queryText": query,
            "resultCount": len([r for r in (results or []) if r]),
            "externalToolId": _hash(prov + "|" + query),
        }
    )
    relationships.append({"source": query_id, "target": prov_id, "type": "answeredBy"})

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
                "type": "SearchResult",
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
                "type": "WebPage",
                "name": norm["title"] or url,
                "sourceUrl": url,
                "externalToolId": uh,
            }
        )
        relationships.append(
            {"source": query_id, "target": result_id, "type": "hasResult"}
        )
        relationships.append(
            {"source": result_id, "target": page_id, "type": "pointsToPage"}
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
                {"source": result_id, "target": doc_id, "type": "hasContent"}
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
                "type": "WebPage",
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
                {"source": page_id, "target": doc_id, "type": "hasContent"}
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
