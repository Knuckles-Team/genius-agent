import asyncio
from pydantic_ai.mcp import MCPServerStdio
import logging
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def debug_mcp():
    server = MCPServerStdio(
        command="portainer-mcp", args=["--transport", "stdio"], id="portainer-mcp"
    )

    logger.info("Attempting to connect to portainer-mcp...")
    try:
        async with server as session:
            logger.info("Connected! Listing tools...")
            tools = await session.list_tools()
            logger.info(f"Success! Found {len(tools)} tools.")
    except Exception as e:
        logger.error(f"Failed with {type(e).__name__}: {e}")
        if hasattr(e, "exceptions"):
            for i, inner in enumerate(e.exceptions):
                logger.error(f"Inner Exception {i}: {type(inner).__name__}: {inner}")
                traceback.print_exception(type(inner), inner, inner.__traceback__)
        else:
            traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(debug_mcp())
