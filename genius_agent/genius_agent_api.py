#!/usr/bin/env python
# coding: utf-8
import uvicorn
from genius_agent.agent_construct import Agents, AgentsConfig
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Optional, Callable, Union
from prometheus_fastapi_instrumentator import Instrumentator

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=True)

# Set up CORS
origins = [
    "http://localhost:3000",  # your React front-end address
    "https://your.production.domain",  # if applicable
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agents_manager = Agents()
Instrumentator().instrument(app).expose(app, include_in_schema=False)

class HealthResponse(BaseModel):
    status: str


@app.get("/api/agents/{name}")
async def get_agent_config_by_name(name: str) -> AgentsConfig:
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
    for agent in agents_manager.agents_config.agents:
        if isinstance(agent.is_termination_msg, Callable):
            agent.is_termination_msg = str(agent.is_termination_msg)
    print("AGENTS_CONFIG: ", agents_manager.agents_config)
    return agents_manager.agents_config

@app.post("/api/agents/load")
async def post_load_agents_config(agents_config: AgentsConfig):
    agents_manager.load_config(payload=agents_config)


@app.post("/api/chat")
async def post_chat(prompt: dict):
    return StreamingResponse(agents_manager.chat(prompt=prompt['prompt']), media_type="text/plain")


@app.post("/api/prometheus/{port}")
async def deploy_exporter(port: str = "8999"):
    from prometheus_collector import start_prometheus_server_background
    start_prometheus_server_background(port=port)
    return f"Prometheus Exporter Running on port: {port}"


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)
    config = {}

    config['log_config'] = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s %(message)s",
                "use_colors": "None"
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": "%(levelprefix)s %(client_addr)s - \"%(request_line)s\" %(status_code)s"
            }
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr"
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout"
            }
        },
        "loggers": {
            "uvicorn": {
                "handlers": [
                    "default"
                ],
                "level": "INFO"
            },
            "uvicorn.error": {
                "level": "INFO",
                "handlers": [
                    "default"
                ],
                "propagate": True
            },
            "uvicorn.access": {
                "handlers": [
                    "access"
                ],
                "level": "INFO",
                "propagate": False
            }
        }
    }

    # add your handler to it (in my case, I'm working with quart, but you can do this with Flask etc. as well, they're all the same)
    config['log_config']['loggers']['quart'] = {
        "handlers": [
            "default"
        ],
        "level": "INFO"
    }

    uvicorn.run("genius_agent_api:app", host="0.0.0.0", port=3001, reload=True,
                log_level="debug", **config)
