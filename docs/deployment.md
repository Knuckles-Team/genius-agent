# Deployment

This page covers running `genius-agent` as a long-lived server: the transports, a
Docker Compose stack, putting it behind a Caddy reverse proxy, and giving it a DNS
name with Technitium.

> `genius-agent` ships an integrated **Agent (A2A/ACP) server** (console script
> `genius-agent`) that also exposes and consumes an **MCP tool surface**. The agent
> connects to MCP servers declared in `mcp_config.json` or to a remote endpoint via
> `MCP_URL`, composing their tools into one orchestration plane.

## Run the agent server

The agent server runs the Pydantic-AI graph agent with the Agent Web UI (AG-UI), the
Agent Control Protocol (ACP), and an interactive terminal interface. Select the model
provider with `--provider` / `--model-id`:

=== "Interactive terminal"

    ```bash
    genius-agent --provider openai --model-id gpt-4o
    ```
    Launches the agent with the terminal interface for local interaction.

=== "Networked (Web UI + ACP)"

    ```bash
    genius-agent --provider openai --model-id gpt-4o \
      --host 0.0.0.0 --port 9000 --web
    ```
    A network server exposing the Agent Web UI and ACP on `:9000` with a `/health`
    endpoint.

=== "Connected to a remote MCP surface"

    ```bash
    MCP_URL=http://your-mcp-host:8000/mcp \
      genius-agent --provider openai --model-id gpt-4o --host 0.0.0.0 --port 9000
    ```

Health check (networked mode):

```bash
curl -s http://localhost:9000/health        # {"status":"OK"}
```

## Configuration (environment)

`genius-agent` is configured entirely from the environment. The **required** set to
bring the agent online:

| Var | Default | Meaning |
|---|---|---|
| `API_KEY` | _(unset)_ | Model provider API key |
| `MODEL_NAME` | `google/vertexai` | Provider/model identifier |
| `DEFAULT_SYSTEM_PROMPT` | _(unset)_ | System prompt for the agent identity |
| `ENABLE_OTEL` | `True` | Enable OpenTelemetry / Langfuse export |
| `EUNOMIA_TYPE` | `none` | Authorization mode: `none`, `embedded`, or `remote` |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` | Local policy file for `embedded` mode |
| `MCP_URL` | _(unset)_ | Remote MCP tool surface the agent connects to |

Plus `HOST` / `PORT` / `PROVIDER` / `MODEL_ID` for the networked server, and the OTEL
exporter settings (`OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_EXPORTER_OTLP_PUBLIC_KEY`,
`OTEL_EXPORTER_OTLP_SECRET_KEY`, `OTEL_EXPORTER_OTLP_PROTOCOL`). The complete set,
including the optional tool toggles, is documented in
[`.env.example`](https://github.com/Knuckles-Team/genius-agent/blob/main/.env.example).
Copy it to `.env` and populate only what you use; the agent remains inactive when the
provider credentials are absent.

!!! note "Backing service"
    `genius-agent` is a self-contained orchestration agent — it has no external
    backing system to provision. It connects outward to model providers and MCP
    servers; only connection configuration is required.

## Docker Compose

The repo ships [`docker/agent.compose.yml`](https://github.com/Knuckles-Team/genius-agent/blob/main/docker/agent.compose.yml).
It reads a sibling `.env` and publishes the agent server (Web UI + ACP) on `:9000`:

```yaml
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
```

```bash
cp .env.example .env          # then edit API_KEY / MODEL_NAME values
docker compose -f docker/agent.compose.yml up -d
docker compose -f docker/agent.compose.yml logs -f
```

## Agent server details

| Property | Value |
|---|---|
| Console script | `genius-agent` (entry: `genius_agent.agent_server:agent_server`) |
| Default port | `9000` (Web UI + ACP) |
| Compose file | [`docker/agent.compose.yml`](https://github.com/Knuckles-Team/genius-agent/blob/main/docker/agent.compose.yml) |
| MCP wiring | `MCP_URL` (remote endpoint) or `mcp_config.json` (local declarations) |
| Agent manifest | [`a2a.json`](https://github.com/Knuckles-Team/genius-agent/blob/main/a2a.json) — declares the `run_graph_flow` capability |

The agent consumes MCP tools rather than terminating at a single backing API. Point
`MCP_URL` at a running MCP server, or mount an `mcp_config.json` that declares the
servers the agent should compose.

## Behind a Caddy reverse proxy

Expose the agent server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
genius-agent.arpa {
    tls internal
    reverse_proxy genius-agent-agent:9000
}
```

```caddy
# Public — automatic Let's Encrypt
genius-agent.example.com {
    reverse_proxy genius-agent-agent:9000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=genius-agent.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `genius-agent.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

`genius-agent` is itself an agent that consumes MCP tools, and it can also be
registered with an MCP client. Add to your client's `mcp_config.json`:

```json
{
  "mcpServers": {
    "genius-agent": {
      "command": "uv",
      "args": ["run", "genius-agent"],
      "env": {
        "API_KEY": "your_model_provider_key",
        "MODEL_NAME": "openai/gpt-4o",
        "ENABLE_OTEL": "false"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://genius-agent.arpa/mcp` instead.
