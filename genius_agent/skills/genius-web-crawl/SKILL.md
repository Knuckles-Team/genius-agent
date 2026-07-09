---
name: genius-web-crawl
skill_type: skill
description: >-
  Crawl web pages, whole sites, or sitemaps to clean markdown via Genius Agent —
  single page, chunked-by-heading, recursive link-following, or sitemap
  sequential/parallel. Use when the agent must read the full body of a page,
  harvest online documentation, or bulk-extract a site into markdown for
  analysis or KG ingestion. Do NOT use to get a ranked list of links for a query
  (use genius-web-search) or for a single quick JSON API fetch.
license: MIT
tags: [genius, web, crawler, docs, scrape, extract, markdown, sitemap, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Genius Web Crawl

Turn URLs into clean markdown with `crawl4ai`-backed strategies: a single page,
heading-chunked output, recursive in-site crawling, or full sitemap processing.

## When to use
- Read the complete content of a page found via `genius-web-search`.
- Harvest an online documentation set (docs site / sitemap) into markdown.
- Recursively crawl a site section for analysis or KG ingestion.

## When NOT to use
- Get a ranked list of result links for a query → `genius-web-search`.
- Persist crawled pages into the epistemic-graph KG → `genius-search-ingest`
  (or ingest the output directory with `ingest_crawled_pages`).
- A one-off structured JSON API call → a plain HTTP fetch.

## Prerequisites & environment
Genius Agent bundles the `universal-skills[web-crawler]` scripts (needs
`crawl4ai` + a headless browser). Connect via the `mcp-client` skill against the
**`genius-agent`** MCP server, or run `scripts/crawl.py` directly.

## Tools & actions
`scripts/crawl.py --urls <url> --strategy <strategy> [options]`

| Strategy | What it does |
|----------|--------------|
| `single` | One page → markdown (stdout is fine) |
| `chunked` | One page, split on H1/H2 headings |
| `recursive` | Follow internal links up to `--max-depth` (path-prefix scoped) |
| `sitemap-sequential` | Crawl every URL in `sitemap.xml`, one session |
| `sitemap-parallel` | Crawl a sitemap concurrently (memory-adaptive) |

### Key parameters
- `--urls` — page URL, or a `sitemap.xml` URL for sitemap strategies.
- `--output-dir` — **required** for sitemap/recursive crawls (saves one `.md` per page).
- `--max-depth` (recursive, default 3), `--max-pages` (default 500),
  `--max-concurrent` (default 10).
- `--wait-for` — CSS selector / JS expr to await dynamic content.
- `--insecure` — disable SSL verification; `--disable-magic-js` for clean static sites.

## Recipes
Single page to stdout:
```bash
python scripts/crawl.py --urls https://docs.example.com/guide --strategy single
```
Recursive section crawl to a directory:
```bash
python scripts/crawl.py --urls https://docs.example.com/api/ --strategy recursive --max-depth 2 --output-dir ./crawled
```
Whole docs site via sitemap (parallel):
```bash
python scripts/crawl.py --urls https://docs.example.com/sitemap.xml --strategy sitemap-parallel --max-concurrent 10 --output-dir ./docs
```

## Gotchas
- Always pass `--output-dir` for `recursive` and `sitemap-*` — without it, large
  crawls flood stdout.
- `single`/`recursive` on a bare URL auto-discovers `robots.txt` + `/sitemap.xml`
  and may switch to `sitemap-parallel` for full coverage.
- Recursive mode enforces a path-prefix filter to stay in-section; pass
  `--ignore-prefix-restriction` to disable.
- Heavy JS scrubbing runs by default; use `--disable-magic-js` on clean static sites.

## Related
- `genius-web-search` — produce the seed URLs to crawl.
- `genius-search-ingest` — push crawled pages into the KG as `:WebPage`/`:Document`.
- `web-crawler` (universal) — the underlying `crawl.py` strategies.
