[Skip to main content](https://gofastmcp.com/servers/server#content-area)
Join us at the inaugural PyAI Conf in San Francisco on March 10th! [Learn More](https://pyai.events?utm_source=gofastmcp)
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
  * [](https://discord.gg/uu8dJCgttd)
  * [](https://prefect.io/horizon)
  * [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")
  * [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")


Search...
Navigation
Servers
The FastMCP Server
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
  * [Creating a Server](https://gofastmcp.com/servers/server#creating-a-server)
  * [Components](https://gofastmcp.com/servers/server#components)
  * [Tools](https://gofastmcp.com/servers/server#tools)
  * [Resources](https://gofastmcp.com/servers/server#resources)
  * [Resource Templates](https://gofastmcp.com/servers/server#resource-templates)
  * [Prompts](https://gofastmcp.com/servers/server#prompts)
  * [Tag-Based Filtering](https://gofastmcp.com/servers/server#tag-based-filtering)
  * [Running the Server](https://gofastmcp.com/servers/server#running-the-server)
  * [Custom Routes](https://gofastmcp.com/servers/server#custom-routes)


Servers
# The FastMCP Server
Copy page
The core FastMCP server class for building MCP applications
Copy page
The `FastMCP` class is the central piece of every FastMCP application. It acts as the container for your tools, resources, and prompts, managing communication with MCP clients and orchestrating the entire server lifecycle.
##
[​](https://gofastmcp.com/servers/server#creating-a-server)
Creating a Server
Instantiate a server by providing a name that identifies it in client applications and logs. You can also provide instructions that help clients understand the server’s purpose.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP(name="MyAssistantServer")

# Instructions help clients understand how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)

```

The `FastMCP` constructor accepts several configuration options. The most commonly used parameters control server identity, authentication, and component behavior.
## FastMCP Constructor Parameters
[​](https://gofastmcp.com/servers/server#param-name)
name
str
default:"FastMCP"
A human-readable name for your server
[​](https://gofastmcp.com/servers/server#param-instructions)
instructions
str | None
Description of how to interact with this server. These instructions help clients understand the server’s purpose and available functionality
[​](https://gofastmcp.com/servers/server#param-version)
version
str | None
Version string for your server. If not provided, defaults to the FastMCP library version
[​](https://gofastmcp.com/servers/server#param-website-url)
website_url
str | None
`2.13.0`URL to a website with more information about your server. Displayed in client applications
[​](https://gofastmcp.com/servers/server#param-icons)
icons
list[Icon] | None
`2.13.0`List of icon representations for your server. Icons help users visually identify your server in client applications. See [Icons](https://gofastmcp.com/servers/icons) for detailed examples
[​](https://gofastmcp.com/servers/server#param-auth)
auth
OAuthProvider | TokenVerifier | None
Authentication provider for securing HTTP-based transports. See [Authentication](https://gofastmcp.com/servers/auth/authentication) for configuration options
[​](https://gofastmcp.com/servers/server#param-lifespan)
lifespan
Lifespan | AsyncContextManager | None
Server-level setup and teardown logic. See [Lifespans](https://gofastmcp.com/servers/lifespan) for composable lifespans
[​](https://gofastmcp.com/servers/server#param-tools)
tools
list[Tool | Callable] | None
A list of tools (or functions to convert to tools) to add to the server. In some cases, providing tools programmatically may be more convenient than using the `@mcp.tool` decorator
[​](https://gofastmcp.com/servers/server#param-include-tags)
include_tags
set[str] | None
Only expose components with at least one matching tag
[​](https://gofastmcp.com/servers/server#param-exclude-tags)
exclude_tags
set[str] | None
Hide components with any matching tag
[​](https://gofastmcp.com/servers/server#param-on-duplicate-tools)
on_duplicate_tools
Literal["error", "warn", "replace"]
default:"error"
How to handle duplicate tool registrations
[​](https://gofastmcp.com/servers/server#param-on-duplicate-resources)
on_duplicate_resources
Literal["error", "warn", "replace"]
default:"warn"
How to handle duplicate resource registrations
[​](https://gofastmcp.com/servers/server#param-on-duplicate-prompts)
on_duplicate_prompts
Literal["error", "warn", "replace"]
default:"replace"
How to handle duplicate prompt registrations
[​](https://gofastmcp.com/servers/server#param-strict-input-validation)
strict_input_validation
bool
default:"False"
`2.13.0`Controls how tool input parameters are validated. When `False` (default), FastMCP uses Pydantic’s flexible validation that coerces compatible inputs (e.g., `"10"` to `10` for int parameters). When `True`, uses the MCP SDK’s JSON Schema validation to validate inputs against the exact schema before passing them to your function, rejecting any type mismatches. The default mode improves compatibility with LLM clients while maintaining type safety. See [Input Validation Modes](https://gofastmcp.com/servers/tools#input-validation-modes) for details
[​](https://gofastmcp.com/servers/server#param-list-page-size)
list_page_size
int | None
default:"None"
`3.0.0`Maximum number of items per page for list operations (`tools/list`, `resources/list`, etc.). When `None` (default), all results are returned in a single response. When set, responses are paginated and include a `nextCursor` for fetching additional pages. See [Pagination](https://gofastmcp.com/servers/pagination) for details
##
[​](https://gofastmcp.com/servers/server#components)
Components
FastMCP servers expose three types of components to clients. Each type serves a distinct purpose in the MCP protocol.
###
[​](https://gofastmcp.com/servers/server#tools)
Tools
Tools are functions that clients can invoke to perform actions or access external systems. They’re the primary way clients interact with your server’s capabilities.
Copy
```
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

```

See [Tools](https://gofastmcp.com/servers/tools) for detailed documentation.
###
[​](https://gofastmcp.com/servers/server#resources)
Resources
Resources expose data that clients can read. Unlike tools, resources are passive data sources that clients pull from rather than invoke.
Copy
```
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}

```

See [Resources](https://gofastmcp.com/servers/resources) for detailed documentation.
###
[​](https://gofastmcp.com/servers/server#resource-templates)
Resource Templates
Resource templates are parameterized resources. The client provides values for template parameters in the URI, and the server returns data specific to those parameters.
Copy
```
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}

```

See [Resource Templates](https://gofastmcp.com/servers/resources#resource-templates) for detailed documentation.
###
[​](https://gofastmcp.com/servers/server#prompts)
Prompts
Prompts are reusable message templates that guide LLM interactions. They help establish consistent patterns for how clients should frame requests.
Copy
```
@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"

```

See [Prompts](https://gofastmcp.com/servers/prompts) for detailed documentation.
##
[​](https://gofastmcp.com/servers/server#tag-based-filtering)
Tag-Based Filtering
`2.8.0` Tags let you categorize components and selectively expose them based on configurable include/exclude sets. This is useful for creating different views of your server for different environments or user types. Components can be tagged when defined using the `tags` parameter. A component can have multiple tags, and filtering operates on tag membership.
Copy
```
@mcp.tool(tags={"public", "utility"})
def public_tool() -> str:
    return "This tool is public"

@mcp.tool(tags={"internal", "admin"})
def admin_tool() -> str:
    return "This tool is for admins only"

```

The filtering logic works as follows:
  * **Include tags** : If specified, only components with at least one matching tag are exposed
  * **Exclude tags** : Components with any matching tag are filtered out
  * **Precedence** : Exclude tags always take priority over include tags


To ensure a component is never exposed, you can set `enabled=False` on the component itself. See the component-specific documentation for details.
Configure tag-based filtering when creating your server.
Copy
```
# Only expose components tagged with "public"
mcp = FastMCP(include_tags={"public"})

# Hide components tagged as "internal" or "deprecated"
mcp = FastMCP(exclude_tags={"internal", "deprecated"})

# Combine both: show admin tools but hide deprecated ones
mcp = FastMCP(include_tags={"admin"}, exclude_tags={"deprecated"})

```

This filtering applies to all component types (tools, resources, resource templates, and prompts) and affects both listing and access.
##
[​](https://gofastmcp.com/servers/server#running-the-server)
Running the Server
FastMCP servers communicate with clients through transport mechanisms. Start your server by calling `mcp.run()`, typically within an `if __name__ == "__main__":` block. This pattern ensures compatibility with various MCP clients.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Defaults to STDIO transport
    mcp.run()

    # Or use HTTP transport
    # mcp.run(transport="http", host="127.0.0.1", port=9000)

```

FastMCP supports several transports:
  * **STDIO** (default): For local integrations and CLI tools
  * **HTTP** : For web services using the Streamable HTTP protocol
  * **SSE** : Legacy web transport (deprecated)

The server can also be run using the FastMCP CLI. For detailed information on transports and configuration, see the [Running Your Server](https://gofastmcp.com/deployment/running-server) guide.
##
[​](https://gofastmcp.com/servers/server#custom-routes)
Custom Routes
When running with HTTP transport, you can add custom web routes alongside your MCP endpoint using the `@custom_route` decorator. This is useful for auxiliary endpoints like health checks.
Copy
```
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

if __name__ == "__main__":
    mcp.run(transport="http")  # Health check at http://localhost:8000/health

```

Custom routes are served alongside your MCP endpoint and are useful for:
  * Health check endpoints for monitoring
  * Simple status or info endpoints
  * Basic webhooks or callbacks

For more complex web applications, consider [mounting your MCP server into a FastAPI or Starlette app](https://gofastmcp.com/deployment/http#integration-with-web-frameworks).
[ Upgrading from the MCP Low-Level SDK Previous ](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk)[ Tools Next ](https://gofastmcp.com/servers/tools)
[discord](https://discord.gg/uu8dJCgttd)[github](https://github.com/PrefectHQ/fastmcp)[website](https://www.prefect.io)[x](https://x.com/fastmcp)
[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=fastmcp)
