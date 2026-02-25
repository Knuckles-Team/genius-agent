---
name: comprehensive-search
description: Unified search capability that intelligently combines Vector Search, Knowledge Graph, and Web Search.
tags: [comprehensive-search]
---

### Overview
This is the primary search skill for the agent. It implements a tiered search strategy to ensure the most accurate, relevant, and grounded answers. It prioritizes the agent's internal memory (Vector/Graph) before resorting to external web search.

### Strategy (Order of Operations)
1.  **Internal Search (Memory)**:
    - **Step 1**: Always query the **Vector Database** (`vector_search`), **Knowledge Graph** (`search_knowledge_base`), and **Document Database** (`find`) first.
    - **Step 2**: Analyze the results. Do they fully answer the user's question with high confidence?
    - **Step 3**: If yes, synthesize the answer and Stop.

2.  **External Search (Discovery)**:
    - **Step 4**: If internal memory is insufficient, perform a **Web Search** (`web_search` via SearXNG).
    - **Step 5**: Analyze the search snippets.

3.  **Deep Dive (Acquisition)**:
    - **Step 6**: If a web search result looks promising but lacks detail, use **Web Scraping** (`crawl` or `md`) to read the full page.
    - **Step 7**: (Optional) Trigger the `ingest` tool (from Ingestion Skill) with the desired URL or document paths to save this new high-value info if relevant to the existing knowledge base.

### Tools
- `vector_search` (Vector MCP): Semantic search.
- `search_knowledge_base` (Graphiti): Graph/Fact search.
- `find` (DocumentDB MCP): Document search.
- `web_search` (SearXNG): Live web search.
- `ingestion` (Ingestion Skill): Save new high-value info to the knowledge base.
- `crawl` (Crawl4AI): Multiple page fetching.
- `md` (Crawl4AI): Single page fetching as Markdown.

### Usage Rules
- **Never** skip the internal search step. Check what you know first.
- **Always** cite the source (Vector Doc, Graph Fact, or Web URL).
- Use `web_search` only when internal knowledge is missing or outdated.
