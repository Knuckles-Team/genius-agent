#!/usr/bin/python
"""Governed MCP surface for Genius Agent search ingestion."""

from __future__ import annotations

import logging
import sys
from typing import Annotated, Any

from agent_utilities.core.config import load_config
from agent_utilities.mcp.server_factory import create_mcp_server
from fastmcp import FastMCP
from pydantic import Field

from genius_agent.agent_server import __version__
from genius_agent.kg_ingest import genius_ingest_search as _genius_ingest_search

logger = logging.getLogger(__name__)


def genius_ingest_search(
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
    return _genius_ingest_search(normalized_query, max_results=max_results)


def register_tools(mcp: FastMCP) -> None:
    """Register the canonical, signed Genius source tool."""

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


def get_mcp_instance() -> tuple[Any, Any, Any]:
    """Build the Genius MCP instance without starting a transport."""

    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="Genius Agent",
        version=__version__,
        instructions=(
            "Search the web and materialize ranked evidence into epistemic-graph. "
            "Runtime endpoints, credentials, TLS trust, and graph policy come from "
            "AgentConfig; no deployment values are packaged."
        ),
    )
    register_tools(mcp)
    for middleware in middlewares:
        mcp.add_middleware(middleware)
    return mcp, args, middlewares


def mcp_server() -> None:
    """Run the configured Genius MCP transport."""

    mcp, args, _ = get_mcp_instance()
    print(f"Genius Agent MCP v{__version__}", file=sys.stderr)
    print(f"Transport: {args.transport.upper()}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport configuration")
        raise SystemExit(1)


if __name__ == "__main__":
    mcp_server()
