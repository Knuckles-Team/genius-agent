# Genius Agent
## CLI or API | Agent

![PyPI - Version](https://img.shields.io/pypi/v/genius-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/genius-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/genius-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/genius-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/genius-agent)
![PyPI - License](https://img.shields.io/pypi/l/genius-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/genius-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/genius-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/genius-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/genius-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/genius-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/genius-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/genius-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/genius-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/genius-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/genius-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/genius-agent)

*Version: 2.44.0*

> **Documentation** — Installation, deployment, usage across the agent, MCP, and CLI
> interfaces are maintained in the
> [official documentation](https://knuckles-team.github.io/genius-agent/).

---

## Overview

**Genius Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with GeniusAgent Search Engine for Agentic AI!.

---

## Key Features

- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the GeniusAgent Search Engine for Agentic AI! API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Optional: override the agent's identity / workspace
export DEFAULT_AGENT_NAME="Genius Agent"
export WORKSPACE_DIR="/path/to/workspace"

# Run the agent server (provider / model / key are CLI args)
genius-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  genius-agent-agent:
    image: knucklessg1/genius-agent:latest
    container_name: genius-agent-agent
    hostname: genius-agent-agent
    restart: always
    env_file:
      - ../.env
    command: [ "genius-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9000
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9000:9000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `genius-agent[mcp]` | Slim MCP/runtime base only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only need the lightweight tool-hosting base (smallest install) |
| `genius-agent[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** (the primary surface) |
| `genius-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# Slim base (smallest install)
uv pip install "genius-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine) — recommended
uv pip install "genius-agent[agent]"

# Everything (development)
uv pip install "genius-agent[all]"      # or: python -m pip install "genius-agent[all]"
```

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` base does **not** require the database.

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | `pk-...` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | `sk-...` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `OTEL_EXPORTER_OTLP_HEADERS` | — | OTLP auth header, e.g. "Authorization=Basic <token>" |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `WORKSPACE_DIR` | `/home/apps/workspace/agent-packages` | workspace root the agent initializes from |
| `MCP_CONFIG` | `mcp_config.json` | path to the MCP config the agent loads |
| `GRAPH_DB_PATH` | — | path to the local graph DB backing store |
| `GRAPHDB_PASSWORD` | `letmein` | password for the FalkorDB / graph DB backend |
| `AGENT_UTILITIES_TESTING` | `true` | set "true" to skip live integration tests |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `TRANSPORT` | `stdio` | MCP transport: `stdio` | `streamable-http` | `sse` |
| `HOST` | `0.0.0.0` | Bind host (HTTP transports) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET` | — | OIDC client secret (service-account auth) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_14 package + 17 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the agent reads, grouped by purpose.

### Agent runtime
| Variable | Description | Default |
|----------|-------------|---------|
| `DEFAULT_AGENT_NAME` | Override the agent's identity name | `Genius Agent` |
| `AGENT_DESCRIPTION` | Override the agent description | identity / built-in |
| `AGENT_SYSTEM_PROMPT` | Override the agent system prompt | identity / workspace-derived |
| `WORKSPACE_DIR` | Agent workspace directory | — |
| `MCP_URL` | URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `MCP_CONFIG` | Path to an `mcp_config.json` for downstream tool servers | `mcp_config.json` |
| `PROVIDER` | LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `LLM_API_KEY` | LLM provider API key | — |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface | `True` |
| `GRAPH_DB_PATH` | Path to the local epistemic-graph database file | — |
| `GRAPHDB_PASSWORD` | Password for an external graph database | — |
| `HOST` | Bind host | `0.0.0.0` |
| `PORT` | Bind port | `9000` |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_HEADERS` | OTLP exporter headers | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |

See [`.env.example`](.env.example) for a copy-paste starting point.

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/genius-agent/) and is the
recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/genius-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/genius-agent/deployment/) | run the agent server, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/genius-agent/usage/) | the agent, the MCP tool surface, the CLI |
| [Overview](https://knuckles-team.github.io/genius-agent/overview/) | capabilities, enterprise readiness, configuration |
| [Concepts](https://knuckles-team.github.io/genius-agent/concepts/) | concept registry (`CONCEPT:GENIUS-*`) |

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `genius-agent` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx genius-agent-mcp` · or `uv tool install genius-agent` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/genius-agent:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
