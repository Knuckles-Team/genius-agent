import sys
import logging
import warnings

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="fastmcp")


from agent_utilities import (
    build_system_prompt_from_workspace,
    create_agent_parser,
    create_graph_agent_server,
    initialize_workspace,
    load_identity,
)

__version__ = "2.13.55"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


initialize_workspace()
meta = load_identity()

from agent_utilities.config import (
    DEFAULT_AGENT_NAME as CFG_NAME,
    DEFAULT_AGENT_DESCRIPTION as CFG_DESC,
    DEFAULT_AGENT_SYSTEM_PROMPT as CFG_PROMPT,
)

DEFAULT_AGENT_NAME = CFG_NAME or meta["name"]
DEFAULT_AGENT_DESCRIPTION = CFG_DESC or meta["description"]
DEFAULT_AGENT_SYSTEM_PROMPT = (
    CFG_PROMPT or meta.get("content") or build_system_prompt_from_workspace()
)


def agent_template(mcp_url: str = None, mcp_config: str = None, **kwargs):
    from agent_utilities import create_master_graph

    return create_master_graph(
        name=f"{DEFAULT_AGENT_NAME} Master Graph",
        **kwargs,
    )


def agent_server():

    warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="fastmcp")

    print(f"{DEFAULT_AGENT_NAME} v{__version__}", file=sys.stderr)
    parser = create_agent_parser()

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    graph_bundle = agent_template(
        provider=args.provider,
        agent_model=args.model_id,
        base_url=args.base_url,
        api_key=args.api_key,
        custom_skills_directory=args.custom_skills_directory,
        debug=args.debug,
        ssl_verify=not args.insecure,
        current_host=args.host,
        current_port=args.port,
    )

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
