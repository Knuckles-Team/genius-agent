[Skip to main content](https://gofastmcp.com/apps/overview#content-area)
Join us at the inaugural PyAI Conf in San Francisco on March 10th! [Learn More](https://pyai.events?utm_source=gofastmcp)
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
  * [](https://discord.gg/uu8dJCgttd)
  * [](https://prefect.io/horizon)
  * [ PrefectHQ/fastmcp 23,195 ](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")
  * [ PrefectHQ/fastmcp 23,195 ](https://github.com/PrefectHQ/fastmcp "PrefectHQ/fastmcp")


Search...
Navigation
Apps
Apps
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
  * [What’s Available Today](https://gofastmcp.com/apps/overview#what%E2%80%99s-available-today)
  * [What’s Coming in 3.1](https://gofastmcp.com/apps/overview#what%E2%80%99s-coming-in-3-1)


Apps
# Apps
Copy page
Give your tools interactive UIs rendered directly in the conversation.
Copy page
`3.0.0` MCP Apps let your tools return interactive UIs — rendered in a sandboxed iframe right inside the host client’s conversation. Instead of returning plain text or JSON, a tool can show a chart, a form, an image viewer, or anything you can build with HTML and JavaScript. FastMCP implements the [MCP Apps extension](https://modelcontextprotocol.io/docs/extensions/apps), so you can start building apps today. FastMCP 3.1 will introduce a full Python-native app framework that makes building rich UIs dramatically simpler — no HTML or JavaScript required.
##
[​](https://gofastmcp.com/apps/overview#what%E2%80%99s-available-today)
What’s Available Today
FastMCP provides typed models and helpers for working with the MCP Apps extension directly:
  * **`AppConfig`**to link tools to UI resources and control visibility
  * **`ui://`resources** that automatically serve HTML with the correct MIME type
  * **`ResourceCSP`**and**`ResourcePermissions`**for security and sandboxing

This is the [low-level API](https://gofastmcp.com/apps/low-level) — you write the HTML yourself and wire up communication with the host via the `@modelcontextprotocol/ext-apps` JavaScript SDK. It gives you full control over the UI.
##
[​](https://gofastmcp.com/apps/overview#what%E2%80%99s-coming-in-3-1)
What’s Coming in 3.1
FastMCP 3.1 will ship a Python-native app framework that lets you build interactive UIs entirely in Python. Define layouts, handle events, and manage state without writing any HTML or JavaScript — FastMCP generates the app for you. Stay tuned. In the meantime, the [low-level API](https://gofastmcp.com/apps/low-level) is ready to use.
[ Testing your FastMCP Server Previous ](https://gofastmcp.com/patterns/testing)[ Low-Level API Next ](https://gofastmcp.com/apps/low-level)
Ctrl+I
[discord](https://discord.gg/uu8dJCgttd)[github](https://github.com/PrefectHQ/fastmcp)[website](https://www.prefect.io)[x](https://x.com/fastmcp)
[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=fastmcp)
