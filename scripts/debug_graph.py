import asyncio
from agent_utilities.graph.builder import initialize_graph_from_workspace
from agent_utilities.graph.runner import run_graph


async def main():
    print("Initializing...")
    graph, config = initialize_graph_from_workspace()
    print("Graph Initialized! Running...")
    res = await run_graph(
        graph, config, query="Show me the running stacks in portainer"
    )
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
