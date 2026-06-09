# genius-agent

A production-grade **Agent (A2A) + MCP** orchestration server for agentic AI,
built on the `agent-utilities` core.

!!! info "Official documentation"
    This site is the canonical reference for `genius-agent`, maintained alongside every
    release.

[![PyPI](https://img.shields.io/pypi/v/genius-agent)](https://pypi.org/project/genius-agent/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/genius-agent)](https://github.com/Knuckles-Team/genius-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/genius-agent)

## Overview

`genius-agent` is a fully integrated Pydantic-AI graph agent and Model Context
Protocol (MCP) surface for the agent-utilities ecosystem. It provides:

- **An integrated graph agent** — a Pydantic-AI agent that communicates over the
  Agent Control Protocol (ACP), drives the Agent Web UI (AG-UI), and runs an
  interactive terminal interface.
- **A consumed MCP tool surface** — the agent connects to any MCP server declared in
  `mcp_config.json` (or a remote endpoint via `MCP_URL`), composing their tools into
  a single orchestration plane.
- **Enterprise security and telemetry inherited from `agent-utilities`** — Eunomia
  policy enforcement, OIDC token delegation, OpenTelemetry export, and native
  Langfuse tracing, with guardrails enabled by default.

The agent remains inactive when credentials are absent: provide a model provider key
and a system prompt and the graph agent comes online.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the agent server, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the agent, the MCP tool surface, and the CLI.
- :material-sitemap: **[Overview](overview.md)** — capabilities, enterprise readiness, and configuration.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:GENIUS-*` registry.

</div>

## Quick start

```bash
pip install "genius-agent[all]"
export API_KEY=your_model_provider_key
genius-agent --provider openai --model-id gpt-4o
```

The agent server starts with the Agent Web UI and ACP enabled. To connect it to a
remote MCP tool surface:

```bash
export MCP_URL=http://your-mcp-host:8000/mcp
genius-agent --provider openai --model-id gpt-4o --host 0.0.0.0 --port 9000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, transports, reverse proxy, DNS).
