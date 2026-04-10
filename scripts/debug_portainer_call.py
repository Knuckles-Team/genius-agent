import asyncio
from pydantic_ai.mcp import MCPServerStdio
import logging
import traceback
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def debug_mcp_call():
    server = MCPServerStdio(
        command="portainer-mcp", args=["--transport", "stdio"], id="portainer-mcp"
    )

    logger.info("Attempting to connect to portainer-mcp...")
    try:
        async with server as session:
            logger.info("Connected! Calling get_stacks via direct_call_tool...")
            # Pydantic AI MCPServer.direct_call_tool(name, args, metadata=None)
            result = await session.direct_call_tool("get_stacks", args={})

            print("\nTOOL RESULT:")
            print(
                json.dumps(result, indent=2) if not isinstance(result, str) else result
            )

    except Exception as e:
        logger.error(f"Failed with {type(e).__name__}: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(debug_mcp_call())
