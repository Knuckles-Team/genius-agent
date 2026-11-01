# CONN-GENIUS-AGENT-CONNECTOR-CONTENT — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it. The generator sets each row's state in `status.json`.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-GENIUS-AGENT-CONNECTOR-CONTENT-R001` | **Default content.** `pyproject.toml` declares `genius-agent` as the single `scion_sdk.connector` entry point. The server lists the packaged `skill://` and `ontology://` resources and the packaged prompts with no `content=` argument. Proving test: `tests/test_default_content_surfaces.py`. Caller chain: The `genius-mcp` console script in pyproject.toml runs `scion_sdk.cli:serve`, which loads the `scion_sdk.connector` entry point `genius-mcp = genius_agent:connector` and builds the server from `genius_agent/__init__.py::connector`, whose `register_tools` in `genius_agent/mcp_server.py` adds `genius_ingest_search`. Shape: The row declares `genius-agent` as the entry point name but pyproject.toml names it `genius-mcp`, so rename the entry point or the row; the test builds the server with `scion_sdk.connector.build_server` and reuses `ConnectorContent.for_package` defaults from `scion_sdk.mcp.content` for `genius_agent/skills` and `genius_agent/ontology`. | `resources/list` includes `skill://` and `ontology://`; `prompts/list` includes each packaged prompt. Planned test: `tests/test_default_content_surfaces.py::test_default_content_lists_skill_and_ontology_resources_and_prompts`. |
