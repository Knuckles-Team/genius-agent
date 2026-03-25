import sys
import os
import logging
import warnings

# Suppress RequestsDependencyWarning and FastMCP DeprecationWarnings
warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="fastmcp")


from agent_utilities import (
    build_system_prompt_from_workspace,
    create_agent_parser,
    create_graph_agent_server,
    initialize_workspace,
    load_identity,
)

__version__ = "2.13.48"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Load identity and system prompt from workspace
initialize_workspace()
meta = load_identity()
DEFAULT_AGENT_NAME = os.getenv("DEFAULT_AGENT_NAME", meta["name"])
DEFAULT_AGENT_DESCRIPTION = os.getenv("AGENT_DESCRIPTION", meta["description"])
DEFAULT_AGENT_SYSTEM_PROMPT = os.getenv(
    "AGENT_SYSTEM_PROMPT", meta.get("content") or build_system_prompt_from_workspace()
)


def agent_template(mcp_url: str = None, mcp_config: str = None, **kwargs):
    """Factory function returning the fully initialized graph for execution."""
    from agent_utilities import create_graph_agent
    from genius_agent.graph_config import get_dynamic_config

    tag_prompts, tag_env_vars, sub_agents = get_dynamic_config()

    # Pass through standard MCP configuration
    effective_mcp_url = mcp_url or os.getenv("MCP_URL")
    effective_mcp_config = mcp_config or os.getenv("MCP_CONFIG")
    mcp_toolsets = kwargs.get("mcp_toolsets", [])

    return create_graph_agent(
        mcp_url=effective_mcp_url,
        mcp_config=effective_mcp_config or "",
        mcp_toolsets=mcp_toolsets,
        name=f"{DEFAULT_AGENT_NAME} Master Graph",
        tag_prompts=tag_prompts,
        tag_env_vars=tag_env_vars,
        sub_agents=sub_agents,
        **kwargs,
    )


def agent_server():
    # Suppress RequestsDependencyWarning and FastMCP DeprecationWarnings
    warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="fastmcp")

    print(f"{DEFAULT_AGENT_NAME} v{__version__}", file=sys.stderr)
    print(f"{DEFAULT_AGENT_NAME} v{__version__}", file=sys.stderr)
    parser = create_agent_parser()

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    # Create graph and config using standardized template
    graph_bundle = agent_template(
        provider=args.provider,
        agent_model=args.model_id,
        base_url=args.base_url,
        api_key=args.api_key,
        custom_skills_directory=args.custom_skills_directory,
        debug=args.debug,
        ssl_verify=not args.insecure,
    )

    # Start server using the pre-built graph bundle
    create_graph_agent_server(
        graph_bundle=graph_bundle,
        host=args.host,
        port=args.port,
        enable_web_ui=args.web,
        enable_otel=args.otel,
        otel_endpoint=args.otel_endpoint,
        otel_headers=args.otel_headers,
        otel_public_key=args.otel_public_key,
        otel_secret_key=args.otel_secret_key,
        otel_protocol=args.otel_protocol,
        debug=args.debug,
    )


if __name__ == "__main__":
    agent_server()
