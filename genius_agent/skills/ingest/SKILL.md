---
name: ingest
description: Pipeline for ingesting content from URLs or documents directory into the Knowledge Graph, Vector Database, and Document Database.
tags: [ingest]
---

### Overview
This skill defines a robust pipeline for gathering information and populating the agent's long-term memory. It orchestrates the process of extracting content (via scraping) and ingesting it into the Knowledge Graph (Graphiti), Vector Database (Vector MCP), and Document Database (DocumentDB).

### Capabilities
- **Ingest from URL or Path**: Ingest content from a list of URLs or local file paths.
- **Optional Crawling**: Optionally crawl specific URLs to a configured depth.

### Workflow: Ingestion
1.  **Ingest Content**
    - Use the `ingest` tool with a list of `path`s (URLs or local files).
    - Set `crawl=True` if you want to recursively crawl the provided URLs.
    - The tool handles downloading, parsing, and ingesting into Vector, Graph, and Document databases.

### Tools and Skills Used
- `ingest` tool: For ingesting content from URLs or local paths into the vector, graph, and document databases.

### Example Prompt
- "Ingest the documentation at https://ai.pydantic.dev"
- "Ingest the files in /home/user/docs and also https://example.com"
