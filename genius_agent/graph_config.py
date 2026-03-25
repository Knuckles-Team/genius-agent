"""Genius Master Graph configuration — dynamic discovery of sub-agents.

This file enables the master orchestrator to follow the same graph_config pattern
as leaf agents, but with dynamic discovery of its "domains" (which are sub-agents).
"""

from genius_agent.master_graph import discover_agents
from genius_agent.skill_agent_config import SKILL_AGENTS
from agent_utilities import build_tag_env_map


def get_dynamic_config():
    """Generates the graph configuration by discovering available sub-agents and specialized skill agents.

    Returns:
        tuple: (tag_prompts, tag_env_vars, sub_agents)
    """
    agents = discover_agents()  # {tag: package_name}

    # Tag -> Prompt mapping (used by RouterNode to understand where to route)
    # We use the package name as a placeholder description for now,
    # but we could improve this by extracting descriptions from IDENTITY.md or metadata.
    tag_prompts = {
        name: f"Specialized agent for {package_name}"
        for name, package_name in agents.items()
    }

    # Add specialized skill agents
    for name, config in SKILL_AGENTS.items():
        if name not in tag_prompts:
            tag_prompts[name] = config["description"]

    # Tag -> Env Var mapping (following standard convention)
    tag_env_vars = build_tag_env_map(list(tag_prompts.keys()))

    # Tag -> Sub-Agent mapping (directing DomainNode to delegate to the agent package or skill agent)
    sub_agents = {name: package_name for name, package_name in agents.items()}
    # Add skill agents to sub_agents mapping
    for name in SKILL_AGENTS.keys():
        if name not in sub_agents:
            sub_agents[name] = name  # Skill agents use their own name as the target

    return tag_prompts, tag_env_vars, sub_agents
