import asyncio
import sys

# Add project roots to sys.path
sys.path.append("/home/genius/Workspace/agent-packages/agent-utilities")
sys.path.append("/home/genius/Workspace/agent-packages/agents/genius-agent")
sys.path.append("/home/genius/Workspace/agent-packages/agents/portainer-agent")

from genius_agent.agent_server import agent_template
from agent_utilities.agent_utilities import run_graph


async def main():
    print("🚀 Initializing Genius Agent Master Graph...")
    graph, config = agent_template()

    # Ensure validation is disabled for this test as well
    config["enable_llm_validation"] = False

    print("📡 Querying Portainer for running stacks...")
    result = await run_graph(graph, config, "List the running stacks in Portainer")

    print("\n--- TEST RESULT ---")
    res_data = result.get("results", {})
    # In my orchestrator, the results are keyed by domain
    if isinstance(res_data, dict) and "portainer" in res_data:
        print(res_data["portainer"])
    else:
        print(res_data)
    print("-------------------")


if __name__ == "__main__":
    asyncio.run(main())
