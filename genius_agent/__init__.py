#!/usr/bin/env python

"""
genius-agent

GeniusAgent Agent Server
"""

from scion_sdk.connector import Connector

from genius_agent.mcp_server import register_tools

connector = Connector(
    instructions="Search the web and materialize ranked evidence into epistemic-graph. Runtime endpoints, credentials, TLS trust, and graph policy come from AgentConfig; no deployment values are packaged.",
    extra_registrations=(register_tools,),
)
