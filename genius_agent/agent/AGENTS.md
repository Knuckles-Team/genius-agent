# AGENTS.md - Multi-Agent Registry

This registry tracks the peer agents and specialized workers that the **Genius Agent** can orchestrate.

## Orchestration Strategy
The Genius Agent acts as the **Coordinator**. It delegates domain-specific tasks to peers and sub-agents, then synthesizes the results.

## Registered Peers

| Name | Role | Capability | URL |
|------|------|------------|-----|
| SearchMaster | Web Search & Research | `web-search`, `web-crawler` | http://search-master.arpa/a2a/ |
| CodeArchitect | Code Review & Refactoring | `agent-builder`, `mcp-builder` | http://code-architect.arpa/a2a/ |

## Sub-Agents (Dynamic)
The Genius Agent can spawn dynamic sub-agents using the `agent-spawner` skill when isolated execution environments are required for high-risk or high-compute tasks.

*Add new rows manually or let the agent call `register_a2a_peer(...)`.*
