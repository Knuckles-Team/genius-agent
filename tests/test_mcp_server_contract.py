"""Current Genius MCP source-contract coverage."""

from __future__ import annotations

import sys

import pytest

from genius_agent import mcp_server


@pytest.mark.asyncio
async def test_factory_exposes_the_signed_source_tool(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["genius-mcp"])

    mcp, _args, _middlewares = mcp_server.get_mcp_instance()
    tools = await mcp.list_tools()
    matching = [tool for tool in tools if tool.name == "genius_ingest_search"]

    assert len(matching) == 1
    assert set(matching[0].parameters["properties"]) == {"query", "max_results"}
    assert matching[0].parameters["properties"]["max_results"]["maximum"] == 50


def test_source_tool_normalizes_and_delegates(monkeypatch):
    captured: dict[str, str | int] = {}

    def fake_ingest(query, *, max_results):
        captured.update(query=query, max_results=max_results)
        return {"provider": "synthetic", "results": 2, "ingested": None}

    monkeypatch.setattr(mcp_server, "_genius_ingest_search", fake_ingest)

    result = mcp_server.genius_ingest_search("  bounded query  ", max_results=2)

    assert captured == {"query": "bounded query", "max_results": 2}
    assert result == {"provider": "synthetic", "results": 2, "ingested": None}


@pytest.mark.parametrize(
    ("query", "max_results"),
    [("   ", 1), ("query", 0), ("query", 51)],
)
def test_source_tool_rejects_invalid_bounds(query, max_results):
    with pytest.raises(ValueError):
        mcp_server.genius_ingest_search(query, max_results=max_results)
