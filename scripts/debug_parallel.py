import asyncio
from pydantic_ai.mcp import MCPServerStdio
import logging
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def connect_one(i):
    server = MCPServerStdio(
        command="jellyfin-mcp", args=["--transport", "stdio"], id=f"jellyfin-mcp-{i}"
    )

    logger.info(f"[{i}] Attempting to connect...")
    try:
        async with server as session:
            logger.info(f"[{i}] Connected! Listing tools...")
            tools = await session.list_tools()
            logger.info(f"[{i}] Success! Found {len(tools)} tools.")
            return True
    except Exception as e:
        logger.error(f"[{i}] Failed with {type(e).__name__}: {e}")
        if hasattr(e, "exceptions"):
            for inner in e.exceptions:
                logger.error(f"  Inner: {type(inner).__name__}: {inner}")
                # Print the first traceback to see the point of failure
                traceback.print_exception(type(inner), inner, inner.__traceback__)
        return False


async def debug_parallel():
    # Attempt with semaphore of 2 to see if THAT fails
    semaphore = asyncio.Semaphore(2)

    async def limited_connect(i):
        async with semaphore:
            return await connect_one(i)

    tasks = [limited_connect(i) for i in range(4)]
    results = await asyncio.gather(*tasks)
    logger.info(
        f"Final results: {results.count(True)} success, {results.count(False)} failure"
    )


if __name__ == "__main__":
    asyncio.run(debug_parallel())
