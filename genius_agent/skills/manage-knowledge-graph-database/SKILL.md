---
name: knowledge-graph
description: Capabilities for managing a Knowledge Graph.
---

### Overview
This skill allows you to manage a Knowledge Graph. Use this for complex relationships, entity tracking, and temporal facts.

### Capabilities
- **add_episode**: Add information (text, JSON) to the graph. The system will automatically extract entities and relationships.
- **search_knowledge_base**: Search the graph for information.
- **search_nodes**: Search for specific nodes/entities.
- **search_facts**: Search for specific facts/edges.
- **get_entity_info**: Get detailed relationships for a specific entity.

### Common Tools
- `search_knowledge_base`: Primary tool for retrieving information from the graph.
- `add_episode`: Primary tool for ingesting new knowledge.

### Usage Rules
- Always search the knowledge graph (`search_knowledge_base`) when answering questions about entities that might be stored.
- When you learn new information from crawling or conversation, use `add_episode` to persist it.
