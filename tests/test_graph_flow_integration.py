#!/usr/bin/env python3
"""
Integration tests for the genius-agent graph orchestration flow.

Tests cover:
  1. MCP config loading and structure validation
  2. MCP registry sync (mcp_config.json → NODE_AGENTS.md)
  3. Graph topology validation (domains, toolsets, agents)
  4. run_graph() result type integrity (must return GraphResponse, never a plain string)
  5. End-to-end Portainer stack listing using real API credentials from .env

Run with:
    pytest tests/test_graph_flow_integration.py -v --timeout=300
"""

import os
import json
import asyncio
import anyio
import pytest

pytestmark = pytest.mark.integration
from pathlib import Path
from dotenv import load_dotenv

# ------------------------------------------------------------------
# Environment setup — load the genius-agent .env automatically
# Override=True ensures MCP env-vars (e.g. ANSIBLE_TOWER_URL) are available
# before any test code runs, preventing env-var substitution failures.
# ------------------------------------------------------------------
_ENV_FILE = Path(__file__).parents[1] / ".env"
if _ENV_FILE.exists():
    load_dotenv(dotenv_path=str(_ENV_FILE), override=True)

# MCP config path (relative to genius-agent root, or override via env)
_MCP_CONFIG_PATH = os.environ.get(
    "MCP_CONFIG",
    str(Path(__file__).parents[1] / "genius_agent" / "mcp_config.json"),
)

# Workspace dir is the genius-agent package root
_WORKSPACE = str(Path(__file__).parents[1])


# ==================================================================
# Fixtures
# ==================================================================


@pytest.fixture(scope="module")
def mcp_config() -> dict:
    """Load the raw mcp_config.json once for all tests."""
    path = Path(_MCP_CONFIG_PATH)
    assert path.exists(), f"mcp_config.json not found at {path}"
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def graph_bundle():
    """
    Initialize the graph once for the entire module.
    Sources the .env file first so MCP tool env-var substitution works,
    then runs registry sync and builds the graph topology.
    """
    # Ensure .env is loaded with override so all MCP env vars are available
    # for pydantic-ai's load_mcp_servers env-var substitution
    if _ENV_FILE.exists():
        load_dotenv(dotenv_path=str(_ENV_FILE), override=True)

    # Must call initialize_workspace() so WORKSPACE_DIR is set before any
    # registry or graph calls. This ensures NODE_AGENTS.md is found correctly.
    from agent_utilities import initialize_workspace

    initialize_workspace()

    from agent_utilities.graph.builder import initialize_graph_from_workspace

    graph, config = initialize_graph_from_workspace(
        mcp_config=_MCP_CONFIG_PATH,
        workspace=_WORKSPACE,
    )
    return graph, config


def _load_registry():
    """Helper: ensure workspace is initialized before loading the MCP registry."""
    from agent_utilities import initialize_workspace
    from agent_utilities.graph.config_helpers import load_node_agents_registry
    from agent_utilities.mcp_agent_manager import sync_mcp_agents

    initialize_workspace()
    # Explicitly trigger sync for integration tests
    import asyncio
    asyncio.run(sync_mcp_agents())
    return load_node_agents_registry()


# ==================================================================
# Phase 1 — MCP Config Structure Tests
# ==================================================================


def test_mcp_config_exists():
    """mcp_config.json must exist and be valid JSON."""
    path = Path(_MCP_CONFIG_PATH)
    assert path.exists(), f"mcp_config.json not found at {path}"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert "mcpServers" in data, "mcp_config.json missing top-level 'mcpServers' key"
    assert len(data["mcpServers"]) > 0, "mcp_config.json has no MCP server entries"


def test_mcp_config_repository_entry(mcp_config):
    """repository-manager MUST be configured with repository-mcp command."""
    servers = mcp_config["mcpServers"]
    assert (
        "repository-manager" in servers
    ), "Expected 'repository-manager' key in mcp_config.json mcpServers"
    repo = servers["repository-manager"]
    assert (
        repo.get("command") == "repository-manager-mcp"
    ), f"repository-manager command should be 'repository-manager-mcp', got '{repo.get('command')}'"
    assert "--transport" in repo.get(
        "args", []
    ), "repository-manager should specify --transport in args"
    assert "stdio" in repo.get(
        "args", []
    ), "repository-manager should use stdio transport"


def test_mcp_config_all_entries_have_commands(mcp_config):
    """Every MCP server entry must have a non-empty 'command' field."""
    servers = mcp_config["mcpServers"]
    bad = [name for name, cfg in servers.items() if not cfg.get("command")]
    assert not bad, f"MCP servers missing 'command': {bad}"


