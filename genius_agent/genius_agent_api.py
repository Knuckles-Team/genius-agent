#!/usr/bin/env python
# coding: utf-8

from agent_constructs import Agents, AgentsConfig
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

class HealthResponse(BaseModel):
    status: str


agents_manager = Agents()
app = FastAPI()
Instrumentator().instrument(app).expose(app, include_in_schema=False)


@app.get("/api/agents/{name}")
async def get_agent_config_by_name(name: str) -> [AgentsConfig, dict]:
    agent_config = agents_manager.find_agent_config(name=name)
    if agent_config:
        return agent_config
    else:
        return {"error": "Object not found"}


@app.get("/api/health", response_model=HealthResponse)
async def get_health() -> HealthResponse:
    health_response = HealthResponse.model_validate({"status": "200 OK"})
    return health_response


@app.get("/api/agents", response_model=AgentsConfig)
async def get_agent_configs() -> AgentsConfig:
    return agents_manager.agents_config


@app.post("/api/agents/load")
async def post_load_agents_config(agents_config: AgentsConfig):
    agents_manager.load_config(payload=agents_config)


@app.post("/api/chat")
async def post_chat(prompt: dict):
    return StreamingResponse(agents_manager.chat(prompt=prompt['prompt']), media_type="text/plain")


@app.post("/api/prometheus/{port}")
async def deploy_exporter(port: [int, str] = 8999):
    from prometheus_collector import start_prometheus_server_background
    start_prometheus_server_background(port=port)
    return f"Prometheus Exporter Running on port: {port}"
