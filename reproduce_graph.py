import asyncio
import os
import logging
import sys

sys.path.append(os.getcwd())


os.chdir(os.path.dirname(os.path.abspath(__file__)))

from agent_utilities.base_utilities import load_env_vars
from agent_utilities import create_master_graph, run_graph

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("reproduce_graph")


async def main():

    load_env_vars(".env")

    os.environ["DEBUG"] = "True"

    prompt = "List the running stacks in Portainer."

    print(f"\n🚀 Reproducing Graph Execution for prompt: '{prompt}'")
    print("-" * 50)

    try:

        print("Initializing Master Graph (Discovering Agents)...")
        graph_bundle = create_master_graph(
            name="Manual Test Master Graph",
        )
        graph, config = graph_bundle
        print(f"Graph initialized with {len(config.get('tag_prompts', {}))} domains.")

        print("\nExecuting graph.run()...")

        eq = asyncio.Queue()

        async def event_consumer():
            while True:
                event = await eq.get()
                if event is None:
                    break
                logger.info(f"📡 Graph Event: {event}")

        consumer_task = asyncio.create_task(event_consumer())

        result = await asyncio.wait_for(
            run_graph(graph, config, prompt, eq=eq), timeout=120
        )

        await eq.put(None)
        await consumer_task

        print("\n✅ Execution Complete!")
        print("-" * 50)
        print(f"Results: {result.get('results')}")

    except asyncio.TimeoutError:
        print("\n❌ FAILED: Graph execution timed out after 120 seconds.")
    except Exception as e:
        logger.exception(f"\n❌ FAILED: Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
