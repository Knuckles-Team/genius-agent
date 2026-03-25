import os
import importlib
import logging
from dataclasses import dataclass, field
from typing import Any
from genius_agent.skill_agent_config import SKILL_AGENTS

from pydantic import BaseModel, Field

try:
    from pydantic_graph import BaseNode, End, Graph, GraphRunContext
    from pydantic_graph.persistence.file import FileStatePersistence

    _PYDANTIC_GRAPH_AVAILABLE = True
except ImportError:
    _PYDANTIC_GRAPH_AVAILABLE = False

from agent_utilities import create_model

logger = logging.getLogger(__name__)

# Defaults matching agent-utilities
DEFAULT_ROUTER_MODEL = os.getenv("GRAPH_ROUTER_MODEL", os.getenv("MODEL_ID"))
DEFAULT_ROUTER_PROVIDER = os.getenv(
    "GRAPH_ROUTER_PROVIDER", os.getenv("PROVIDER", "openai")
)
DEFAULT_ROUTER_BASE_URL = os.getenv("GRAPH_ROUTER_BASE_URL", os.getenv("LLM_BASE_URL"))
DEFAULT_ROUTER_API_KEY = os.getenv("GRAPH_ROUTER_API_KEY", os.getenv("LLM_API_KEY"))


@dataclass
class MasterGraphState:
    query: str
    routed_agent: str = ""
    results: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class AgentChoice(BaseModel):
    """Structured output from the master router LLM."""

    agent_name: str = Field(description="The package name of the agent to route to")
    confidence: float = Field(ge=0, le=1, description="Routing confidence 0-1")
    reasoning: str = Field(description="Brief reasoning for the classification")


_MasterRouterNodeBase = (
    BaseNode[MasterGraphState, None, dict] if _PYDANTIC_GRAPH_AVAILABLE else object
)
_MasterAgentNodeBase = (
    BaseNode[MasterGraphState, None, dict] if _PYDANTIC_GRAPH_AVAILABLE else object
)


@dataclass
class MasterRouterNode(_MasterRouterNodeBase):
    agent_descriptions: dict[str, str] = field(default_factory=dict)
    router_model: str = DEFAULT_ROUTER_MODEL
    min_confidence: float = 0.6

    async def run(self, ctx) -> "MasterAgentNode | End[dict]":
        from pydantic_ai import Agent

        model_id = (
            self.router_model.split(":")[-1]
            if self.router_model and ":" in self.router_model
            else self.router_model
        )
        model = create_model(
            provider=DEFAULT_ROUTER_PROVIDER,
            model_id=model_id,
            base_url=DEFAULT_ROUTER_BASE_URL,
            api_key=DEFAULT_ROUTER_API_KEY,
        )

        valid_agents = list(self.agent_descriptions.keys())
        desc_str = "\n".join(
            [f"- {k}: {v}" for k, v in self.agent_descriptions.items()]
        )

        router_agent = Agent(
            model=model,
            output_type=AgentChoice,
            instructions=(
                "You are the Genius Agent Master Orchestrator. Route the user query to "
                "the most appropriate specialized agent package.\n\n"
                f"Available Agents:\n{desc_str}\n\n"
                f"Classify into exactly ONE of these domains: {', '.join(valid_agents)}.\n"
                "Return the exact agent package name, a confidence score (0-1), and brief reasoning.\n"
                "If multiple agents apply, pick the PRIMARY one."
            ),
        )

        try:
            result = await router_agent.run(ctx.state.query)
            choice = result.output
        except Exception as e:
            logger.error(f"Master Router failed: {e}")
            from pydantic_graph import End

            return End(
                {"error": f"Master Router failed: {e}", "agent": "", "results": {}}
            )

        from pydantic_graph import End

        if choice.agent_name not in valid_agents:
            logger.warning(
                f"Router returned invalid agent '{choice.agent_name}', valid: {valid_agents}"
            )
            return End(
                {
                    "error": f"Invalid agent route: {choice.agent_name}",
                    "reasoning": choice.reasoning,
                    "agent": "",
                    "results": {},
                }
            )

        if choice.confidence < self.min_confidence:
            logger.warning(
                f"Low confidence {choice.confidence} for agent '{choice.agent_name}'"
            )
            return End(
                {
                    "error": "low_confidence",
                    "agent": choice.agent_name,
                    "confidence": choice.confidence,
                    "reasoning": choice.reasoning,
                    "results": {},
                }
            )

        logger.info(
            f"Routed to Agent '{choice.agent_name}' (conf={choice.confidence:.2f}): {choice.reasoning}"
        )
        ctx.state.routed_agent = choice.agent_name
        return MasterAgentNode(agent_descriptions=self.agent_descriptions)


