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

*Version: 2.25.0*

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

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](file:///home/apps/workspace/agent-packages/agents/genius-agent/docs/index.md).

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export API_KEY="your_value"
export MODEL_NAME="your_value"
export DEFAULT_SYSTEM_PROMPT="your_value"
export SERVICENOW_INSTANCE="your_value"
export SERVICENOW_USERNAME="your_value"
export OPENROUTER_API_KEY="your_value"
export SERVICENOW_PASSWORD="your_value"

# Run the agent server
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

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](file:///home/apps/workspace/agent-packages/agents/genius-agent/docs/agent.md).

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

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install genius-agent[all]

# Using standard pip
python -m pip install genius-agent[all]
```

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
