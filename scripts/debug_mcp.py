import asyncio
from pydantic_ai_mcp import MCPServer
from contextlib import AsyncExitStack


async def debug_mcp():
    server = MCPServer(command="portainer-mcp", args=["--transport", "stdio"])
    async with AsyncExitStack() as stack:
        print(f"Connecting to {server.command}...")
        try:
            await stack.enter_async_context(server)
            print(f"Connection established. Server ID: {getattr(server, 'id', 'N/A')}")
            # pydanticai-mcp 0.0.18+ uses .tools property
            tools = getattr(server, "tools", [])
            print(f"Tools count: {len(tools)}")
            for t in tools:
                print(f" - {t.name}")
        except Exception as e:
            print(f"Connection failed: {e}")


if __name__ == "__main__":
    asyncio.run(debug_mcp())
