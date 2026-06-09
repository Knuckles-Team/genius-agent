# Installation

`genius-agent` is a standard Python package and a prebuilt container image. Pick the
path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A model provider API key (OpenAI, OpenRouter, Vertex AI, or any provider supported
  by `agent-utilities`).
- Optionally, a reachable MCP server (or `mcp_config.json`) to provide the agent's
  tool surface — see [Deployment](deployment.md).

## From PyPI (recommended)

```bash
pip install genius-agent
```

### Optional extras

The base install pulls in the `agent-utilities[agent,logfire]` core. Install an extra
for additional capability:

| Extra | Install | Pulls in |
|---|---|---|
| `test` | `pip install "genius-agent[test]"` | `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist` for the test suite |
| `all` | `pip install "genius-agent[all]"` | Every optional dependency above |

```bash
# Typical: the agent runtime with everything enabled
pip install "genius-agent[all]"
```

## From source

```bash
git clone https://github.com/Knuckles-Team/genius-agent.git
cd genius-agent
pip install -e ".[all]"          # editable install with every extra
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run genius-agent
```

## Prebuilt Docker image

A multi-stage, slim image is published on every release (installs
`genius-agent[all]`, entrypoint `genius-agent`):

```bash
docker pull knucklessg1/genius-agent:latest

docker run --rm -i \
  -e API_KEY=your_model_provider_key \
  -e MODEL_NAME=openai/gpt-4o \
  knucklessg1/genius-agent:latest
```

For an HTTP agent server with a published port and the Agent Web UI, see
[Deployment](deployment.md).

## Verify the install

```bash
genius-agent --help
python -c "import genius_agent; print(genius_agent.__doc__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived agent server behind Caddy + DNS.
- **[Usage](usage.md)** — drive the agent, the MCP tool surface, and the CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
