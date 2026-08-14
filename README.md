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

*Version: 4.1.0*

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

## MCP source connector

Run the native MCP surface with `genius-mcp`. Its signed source tool,
`genius_ingest_search`, searches through the configured provider and idempotently
materializes ranked evidence into epistemic-graph. Tool discovery requires no upstream
connection; search credentials, graph connectivity, TLS trust, tenant, and policy are
all supplied at runtime through AgentConfig and the environment.

```bash
uvx --from genius-agent genius-mcp
```

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
    image: <registry>/genius-agent@sha256:<digest>
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

Graph architecture, governed skill integration, and agent execution guidance are
documented in [docs/overview.md](docs/overview.md) and
[docs/usage.md](docs/usage.md).

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
| `genius-agent[mcp]` | MCP server (`agent-utilities[mcp]`) plus the mandatory full epistemic-graph base runtime | You run the MCP tool surface without the integrated agent runtime |
| `genius-agent[agent]` | Current agent runtime (`agent-utilities[agent,logfire]`) plus the mandatory full epistemic-graph base runtime | You run the **integrated agent** (the primary surface) |
| `genius-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# MCP serving runtime
uv pip install "genius-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine) — recommended
uv pip install "genius-agent[agent]"

# Everything (development)
uv pip install "genius-agent[all]"      # or: python -m pip install "genius-agent[all]"
```

### Knowledge-graph database (`epistemic-graph`)

Every install receives `epistemic-graph[full]` through the current Agent Utilities
base dependency. The `[mcp]` and `[agent]` extras add their respective tool and agent
runtime layers without changing that database contract. For production — or to share
one knowledge graph across multiple agents — run **epistemic-graph as its own database
service** and point the agent at it. Deployment recipes (single-node + Raft HA),
connection config, and the full database architecture are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | secret-injected |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | secret-injected |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `OTEL_EXPORTER_OTLP_HEADERS` | — | OTLP auth header, e.g. "Authorization=Basic <token>" |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `WORKSPACE_DIR` | — | workspace root supplied by the launcher |
| `MCP_CONFIG` | `mcp_config.json` | path to the MCP config the agent loads |
| `GRAPH_DB_PATH` | — | path to the local graph DB backing store |
| `GRAPHDB_PASSWORD` | secret-injected | password for the FalkorDB / graph DB backend |
| `FALKORDB_URI` | — | FalkorDB/Redis connection URI (scripts/validate_falkordb.py) |
| `SEARXNG_URL` | — | SearXNG instance URL; when set, web search uses SearXNG |
| `GOOGLE_API_KEY` | secret-injected | Google Custom Search API key (used together with GOOGLE_CX) |
| `GOOGLE_CX` | — | Google Custom Search Engine ID (used together with GOOGLE_API_KEY) |
| `BING_API_KEY` | secret-injected | Bing Search API key |
| `AGENT_UTILITIES_TESTING` | `true` | set "true" to skip live integration tests |
| `A2A_URL` | — | base URL of the running A2A agent endpoint (scripts/validate_a2a_agent.py) |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `TRANSPORT` | `stdio` | MCP transport: `stdio` \| `streamable-http` \| `sse` |
| `HOST` | `127.0.0.1` | Loopback bind host (set an authenticated ingress explicitly) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_TOOL_MODE` | `intent` | Tool surface: `intent` \| `condensed` \| `verbose` \| `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_20 package + 19 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
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

### Web search providers
Provider is selected in priority order: Searxng > Google > Bing > DuckDuckGo (default, no key required).

| Variable | Description | Default |
|----------|-------------|---------|
| `SEARXNG_URL` | SearXNG instance URL | — |
| `GOOGLE_API_KEY` | Google Custom Search API key (with `GOOGLE_CX`) | — |
| `GOOGLE_CX` | Google Custom Search Engine ID (with `GOOGLE_API_KEY`) | — |
| `BING_API_KEY` | Bing Search API key | — |

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

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=example&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/example)
![GitHub User's stars](https://img.shields.io/github/stars/example)

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

<!-- BEGIN agent-utilities-deployment (generated; do not edit between markers) -->

## Deploy with `agent-utilities-deployment`

Provision this package with the consolidated **`agent-utilities-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `genius-agent` with agent-utilities-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "genius-agent[mcp]"`, then run `genius-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `genius-mcp` |
| Immutable container | deploy `registry.example.invalid/genius-agent@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-utilities-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, GraphOS delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
