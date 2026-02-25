[Skip to main content](https://gofastmcp.com/getting-started/installation#content-area)
Join us at the inaugural PyAI Conf in San Francisco on March 10th! [Learn More](https://pyai.events?utm_source=gofastmcp)
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
  * [](https://discord.gg/uu8dJCgttd)
  * [](https://prefect.io/horizon)
  * [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")
  * [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")


Search...
Navigation
Get Started
Installation
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
  * [Install FastMCP](https://gofastmcp.com/getting-started/installation#install-fastmcp)
  * [Optional Dependencies](https://gofastmcp.com/getting-started/installation#optional-dependencies)
  * [Verify Installation](https://gofastmcp.com/getting-started/installation#verify-installation)
  * [Dependency Licensing](https://gofastmcp.com/getting-started/installation#dependency-licensing)
  * [Upgrading](https://gofastmcp.com/getting-started/installation#upgrading)
  * [From FastMCP 2.x](https://gofastmcp.com/getting-started/installation#from-fastmcp-2-x)
  * [From FastMCP 1.0 (in the Low-Level SDK)](https://gofastmcp.com/getting-started/installation#from-fastmcp-1-0-in-the-low-level-sdk)
  * [From the Low-Level Server API](https://gofastmcp.com/getting-started/installation#from-the-low-level-server-api)
  * [Versioning Policy](https://gofastmcp.com/getting-started/installation#versioning-policy)
  * [Looking Ahead: FastMCP 4.0](https://gofastmcp.com/getting-started/installation#looking-ahead-fastmcp-4-0)
  * [Contributing to FastMCP](https://gofastmcp.com/getting-started/installation#contributing-to-fastmcp)


Get Started
# Installation
Copy page
Install FastMCP and verify your setup
Copy page
##
[​](https://gofastmcp.com/getting-started/installation#install-fastmcp)
Install FastMCP
We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install and manage FastMCP.
Copy
```
pip install fastmcp

```

Or with uv:
Copy
```
uv add fastmcp

```

###
[​](https://gofastmcp.com/getting-started/installation#optional-dependencies)
Optional Dependencies
FastMCP provides optional extras for specific features. For example, to install the background tasks extra:
Copy
```
pip install "fastmcp[tasks]"

```

See [Background Tasks](https://gofastmcp.com/servers/tasks) for details on the task system.
###
[​](https://gofastmcp.com/getting-started/installation#verify-installation)
Verify Installation
To verify that FastMCP is installed correctly, you can run the following command:
Copy
```
fastmcp version

```

You should see output like the following:
Copy
```
$ fastmcp version

FastMCP version:                           3.0.0
MCP version:                               1.25.0
Python version:                            3.12.2
Platform:            macOS-15.3.1-arm64-arm-64bit
FastMCP root path:            ~/Developer/fastmcp

```

###
[​](https://gofastmcp.com/getting-started/installation#dependency-licensing)
Dependency Licensing
FastMCP depends on Cyclopts for CLI functionality. Cyclopts v4 includes docutils as a transitive dependency, which has complex licensing that may trigger compliance reviews in some organizations.If this is a concern, you can install Cyclopts v5 alpha which removes this dependency:
Copy
```
pip install "cyclopts>=5.0.0a1"

```

Alternatively, wait for the stable v5 release. See [this issue](https://github.com/BrianPugh/cyclopts/issues/672) for details.
##
[​](https://gofastmcp.com/getting-started/installation#upgrading)
Upgrading
###
[​](https://gofastmcp.com/getting-started/installation#from-fastmcp-2-x)
From FastMCP 2.x
See the [Upgrade Guide](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2) for a complete list of breaking changes and migration steps.
###
[​](https://gofastmcp.com/getting-started/installation#from-fastmcp-1-0-in-the-low-level-sdk)
From FastMCP 1.0 (in the Low-Level SDK)
If you’re using FastMCP 1.0 via the `mcp` package (`from mcp.server.fastmcp import FastMCP`), upgrading is straightforward — for most servers, it’s a single import change. See the [full upgrade guide](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk) for details.
###
[​](https://gofastmcp.com/getting-started/installation#from-the-low-level-server-api)
From the Low-Level Server API
If you built your server directly on the `mcp` package’s `Server` class — with `list_tools()`/`call_tool()` handlers and hand-written JSON Schema — see the [migration guide](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk) for a full walkthrough.
##
[​](https://gofastmcp.com/getting-started/installation#versioning-policy)
Versioning Policy
FastMCP follows semantic versioning with pragmatic adaptations for the rapidly evolving MCP ecosystem. Breaking changes may occur in minor versions (e.g., 2.3.x to 2.4.0) when necessary to stay current with the MCP Protocol. For production use, always pin to exact versions:
Copy
```
fastmcp==3.0.0  # Good
fastmcp>=3.0.0  # Bad - may install breaking changes

```

See the full [versioning and release policy](https://gofastmcp.com/development/releases#versioning-policy) for details on our public API, deprecation practices, and breaking change philosophy.
###
[​](https://gofastmcp.com/getting-started/installation#looking-ahead-fastmcp-4-0)
Looking Ahead: FastMCP 4.0
The MCP Python SDK v2 is expected in early 2026 and will include breaking changes. When released, FastMCP will incorporate these upstream changes in a new major version (FastMCP 4.0). To avoid unexpected breaking changes, we recommend pinning your dependency with an upper bound:
Copy
```
fastmcp>=3.0,<4

```

We’ll provide migration guidance when FastMCP 4.0 is released.
##
[​](https://gofastmcp.com/getting-started/installation#contributing-to-fastmcp)
Contributing to FastMCP
Interested in contributing to FastMCP? See the [Contributing Guide](https://gofastmcp.com/development/contributing) for details on:
  * Setting up your development environment
  * Running tests and pre-commit hooks
  * Submitting issues and pull requests
  * Code standards and review process


[ Welcome to FastMCP Previous ](https://gofastmcp.com/getting-started/welcome)[ Quickstart Next ](https://gofastmcp.com/getting-started/quickstart)
[discord](https://discord.gg/uu8dJCgttd)[github](https://github.com/PrefectHQ/fastmcp)[website](https://www.prefect.io)[x](https://x.com/fastmcp)
[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=fastmcp)
