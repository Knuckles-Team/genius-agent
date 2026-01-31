---
name: ingest
description: Pipeline for ingesting content from URLs or documents directory into the Knowledge Graph and Vector Database.
---

### Overview
This skill defines a robust pipeline for gathering information and populating the agent's long-term memory. It orchestrates the process of extracting content (via scraping) and ingesting it into both the Knowledge Graph (Graphiti) and Vector Database (Vector MCP).

### Capabilities
- **Ingest from URL**: Crawl a website, converting content to Markdown, and storing it in both databases.

### Workflow: URL Ingestion
1.  **Download & Ingest**
    - Use the `ingest` tool to ingest the contents from the provided URL(s) into the vector and graph databases.

### Tools and Skills Used
- `ingest` tool: For ingesting the contents from the provided URL(s) into the vector and graph databases.

### Example Prompt
- "Ingest the documentation at https://ai.pydantic.dev"
