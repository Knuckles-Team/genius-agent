---
name: genius-web-search
skill_type: skill
description: >-
  Multi-provider web search via Genius Agent — get ranked titles, snippets, and
  URLs for a query from DuckDuckGo, Google, Bing, or Searxng. Use when the agent
  needs current, real-time information from the open web, references/links to
  authoritative pages, or a candidate set of URLs to then crawl. Do NOT use to
  read the full body of a page (use genius-web-crawl) or to persist results into
  the knowledge graph (use genius-search-ingest).
license: MIT
tags: [genius, web, search, duckduckgo, google, bing, searxng, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Genius Web Search

Run web searches across pluggable providers and get back structured hits
(`title`, `link`, `snippet`). Provider is auto-selected from the environment;
DuckDuckGo is the zero-config default.

## When to use
- Answer a question that needs up-to-date / real-time information.
- Find authoritative references or a candidate set of URLs on a topic.
- Produce the seed URLs that `genius-web-crawl` will then read in full.

## When NOT to use
- Read or extract the full markdown body of a page → `genius-web-crawl`.
- Persist the hits into the epistemic-graph KG → `genius-search-ingest`
  (or its `genius_ingest_search` tool, which searches *and* ingests in one call).
- Deep multi-source, adversarially-verified research reports → the
  `deep-research` skill.

## Prerequisites & environment
Genius Agent bundles the `universal-skills[web-search]` scripts. Provider is
chosen by which credentials are present (first match wins):

| Variable(s) | Provider | Notes |
|-------------|----------|-------|
| _(none)_ | DuckDuckGo | Free, no key — the default fallback |
| `SEARXNG_URL` | Searxng | Self-hosted / public metasearch instance |
| `GOOGLE_API_KEY` + `GOOGLE_CX` | Google | Custom Search API + engine id |
| `BING_API_KEY` | Bing | Bing Web Search API |
| `SSL_VERIFY` | _(all)_ | Toggle TLS verification (default on) |

Connect via the `mcp-client` skill against the **`genius-agent`** MCP server, or
call the bundled scripts directly.

## Tools & actions
- Dispatcher (auto-selects provider): `scripts/search.py --query "<q>" --json`
- Provider-specific: `scripts/search_duckduckgo.py`, `scripts/search_google.py`,
  `scripts/search_bing.py`, `scripts/search_searxng.py`.

### Key parameters
- `--query` — required; the search string.
- `--max-results` / `--max_results` — cap the hit count (default 10).
- `--json` — emit machine-readable results (list of `{title, link, snippet}`).
- `--insecure` — disable TLS verification (prefer `SSL_VERIFY` env).

## Recipes
Auto-provider search, JSON out:
```bash
python scripts/search.py --query "cilium eBPF service mesh 2026" --max-results 8 --json
```
Force DuckDuckGo (no keys needed):
```bash
python scripts/search_duckduckgo.py --query "openraft vs multi-paxos" --max-results 5 --json
```
Searxng against a self-hosted instance:
```bash
SEARXNG_URL=https://searx.example.org python scripts/search_searxng.py --query "OWL RDF reasoner benchmark" --json
```

## Gotchas
- Result fields are `title`, `link`, `snippet` — note `link`, not `url`
  (the ingest mapper normalizes both).
- DuckDuckGo's instant-answer API is sparse for some queries; if you get few
  hits, configure Searxng/Google/Bing for fuller coverage.
- Keep `--max-results` modest to avoid burning tokens on low-value snippets.
- Set keys via the environment, never on the command line, to avoid leaking
  them into process listings / logs.

## Related
- `genius-web-crawl` — read the full body of the URLs this returns.
- `genius-search-ingest` — search + persist hits as KG `:SearchResult`/`:Document`.
- `web-search` (universal) — the underlying provider scripts.
