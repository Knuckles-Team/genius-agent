import asyncio
import logging
import sys
from genius_agent.master_graph import execute_master_graph

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


async def main():
    print("Starting master graph execution...")
    try:
        res = await execute_master_graph(
            "Can you get me the project details of gitlab project id 171?"
        )
        print(f"RESULT: {res}")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    asyncio.run(main())