@dataclass
class MasterAgentNode(_MasterAgentNodeBase):
    agent_descriptions: dict[str, str] = field(default_factory=dict)

    async def run(self, ctx) -> "End[dict]":
        from pydantic_graph import End
        from agent_utilities import run_graph, create_agent

        agent_pkg = ctx.state.routed_agent
        logger.info(f"MasterAgentNode executing delegate agent '{agent_pkg}'")

        try:
            if agent_pkg in SKILL_AGENTS:
                # Handle specialized skill agents
                config = SKILL_AGENTS[agent_pkg]
                tags = config["tags"]

                # Create a specialized agent instance with tools filtered by the agent's tags
                target = create_agent(
                    name=agent_pkg,
                    system_prompt=config["description"],
                    enable_skills=True,
                    load_universal_skills=True,
                    load_skill_graphs=True,
                    skill_tags=tags,
                )

                res = await target.run(ctx.state.query)
                output = getattr(res, "output", None) or getattr(res, "data", res)
                ctx.state.results[agent_pkg] = str(output)

            else:
                # Dynamically import the chosen agent's agent_server.py and call agent_template()
                module = importlib.import_module(f"{agent_pkg}.agent_server")
                if not hasattr(module, "agent_template"):
                    raise AttributeError(
                        f"Package {agent_pkg} is missing agent_template()"
                    )

                target = module.agent_template()

                # Check if it's a GraphAgent (tuple) or FlatAgent (pydantic_ai.Agent)
                if isinstance(target, tuple) and len(target) == 2:
                    # Graph agent
                    sub_graph, config = target
                    logger.info(f"Delegating to Sub-Graph Orchestrator for {agent_pkg}")
                    # Use run_graph from agent_utilities
                    res = await run_graph(
                        graph=sub_graph, config=config, query=ctx.state.query
                    )
                    output = res.get("results") or res.get("error")
                else:
                    # Flat agent
                    logger.info(f"Delegating to Flat Agent for {agent_pkg}")
                    res = await target.run(ctx.state.query)
                    output = getattr(res, "output", None) or getattr(res, "data", res)

                ctx.state.results[agent_pkg] = str(output)

            logger.info(f"MasterAgentNode completed for '{agent_pkg}'")

        except Exception as e:
            import traceback

            tb = traceback.format_exc()
            logger.error(f"MasterAgentNode error for '{agent_pkg}': {e}\n{tb}")
            ctx.state.error = str(e)

        return End(
            {
                "agent": agent_pkg,
                "results": ctx.state.results,
                "error": ctx.state.error,
            }
        )


def discover_agents() -> dict[str, str]:
    """Discovers available agent packages using installed package metadata."""
    import importlib.metadata
    import importlib.util
    import warnings

    agent_descriptions = {}
    processed_packages = set()

    # Keywords to identify agent-like packages
    keywords = ["agent", "api", "mcp", "manager", "transcriber", "downloader"]
    skip_packages = ["agent-utilities", "universal-skills", "genius-agent"]

    import importlib.metadata

    for dist in importlib.metadata.distributions():
        name = dist.metadata["Name"]
        if name in processed_packages or any(s in name.lower() for s in skip_packages):
            continue
        processed_packages.add(name)

        if any(keyword in name.lower() for keyword in keywords):
            package_name = name.replace("-", "_")
            try:
                # Check for agent_server module without full import first
                spec = importlib.util.find_spec(f"{package_name}.agent_server")
                if spec:
                    logger.debug(
                        f"Master Graph: Checking package {name} ({package_name})..."
                    )
                    # Suppress warnings during discovery import
                    with warnings.catch_warnings():
                        warnings.filterwarnings("ignore", category=DeprecationWarning)
                        module = importlib.import_module(f"{package_name}.agent_server")

                    if hasattr(module, "agent_template"):
                        summary = dist.metadata.get("Summary")
                        desc = (
                            summary
                            if summary
                            else f"Specialized AI agent for {package_name}"
                        )
                        # Build a tag (e.g. 'gitlab-api' -> 'gitlab')
                        tag = name.replace("-agent", "").replace("-api", "").lower()
                        agent_descriptions[tag] = package_name
                        logger.info(
                            f"Master Graph: Discovered agent '{tag}' -> {package_name}"
                        )
            except (ImportError, Exception):
                # Silently skip if import fails
                pass

    logger.info(
        f"Master Graph discovered {len(agent_descriptions)} agents via metadata"
    )
    return agent_descriptions


def create_master_graph():
    """Build the master orchestration graph for genius-agent."""
    if not _PYDANTIC_GRAPH_AVAILABLE:
        raise ImportError(
            "pydantic-graph is required for Master Graph. Install agent-utilities[agent]."
        )

    agents_map = discover_agents()
    logger.info(
        f"Master Graph discovered {len(agents_map)} sub-agents: {list(agents_map.keys())}"
    )

    graph = Graph(
        nodes=(MasterRouterNode, MasterAgentNode),
        name="Genius Master Graph Orchestrator",
    )

    return graph, agents_map


async def execute_master_graph(query: str):
    """Executes a query through the master graph."""
    graph, agents_map = create_master_graph()

    start_node = MasterRouterNode(
        agent_descriptions=agents_map,
        router_model=DEFAULT_ROUTER_MODEL,
        min_confidence=0.5,
    )

    state = MasterGraphState(query=query)

    logger.info(f"Running master graph with {len(agents_map)} agents loaded.")
    result = await graph.run(start_node, state=state)

    output = result.output
    if isinstance(output, dict):
        return output
    return {"results": str(output)}
