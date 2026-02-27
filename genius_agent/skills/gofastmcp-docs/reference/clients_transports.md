[Skip to main content](https://gofastmcp.com/clients/transports#content-area)
Join us at the inaugural PyAI Conf in San Francisco on March 10th! [Learn More](https://pyai.events?utm_source=gofastmcp)
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
  * [](https://discord.gg/uu8dJCgttd)
  * [](https://prefect.io/horizon)
  * [ PrefectHQ/fastmcp 23,195 ](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")
  * [ PrefectHQ/fastmcp 23,195 ](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")


Search...
Navigation
Clients
Client Transports
Search the docs...
Ctrl K
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
  * [STDIO Transport](https://gofastmcp.com/clients/transports#stdio-transport)
  * [Environment Variables](https://gofastmcp.com/clients/transports#environment-variables)
  * [Session Persistence](https://gofastmcp.com/clients/transports#session-persistence)
  * [HTTP Transport](https://gofastmcp.com/clients/transports#http-transport)
  * [SSE Transport](https://gofastmcp.com/clients/transports#sse-transport)
  * [In-Memory Transport](https://gofastmcp.com/clients/transports#in-memory-transport)
  * [Multi-Server Configuration](https://gofastmcp.com/clients/transports#multi-server-configuration)
  * [Tool Transformations](https://gofastmcp.com/clients/transports#tool-transformations)


Clients
# Client Transports
Copy page
Configure how clients connect to and communicate with MCP servers.
Copy page
`2.0.0` Transports handle the underlying connection between your client and MCP servers. While the client can automatically select a transport based on what you pass to it, instantiating transports explicitly gives you full control over configuration.
##
[​](https://gofastmcp.com/clients/transports#stdio-transport)
STDIO Transport
STDIO transport communicates with MCP servers through subprocess pipes. When using STDIO, your client launches and manages the server process, controlling its lifecycle and environment.
STDIO servers run in isolated environments by default. They do not inherit your shell’s environment variables. You must explicitly pass any configuration the server needs.
Copy
```
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

transport = StdioTransport(
    command="python",
    args=["my_server.py", "--verbose"],
    env={"API_KEY": "secret", "LOG_LEVEL": "DEBUG"},
    cwd="/path/to/server"
)
client = Client(transport)

```

For convenience, the client can infer STDIO transport from file paths, though this limits configuration options:
Copy
```
from fastmcp import Client

client = Client("my_server.py")  # Limited - no configuration options

```

###
[​](https://gofastmcp.com/clients/transports#environment-variables)
Environment Variables
Since STDIO servers do not inherit your environment, you need strategies for passing configuration. **Selective forwarding** passes only the variables your server needs:
Copy
```
import os
from fastmcp.client.transports import StdioTransport

required_vars = ["API_KEY", "DATABASE_URL", "REDIS_HOST"]
env = {var: os.environ[var] for var in required_vars if var in os.environ}

transport = StdioTransport(command="python", args=["server.py"], env=env)
client = Client(transport)

```

**Loading from .env files** keeps configuration separate from code:
Copy
```
from dotenv import dotenv_values
from fastmcp.client.transports import StdioTransport

env = dotenv_values(".env")
transport = StdioTransport(command="python", args=["server.py"], env=env)
client = Client(transport)

```

###
[​](https://gofastmcp.com/clients/transports#session-persistence)
Session Persistence
STDIO transports maintain sessions across multiple client contexts by default (`keep_alive=True`). This reuses the same subprocess for multiple connections, improving performance.
Copy
```
from fastmcp.client.transports import StdioTransport

transport = StdioTransport(command="python", args=["server.py"])
client = Client(transport)

async def efficient_multiple_operations():
    async with client:
        await client.ping()

    async with client:  # Reuses the same subprocess
        await client.call_tool("process_data", {"file": "data.csv"})

```

For complete isolation between connections, disable session persistence:
Copy
```
transport = StdioTransport(command="python", args=["server.py"], keep_alive=False)

```

##
[​](https://gofastmcp.com/clients/transports#http-transport)
HTTP Transport
`2.3.0` HTTP transport connects to MCP servers running as web services. This is the recommended transport for production deployments.
Copy
```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    url="https://api.example.com/mcp",
    headers={
        "Authorization": "Bearer your-token-here",
        "X-Custom-Header": "value"
    }
)
client = Client(transport)

```

FastMCP also provides authentication helpers:
Copy
```
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

client = Client(
    "https://api.example.com/mcp",
    auth=BearerAuth("your-token-here")
)

```

###
[​](https://gofastmcp.com/clients/transports#sse-transport)
SSE Transport
Server-Sent Events transport is maintained for backward compatibility. Use Streamable HTTP for new deployments unless you have specific infrastructure requirements.
Copy
```
from fastmcp.client.transports import SSETransport

transport = SSETransport(
    url="https://api.example.com/sse",
    headers={"Authorization": "Bearer token"}
)
client = Client(transport)

```

##
[​](https://gofastmcp.com/clients/transports#in-memory-transport)
In-Memory Transport
In-memory transport connects directly to a FastMCP server instance within the same Python process. This eliminates both subprocess management and network overhead, making it ideal for testing.
Copy
```
from fastmcp import FastMCP, Client
import os

mcp = FastMCP("TestServer")

@mcp.tool
def greet(name: str) -> str:
    prefix = os.environ.get("GREETING_PREFIX", "Hello")
    return f"{prefix}, {name}!"

client = Client(mcp)

async with client:
    result = await client.call_tool("greet", {"name": "World"})

```

Unlike STDIO transports, in-memory servers share the same memory space and environment variables as your client code.
##
[​](https://gofastmcp.com/clients/transports#multi-server-configuration)
Multi-Server Configuration
`2.4.0` Connect to multiple servers defined in a configuration dictionary:
Copy
```
from fastmcp import Client

config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http"
        },
        "assistant": {
            "command": "python",
            "args": ["./assistant.py"],
            "env": {"LOG_LEVEL": "INFO"}
        }
    }
}

client = Client(config)

async with client:
    # Tools are namespaced by server
    weather = await client.call_tool("weather_get_forecast", {"city": "NYC"})
    answer = await client.call_tool("assistant_ask", {"question": "What?"})

```

###
[​](https://gofastmcp.com/clients/transports#tool-transformations)
Tool Transformations
FastMCP supports tool transformations within the configuration. You can change names, descriptions, tags, and arguments for tools from a server.
Copy
```
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http",
            "tools": {
                "weather_get_forecast": {
                    "name": "miami_weather",
                    "description": "Get the weather for Miami",
                    "arguments": {
                        "city": {
                            "default": "Miami",
                            "hide": True,
                        }
                    }
                }
            }
        }
    }
}

```

To filter tools by tag, use `include_tags` or `exclude_tags` at the server level:
Copy
```
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "include_tags": ["forecast"]  # Only tools with this tag
        }
    }
}

```

[ The FastMCP Client Previous ](https://gofastmcp.com/clients/client)[ Client CLI Next ](https://gofastmcp.com/clients/cli)
Ctrl+I
[discord](https://discord.gg/uu8dJCgttd)[github](https://github.com/PrefectHQ/fastmcp)[website](https://www.prefect.io)[x](https://x.com/fastmcp)
[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=fastmcp)
