[Skip to main content](https://gofastmcp.com/clients/client#content-area)
Join us at the inaugural PyAI Conf in San Francisco on March 10th! [Learn More](https://pyai.events?utm_source=gofastmcp)
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
  * [](https://discord.gg/uu8dJCgttd)
  * [](https://prefect.io/horizon)
  * [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")
  * [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")


Search...
Navigation
Clients
The FastMCP Client
Search the docs...
⌘K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/getting-started/welcome)
  * [Installation](https://gofastmcp.com/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/getting-started/quickstart)
  * UpgradeNEW


##### Servers
  * [Overview](https://gofastmcp.com/servers/server)
  * Core Components
  * FeaturesNEW
  * ProvidersNEW
  * TransformsNEW
  * Authentication
  * [ Authorization NEW ](https://gofastmcp.com/servers/authorization)
  * Deployment


##### Apps
  * [ Overview NEW ](https://gofastmcp.com/apps/overview)
  * [ Low-Level API NEW ](https://gofastmcp.com/apps/low-level)


##### Clients
  * [Overview](https://gofastmcp.com/clients/client)
  * [Transports](https://gofastmcp.com/clients/transports)
  * CLINEW
  * Core Operations
  * Handlers
  * AuthenticationNEW


##### Integrations
  * Auth
  * Web Frameworks
  * AI Assistants
  * AI SDKs


##### Development
  * [Contributing](https://gofastmcp.com/development/contributing)
  * [Tests](https://gofastmcp.com/development/tests)
  * [Releases](https://gofastmcp.com/development/releases)
  * [ Updates NEW ](https://gofastmcp.com/updates)
  * [ Changelog NEW ](https://gofastmcp.com/changelog)
  * [Contrib Modules](https://gofastmcp.com/patterns/contrib)


On this page
  * [Creating a Client](https://gofastmcp.com/clients/client#creating-a-client)
  * [Choosing a Transport](https://gofastmcp.com/clients/client#choosing-a-transport)
  * [Configuration-Based Clients](https://gofastmcp.com/clients/client#configuration-based-clients)
  * [Connection Lifecycle](https://gofastmcp.com/clients/client#connection-lifecycle)
  * [Operations](https://gofastmcp.com/clients/client#operations)
  * [Callback Handlers](https://gofastmcp.com/clients/client#callback-handlers)


Clients
# The FastMCP Client
Copy page
Programmatic client for interacting with MCP servers through a well-typed, Pythonic interface.
Copy page
`2.0.0` The `fastmcp.Client` class provides a programmatic interface for interacting with any MCP server. It handles protocol details and connection management automatically, letting you focus on the operations you want to perform. The FastMCP Client is designed for deterministic, controlled interactions rather than autonomous behavior, making it ideal for testing MCP servers during development, building deterministic applications that need reliable MCP interactions, and creating the foundation for agentic or LLM-based clients with structured, type-safe operations.
This is a programmatic client that requires explicit function calls and provides direct control over all MCP operations. Use it as a building block for higher-level systems.
##
[​](https://gofastmcp.com/clients/client#creating-a-client)
Creating a Client
You provide a server source and the client automatically infers the appropriate transport mechanism.
Copy
```
import asyncio
from fastmcp import Client, FastMCP

# In-memory server (ideal for testing)
server = FastMCP("TestServer")
client = Client(server)

# HTTP server
client = Client("https://example.com/mcp")

# Local Python script
client = Client("my_mcp_server.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Execute operations
        result = await client.call_tool("example_tool", {"param": "value"})
        print(result)

asyncio.run(main())

```

All client operations require using the `async with` context manager for proper connection lifecycle management.
##
[​](https://gofastmcp.com/clients/client#choosing-a-transport)
Choosing a Transport
The client automatically selects a transport based on what you pass to it, but different transports have different characteristics that matter for your use case. **In-memory transport** connects directly to a FastMCP server instance within the same Python process. Use this for testing and development where you want to eliminate subprocess and network complexity. The server shares your process’s environment and memory space.
Copy
```
from fastmcp import Client, FastMCP

server = FastMCP("TestServer")
client = Client(server)  # In-memory, no network or subprocess

```

**STDIO transport** launches a server as a subprocess and communicates through stdin/stdout pipes. This is the standard mechanism used by desktop clients like Claude Desktop. The subprocess runs in an isolated environment, so you must explicitly pass any environment variables the server needs.
Copy
```
from fastmcp import Client

# Simple inference from file path
client = Client("my_server.py")

# With explicit environment configuration
client = Client("my_server.py", env={"API_KEY": "secret"})

```

**HTTP transport** connects to servers running as web services. Use this for production deployments where the server runs independently and manages its own lifecycle.
Copy
```
from fastmcp import Client

client = Client("https://api.example.com/mcp")

```

See [Transports](https://gofastmcp.com/clients/transports) for detailed configuration options including authentication headers, session persistence, and multi-server configurations.
##
[​](https://gofastmcp.com/clients/client#configuration-based-clients)
Configuration-Based Clients
`2.4.0` Create clients from MCP configuration dictionaries, which can include multiple servers. While there is no official standard for MCP configuration format, FastMCP follows established conventions used by tools like Claude Desktop.
Copy
```
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather-api.example.com/mcp"
        },
        "assistant": {
            "command": "python",
            "args": ["./assistant_server.py"]
        }
    }
}

client = Client(config)

async with client:
    # Tools are prefixed with server names
    weather_data = await client.call_tool("weather_get_forecast", {"city": "London"})
    response = await client.call_tool("assistant_answer_question", {"question": "What's the capital of France?"})

    # Resources use prefixed URIs
    icons = await client.read_resource("weather://weather/icons/sunny")

```

##
[​](https://gofastmcp.com/clients/client#connection-lifecycle)
Connection Lifecycle
The client uses context managers for connection management. When you enter the context, the client establishes a connection and performs an MCP initialization handshake with the server. This handshake exchanges capabilities, server metadata, and instructions.
Copy
```
from fastmcp import Client, FastMCP

mcp = FastMCP(name="MyServer", instructions="Use the greet tool to say hello!")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

async with Client(mcp) as client:
    # Initialization already happened automatically
    print(f"Server: {client.initialize_result.serverInfo.name}")
    print(f"Instructions: {client.initialize_result.instructions}")
    print(f"Capabilities: {client.initialize_result.capabilities.tools}")

```

For advanced scenarios where you need precise control over when initialization happens, disable automatic initialization and call `initialize()` manually:
Copy
```
from fastmcp import Client

client = Client("my_mcp_server.py", auto_initialize=False)

async with client:
    # Connection established, but not initialized yet
    print(f"Connected: {client.is_connected()}")
    print(f"Initialized: {client.initialize_result is not None}")  # False

    # Initialize manually with custom timeout
    result = await client.initialize(timeout=10.0)
    print(f"Server: {result.serverInfo.name}")

    # Now ready for operations
    tools = await client.list_tools()

```

##
[​](https://gofastmcp.com/clients/client#operations)
Operations
FastMCP clients interact with three types of server components. **Tools** are server-side functions that the client can execute with arguments. Call them with `call_tool()` and receive structured results.
Copy
```
async with client:
    tools = await client.list_tools()
    result = await client.call_tool("multiply", {"a": 5, "b": 3})
    print(result.data)  # 15

```

See [Tools](https://gofastmcp.com/clients/tools) for detailed documentation including version selection, error handling, and structured output. **Resources** are data sources that the client can read, either static or templated. Access them with `read_resource()` using URIs.
Copy
```
async with client:
    resources = await client.list_resources()
    content = await client.read_resource("file:///config/settings.json")
    print(content[0].text)

```

See [Resources](https://gofastmcp.com/clients/resources) for detailed documentation including templates and binary content. **Prompts** are reusable message templates that can accept arguments. Retrieve rendered prompts with `get_prompt()`.
Copy
```
async with client:
    prompts = await client.list_prompts()
    messages = await client.get_prompt("analyze_data", {"data": [1, 2, 3]})
    print(messages.messages)

```

See [Prompts](https://gofastmcp.com/clients/prompts) for detailed documentation including argument serialization.
##
[​](https://gofastmcp.com/clients/client#callback-handlers)
Callback Handlers
The client supports callback handlers for advanced server interactions. These let you respond to server-initiated requests and receive notifications.
Copy
```
from fastmcp import Client
from fastmcp.client.logging import LogMessage

async def log_handler(message: LogMessage):
    print(f"Server log: {message.data}")

async def progress_handler(progress: float, total: float | None, message: str | None):
    print(f"Progress: {progress}/{total} - {message}")

async def sampling_handler(messages, params, context):
    # Integrate with your LLM service here
    return "Generated response"

client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
    progress_handler=progress_handler,
    sampling_handler=sampling_handler,
    timeout=30.0
)

```

Each handler type has its own documentation:
  * **[Sampling](https://gofastmcp.com/clients/sampling)** - Respond to server LLM requests
  * **[Elicitation](https://gofastmcp.com/clients/elicitation)** - Handle server requests for user input
  * **[Progress](https://gofastmcp.com/clients/progress)** - Monitor long-running operations
  * **[Logging](https://gofastmcp.com/clients/logging)** - Handle server log messages
  * **[Roots](https://gofastmcp.com/clients/roots)** - Provide local context to servers


The FastMCP Client is designed as a foundational tool. Use it directly for deterministic operations, or build higher-level agentic systems on top of its reliable, type-safe interface.
[ Low-Level API Previous ](https://gofastmcp.com/apps/low-level)[ Client Transports Next ](https://gofastmcp.com/clients/transports)
[discord](https://discord.gg/uu8dJCgttd)[github](https://github.com/PrefectHQ/fastmcp)[website](https://www.prefect.io)[x](https://x.com/fastmcp)
[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=fastmcp)
