import os
import pytest
import os
import asyncio
from dotenv import load_dotenv
from agent_utilities.graph_orchestration import (
    initialize_graph_from_workspace,
    run_graph,
)

# Load environment variables from .env
load_dotenv()


@pytest.mark.asyncio
async def test_portainer_stack_listing():
    """
    Integration test for the Portainer stack listing flow.
    Requires PORTAINER_URL and PORTAINER_TOKEN to be set in the environment.
    This test verifies that the graph orchestrator can correctly route the query
    to the 'portainer' domain expert and execute the stack listing tool.
    """
    # 1. Initialize the graph from the current workspace
    # This will load the MCP registry and define the domain experts
    mcp_path = os.environ.get("MCP_CONFIG") or "genius_agent/agent_data/mcp_config.json"
    graph, config = initialize_graph_from_workspace(mcp_config=mcp_path)

    # Check if we have the portainer domain registered
    assert (
        "portainer" in config["valid_domains"]
    ), "Portainer domain not found in graph registry"

    # 2. Define the execution query
    prompt = "list the running stacks in portainer"

    # 3. Run the graph flow
    # We use a large timeout for integration tests as specialized agents might take time
    try:
        result = await asyncio.wait_for(run_graph(graph, config, prompt), timeout=300.0)

        # 4. Assertions
        # The result should contain the output from the specialized domain agent
        output = str(result.results.get("output", result.results))
        # Hallucination Guard: Ensure generic mockups are not present
        assert (
            "webapp" not in output.lower()
        ), "hallucinated placeholder 'webapp' found in output"

        # Real Data Check: The user's environment has ~29 stacks.
        # Check for at least 3 known real stack names from the provided list
        real_stacks = [
            "jellyfin",
            "2fauth",
            "archivebox",
            "mealie",
            "uptime",
            "qbittorrent",
        ]
        found_stacks = [s for s in real_stacks if s in output.lower()]

        assert (
            len(found_stacks) >= 3
        ), f"Output did not contain enough real stack names (found {len(found_stacks)}: {found_stacks})"
        assert "running" in output.lower()

        print(f"Genius Agent Portainer Output: {output[:500]}...")

    except asyncio.TimeoutError:
        pytest.fail("Portainer flow integration test timed out after 300 seconds")
    except Exception as e:
        pytest.fail(f"Portainer flow integration test failed with error: {e}")


if __name__ == "__main__":
    asyncio.run(test_portainer_stack_listing())