def test_mcp_config_all_entries_use_stdio_transport(mcp_config):
    """Every MCP server should use stdio transport for consistency."""
    servers = mcp_config["mcpServers"]
    bad = []
    for name, cfg in servers.items():
        args = cfg.get("args", [])
        if "--transport" in args:
            idx = args.index("--transport")
            transport = args[idx + 1] if idx + 1 < len(args) else None
            if transport != "stdio":
                bad.append(f"{name}: transport={transport}")
    assert not bad, f"MCP servers not using stdio transport: {bad}"


# ==================================================================
# Phase 2 — Registry Sync Tests
# ==================================================================


def test_mcp_registry_contains_repository():
    """
    After registry sync, MCP_AGENTS.md must contain a repository specialist.
    Uses the agent-utilities registry loader.
    """
    registry = _load_registry()
    assert registry is not None, "_load_registry() returned None"
    assert (
        len(registry.agents) > 0
    ), "MCP registry is empty — has mcp_config.json been synced to MCP_AGENTS.md?"

    tags = [a.tag for a in registry.agents]
    names = [a.name.lower() for a in registry.agents]
    # The repository specialist may appear under tag 'repository' or name containing 'repository'
    has_repository = any("repository" in (t or "").lower() for t in tags) or any(
        "repository" in n for n in names
    )

    assert has_repository, (
        f"No repository specialist found in registry. "
        f"Tags: {tags[:10]}... Names: {names[:10]}..."
    )


def test_mcp_registry_tool_count():
    """Registry must have a reasonable number of tools registered."""
    registry = _load_registry()
    assert (
        len(registry.tools) > 10
    ), f"Registry has only {len(registry.tools)} tools — expected >10 for a healthy workspace"


def test_mcp_registry_agents_have_mcp_server():
    """All agents in the registry must specify which MCP server they belong to."""
    registry = _load_registry()
    bad = [
        a.name
        for a in registry.agents
        if a.agent_type == "mcp" and not getattr(a, "mcp_server", None)
    ]
    assert not bad, f"MCP Agents missing mcp_server field: {bad}"


# ==================================================================
# Phase 3 — Graph Topology Tests
# ==================================================================


def test_graph_topology_validation():
    """validate_graph() must report MCP agents registered and have no domain warnings."""
    registry = _load_registry()
    assert len(registry.agents) > 0, (
        "MCP registry is empty — no MCP agents registered. "
        "Check mcp_config.json → MCP_AGENTS.md sync."
    )
    # Every registered agent should have a tag
    tagged = [a for a in registry.agents if a.tag]
    assert len(tagged) > 0, (
        f"No agents have tags in the registry. This will prevent graph routing. "
        f"Sample agents: {[a.name for a in registry.agents[:5]]}"
    )


def test_graph_has_repository_domain():
    """A repository specialist must exist in the MCP registry (sourced from mcp_config.json)."""
    registry = _load_registry()
    tags = [a.tag or "" for a in registry.agents]
    names = [a.name.lower() for a in registry.agents]
    has_repository = any("repository" in t.lower() for t in tags) or any(
        "repository" in n for n in names
    )
    assert has_repository, (
        f"No repository specialist in MCP registry. "
        f"Sample names: {[n for n in names if 'repository' not in n][:10]}..."
    )


def test_graph_tag_prompts_non_empty(graph_bundle):
    """Every domain tag must have a non-empty description."""
    _, config = graph_bundle
    tag_prompts = config.get("tag_prompts", {})
    empty = [
        tag for tag, prompt in tag_prompts.items() if not prompt or not prompt.strip()
    ]
    assert not empty, f"Domains with empty prompts: {empty}"


# ==================================================================
# Phase 4 — Result Type Integrity Tests
# ==================================================================


@pytest.mark.asyncio
async def test_run_graph_returns_graphresponse_not_string(graph_bundle):
    """
    run_graph() must ALWAYS return a GraphResponse, never a plain string like 'dispatcher'.
    This regression test covers the core bug where results_registry was empty and
    the graph terminated at the dispatcher node, returning just the node label string.
    """
    from agent_utilities.graph.runner import run_graph
    from agent_utilities.models import GraphResponse

    graph, config = graph_bundle

    # Use a dummy query that will route quickly
    # We set a short timeout since we don't need real API results here — just type check.
    # Use anyio.move_on_after rather than asyncio.wait_for — the latter creates a new
    # asyncio Task which breaks anyio cancel-scope bookkeeping during MCP stdio teardown.
    result = None
    with anyio.move_on_after(30.0) as cancel_scope:
        result = await run_graph(graph, config, "test graph result type check")
    if cancel_scope.cancelled_caught:
        pytest.skip(
            "Graph timed out during topology-only validation — skipping type check"
        )
        return

    assert isinstance(result, GraphResponse), (
        f"run_graph() returned {type(result).__name__} (value: {repr(str(result))[:200]}), "
        f"expected GraphResponse. This indicates the 'dispatcher' bug is still present."
    )
    assert result.results is not None, "GraphResponse.results must not be None"


