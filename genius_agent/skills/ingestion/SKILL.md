---
name: ingestion
description: Pipeline for ingesting content from URLs or documents into the Knowledge Graph and Vector Database.
---

### Overview
This skill defines a robust pipeline for gathering information and populating the agent's long-term memory. It orchestrates the process of extracting content (via scraping) and ingesting it into both the Knowledge Graph (Graphiti) and Vector Database (Vector MCP).

### Capabilities
- **Ingest from URL**: Crawl a website, converting content to Markdown, and storing it in both databases.
- **Ingest from Directory**: (Requires Filesystem Tools) Read local markdown files and store them in both databases.

### Workflow: URL Ingestion
1.  **Crawl & Extract**:
    - Use the `crawl` tool (from `crawl4ai`) to fetch the content of the provided URL(s).
    - Ensure you get the 'markdown' output.
2.  **Vector Ingestion**:
    - Use `add_documents` (from `vector-mcp`) to store the extracted markdown chunks.
    - Ensure appropriate metadata (Source URL, Title) is attached.
3.  **Graph Ingestion**:
    - Use `add_episode` (from `graphiti`) to add the content to the Knowledge Graph.
    - This creates the entity relationships and temporal facts.

### Workflow: Directory Ingestion
1.  **Vector Ingestion**:
    - Use `add_documents` (from `vector-mcp`) to store the extracted markdown chunks from the supplied documents directory.
    - Ensure appropriate metadata (Source URL, Title) is attached.
2.  **Graph Ingestion**:
    - Use `add_episode` (from `graphiti`) to add the content to the Knowledge Graph from the supplied documents directory.
    - This creates the entity relationships and temporal facts.

### Tools Used
- `crawl` (Crawl4AI): For fetching web content.
- `add_documents` (Vector MCP): For semantic search indexing.
- `add_episode` (Graphiti): For knowledge graph indexing.

### Example Prompt
- "Ingest the documentation at https://docs.example.com"
- "Scrape this blog post https://example.com/blog/ai and save it to my memory"
