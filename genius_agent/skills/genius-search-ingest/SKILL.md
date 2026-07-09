---
name: genius-search-ingest
skill_type: skill
description: >-
  Natively ingest Genius Agent web-search hits and crawled pages into the
  epistemic-graph knowledge graph — search results become :SearchQuery /
  :SearchResult / :SearchProvider / :WebPage typed nodes plus shared :Document
  text for semantic search. Use when the agent must persist what it searched or
  crawled into the KG so it becomes durable, queryable agent memory. Do NOT use
  just to view results (use genius-web-search) or to read a page body without
  saving it (use genius-web-crawl).
license: MIT
tags: [genius, knowledge-graph, ingestion, search, documents, epistemic-graph, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Genius Search Ingest

Push the Genius search/crawl harvest into the ONE epistemic-graph knowledge
graph as **typed OWL nodes + documents**, so a query and its evidence become
durable, queryable agent memory instead of a throwaway result list.

## When to use
- Persist a search's ranked hits into the KG (`:SearchQuery` + `:SearchResult` +
  `:SearchProvider` + `:WebPage` + `:Document`).
- Save crawled markdown pages as `:WebPage` + shared `:Document` text.
- Do both in one shot: run a live search **and** ingest it (`genius_ingest_search`).

## When NOT to use
- Only display results to the user → `genius-web-search`.
- Only read a page body, no persistence → `genius-web-crawl`.
- Ingest arbitrary local files / a crawl `--output-dir` into graph-os generically
  → the platform `mcp_graph-os_graph_ingest` tool.

## Prerequisites & environment
- A reachable epistemic-graph engine (graph-os). With **no** engine every entry
  point cleanly **no-ops** (returns `None`) — search/crawl still work.
- Ingestion rides the shared primitive
  `agent_utilities.knowledge_graph.memory.native_ingest` when present, else a
  self-contained txn over the lightweight `GraphComputeEngine()._client`.
- Provenance is stamped automatically: `source=genius-agent`, `domain=genius`.

## Tools & actions
Python API in `genius_agent.kg_ingest`:

| Function | Maps to |
|----------|---------|
| `genius_ingest_search(query, max_results=10)` | **Wire-First**: runs a real web search, then ingests it |
| `ingest_search_results(query, results, provider=...)` | Already-fetched hits → typed nodes + docs |
| `ingest_crawled_pages(pages)` | Crawled `{url, markdown}` pages → `:WebPage` + `:Document` |
| `map_search_results(...)` | Pure mapper → `(entities, relationships, documents)` (offline/testable) |
| `ingest_entities` / `ingest_documents` | Low-level typed-node / document writers |

Node ids are `genius:<class>:<externalId>`; `type` matches the classes federated
by `genius_agent/ontology/genius.ttl`.

## Recipes
Search **and** ingest in one call (the Wire-First tool):
```python
from genius_agent.kg_ingest import genius_ingest_search
genius_ingest_search("cilium eBPF service mesh", max_results=8)
# -> {"query": ..., "provider": "duckduckgo", "results": 8, "ingested": {"nodes": ..., "edges": ..., "documents": ...}}
```
Ingest hits you already fetched with `genius-web-search`:
```python
from genius_agent.kg_ingest import ingest_search_results
ingest_search_results(
    "openraft consensus",
    [{"title": "openraft", "link": "https://github.com/...", "snippet": "..."}],
    provider="duckduckgo",
)
```
Ingest crawled pages from `genius-web-crawl`:
```python
from genius_agent.kg_ingest import ingest_crawled_pages
ingest_crawled_pages([{"url": "https://docs.example.com/g", "markdown": "# Guide\n..."}])
```

## Gotchas
- Everything is **best-effort**: no engine ⇒ `None`, never an exception.
- Result field names vary by provider; the mapper normalizes `link`/`url`/`FirstURL`
  and `snippet`/`body`/`Text`, but a hit with no URL is skipped.
- Retrieved text lands on the **shared** `:Document` class (never redefined by
  this package); hub-side enrichment chunks/embeds it for semantic search.
- Ids are content-hashed on `(provider|query)` and target URL, so re-ingesting the
  same query MERGEs (idempotent) rather than duplicating.

## Related
- `genius-web-search` / `genius-web-crawl` — produce what this ingests.
- `agent-utilities-source-integration` — the fleet-wide native ingestion pattern.