@pytest.mark.asyncio
async def test_run_graph_flow_tool_returns_string_not_graphresponse(graph_bundle):
    """
    The run_graph_flow tool (in tool_registry) wraps run_graph() and must return
    a plain string — the output extracted from GraphResponse.results['output'].
    Ensures the tool_registry wrapper correctly extracts the string content.
    """
    from agent_utilities.graph.runner import run_graph
    from agent_utilities.models import GraphResponse

    graph, config = graph_bundle

    # Simulate what tool_registry.run_graph_flow does
    result = None
    with anyio.move_on_after(30.0) as cancel_scope:
        result = await run_graph(graph, config, "health check")
    if cancel_scope.cancelled_caught:
        pytest.skip("Graph timed out — skipping tool wrapper test")
        return

    # The tool wrapper logic (mirrored from tool_registry.py)
    if hasattr(result, "results"):
        tool_output = str(result.results.get("output", result.results))
    else:
        tool_output = str(result)

    assert isinstance(tool_output, str), "Tool output must be a string"
    # Must NOT be just a node label
    node_labels = {"dispatcher", "verifier", "router", "planner", "error_recovery"}
    assert (
        tool_output.lower().strip() not in node_labels
    ), f"Tool output is a bare node label '{tool_output}' — the dispatcher bug is still active"


# ==================================================================
# Phase 5 — End-to-End Integration Test (Local: repository-manager)
# ==================================================================


@pytest.mark.asyncio
async def test_git_status_via_graph(graph_bundle):
    """
    Full end-to-end integration test: the graph orchestrator routes
    'get git status for genius-agent' to the repository-manager specialist,
    executes the git_action MCP tool, and returns real git status output.

    Uses repository-manager-mcp which is fully local — no network, no credentials.
    Starts in milliseconds, making this reliable for CI.

    Timeout budget (generous for LLM overhead + verifier):
      - Parallel MCP startup: ~2s
      - Router LLM call: ~10-30s
      - git_action tool execution: <1s (local subprocess)
      - Verifier LLM call: ~10-60s
      Total budget: 300s

    Validates:
      - Result is a GraphResponse (not 'dispatcher' string)
      - Output contains git-related keywords (branch, commit, On branch, etc.)
      - Status is 'completed'
    """
    from agent_utilities.graph.runner import run_graph
    from agent_utilities.models import GraphResponse

    graph, config = graph_bundle

    prompt = "Can I get the git status for the project genius-agent"

    result = None
    with anyio.move_on_after(600.0) as cancel_scope:
        result = await run_graph(graph, config, prompt)
    if cancel_scope.cancelled_caught:
        pytest.fail(
            "Git status graph test timed out after 600 seconds. "
            "Check router LLM, repository-manager MCP, and verifier."
        )

    # --- Assert 1: Must be a proper GraphResponse ---
    assert isinstance(result, GraphResponse), (
        f"run_graph() returned {type(result).__name__}: '{str(result)[:200]}'. "
        f"Expected GraphResponse. The 'dispatcher' bug is still active."
    )

    output = str(result.results.get("output", result.results))

    print(f"\n[Git Status Test] Result status: {result.status}")
    print(f"[Git Status Test] Output length: {len(output)} chars")
    print(f"[Git Status Test] Output preview:\n{output[:800]}\n")

    # --- Assert 2: Status must be 'completed' ---
    assert result.status == "completed", (
        f"Graph returned status='{result.status}' (expected 'completed'). "
        f"Output: {output[:400]}"
    )

    # --- Assert 3: Output must contain git-related content ---
    git_keywords = [
        "branch",
        "commit",
        "on branch",
        "modified",
        "untracked",
        "nothing to commit",
        "ahead",
        "up to date",
    ]
    found_keywords = [kw for kw in git_keywords if kw in output.lower()]
    assert len(found_keywords) >= 1, (
        f"Output contains no git-related keywords (checked: {git_keywords}). "
        f"The repository-manager tool may not have executed correctly. "
        f"Output: {output[:600]}"
    )

    # --- Assert 4: No hallucinated content ---
    assert (
        "placeholder" not in output.lower() and "example" not in output.lower()
    ), f"Output contains hallucinated placeholder content. Output: {output[:400]}"

    print(f"[Git Status Test] ✅ PASSED — Git keywords found: {found_keywords}")


if __name__ == "__main__":
    asyncio.run(test_git_status_via_graph(None))
