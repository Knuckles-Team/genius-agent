import asyncio
import logging
import sys
import traceback
from genius_agent.master_graph import execute_master_graph

logging.basicConfig(level=logging.ERROR, stream=sys.stdout)


async def main():
    print("Testing master graph directly...")
    try:
        # Provide any valid LLM base URL/key if required, or let it fail quickly finding the error.
        res = await execute_master_graph(
            "Can you get me the project details of gitlab project id 171?"
        )
        print(f"RESULT TYPE: {type(res)}")
        print(f"RESULT: {res}")
    except Exception as e:
        print(f"FATAL ERROR CAUGHT: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
