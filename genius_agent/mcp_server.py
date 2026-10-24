#!/usr/bin/python
"""Governed MCP surface for Genius Agent search ingestion."""

from __future__ import annotations

import logging
from typing import Annotated, Any

from agent_connector_sdk.connector_hooks import RegistrationContext
from pydantic import Field

from genius_agent.kg_ingest import genius_ingest_search as _genius_ingest_search

logger = logging.getLogger(__name__)


async def genius_ingest_search(
    query: Annotated[
        str,
        Field(
            min_length=1,
            max_length=2048,
            description="Focused web-search query whose ranked results will be ingested.",
        ),
    ],
    max_results: Annotated[
        int,
        Field(
            ge=1,
            le=50,
            description="Maximum ranked search results to retrieve and ingest.",
        ),
    ] = 10,
) -> dict[str, Any] | None:
    """Search the web and idempotently ingest the ranked evidence into the graph."""

    normalized_query = query.strip()
    if not normalized_query:
        raise ValueError("query must contain non-whitespace text")
    if not 1 <= max_results <= 50:
        raise ValueError("max_results must be between 1 and 50")
    return await _genius_ingest_search(normalized_query, max_results=max_results)


def register_tools(context: RegistrationContext) -> None:
    """Register the canonical, signed Genius source tool."""
    mcp = context.server

    mcp.tool(
        name="genius_ingest_search",
        annotations={
            "title": "Search and ingest web evidence",
            "readOnlyHint": False,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": True,
        },
        tags={"search", "ingest", "knowledge-graph"},
        run_in_thread=True,
    )(genius_ingest_search)
