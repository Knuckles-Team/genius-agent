# Usage — Agent / MCP / CLI

`genius-agent` exposes its capability three ways: as an **integrated agent** you drive
over ACP / the Web UI, as an **MCP tool surface** an orchestrator composes, and as a
**CLI** you launch directly. The full capability set and enterprise-readiness matrix
are in [Overview](overview.md).

## As an MCP server

`genius-agent` composes the tools of the MCP servers declared in its
`mcp_config.json` (or reached via `MCP_URL`) into a single orchestration plane, and
exposes its graph-flow capability over MCP. Reads work with no configuration beyond a
model provider key; authorization is enforced through Eunomia when
`EUNOMIA_TYPE=embedded` or `remote`.

| Capability | Description |
|---|---|
| `run_graph_flow` | Execute a multi-step workflow through the agent's Pydantic-Graph orchestration engine (declared in [`a2a.json`](https://github.com/Knuckles-Team/genius-agent/blob/main/a2a.json)). |
| Composed MCP tools | Every tool registered by the MCP servers in `mcp_config.json` becomes callable through the agent. |

Example prompts that drive the agent:

- *"Run the deployment workflow against the staging environment."* → `run_graph_flow`
- *"Search the catalog and summarize the top results."* → a composed MCP tool call
- *"Plan a multi-step task and execute each step."* → graph orchestration

## As a Python API

The agent server is launched programmatically through the package entry point. The
`agent_server()` function builds and runs the integrated agent from the environment:

```python
from genius_agent.agent_server import agent_server

# Builds the Pydantic-AI graph agent from API_KEY / MODEL_NAME / DEFAULT_SYSTEM_PROMPT
# and the MCP tool surface, then serves ACP + the Agent Web UI.
agent_server()
```

Under the hood it composes the `agent-utilities` building blocks
(`create_agent_server`, `build_system_prompt_from_workspace`, `load_identity`,
`initialize_workspace`), so the agent identity, system prompt, and workspace are
resolved from the environment and the bundled `agent_data/` workspace.

## As a CLI

The `genius-agent` console script is the primary entry point. Provide a model
provider and identity, then run:

```bash
export API_KEY=your_model_provider_key
export MODEL_NAME=openai/gpt-4o
export DEFAULT_SYSTEM_PROMPT="You are Genius Agent, an orchestration specialist."

# Interactive terminal agent
genius-agent --provider openai --model-id gpt-4o

# Networked agent server with the Web UI + ACP
genius-agent --provider openai --model-id gpt-4o --host 0.0.0.0 --port 9000 --web
```

Connect the agent to a remote MCP tool surface:

```bash
MCP_URL=http://your-mcp-host:8000/mcp \
  genius-agent --provider openai --model-id gpt-4o
```

Inspect every available flag:

```bash
genius-agent --help
```

Each optional capability reads its own credentials and remains inactive when those
credentials are absent. The full environment set is documented in
[`.env.example`](https://github.com/Knuckles-Team/genius-agent/blob/main/.env.example).
