#!/usr/bin/env python
# coding: utf-8
import uvicorn
import io
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor
from agent_construct import Agents, AgentsConfig
from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, field_validator, model_validator
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


class Chat(BaseModel):
    agents: list[str]
    message: str


class HealthResponse(BaseModel):
    status: str


class Prompt(BaseModel):
    prompt: str
    max_consecutive_replies: Optional[int] = None
    cache_seed: Optional[int] = None

    @field_validator("max_consecutive_replies")
    def validate_max_consecutive_replies(cls, value):
        if not value:
            return value
        if isinstance(value, str):
            try:
                max_consecutive_replies = int(value)
            except Exception:
                raise ValueError(f"max_consecutive_replies was not passed as str: {value}")
        elif isinstance(value, int):
            max_consecutive_replies = value
        else:
            raise ValueError(f"max_consecutive_replies was not passed as int: {value}")
        return max_consecutive_replies

    @field_validator("cache_seed")
    def validate_cache_seed(cls, value):
        if not value:
            return value
        if isinstance(value, str):
            try:
                cache_seed = int(value)
            except Exception:
                raise ValueError(f"cache_seed was not passed as str: {value}")
        elif isinstance(value, int):
            cache_seed = value
        else:
            raise ValueError(f"cache_seed was not passed as int: {value}")
        return cache_seed

@app.get("/")
def read_root():
    return {"message": "API/WebSocket server is running."}

@app.get("/api/agents/{name}")
async def get_agent_config_by_name(name: str) -> Union[AgentsConfig, dict]:
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

# def blocking_chat(prompt: str) -> str:
#     response = agents_manager.chat(prompt=prompt)
#     return response  # Replace this with your actual generated text
#
# async def run_agents_manager(prompt: str, output_queue: asyncio.Queue):
#     # Redirect stdout to capture the output
#     sys.stdout = io.StringIO()
#     print("REACHED MANAGER")
#
#     # Run the blocking task in a separate thread
#     loop = asyncio.get_event_loop()
#     result = await loop.run_in_executor(ThreadPoolExecutor(), blocking_chat, prompt)
#     print("Generated text from blocking_chat:", result)
#     # Restore the original stdout
#     sys.stdout = sys.__stdout__
#
#     # Put the result into the output queue
#     output_queue.put_nowait(result)
#
#     # Signal the end of the stream
#     output_queue.put_nowait(None)
#
# @app.post("/api/chat", response_class=StreamingResponse)
# async def post_chat(prompt: Prompt):
#     print(f"Streaming Stuff: {prompt.prompt}")
#     output_queue = asyncio.Queue()
#
#     # Start the text generation task
#     asyncio.create_task(run_agents_manager(prompt=prompt.prompt, output_queue=output_queue))
#
#     async def stream_text():
#         while True:
#             text = await output_queue.get()
#             if text is None:
#                 break
#             print("Text received from output_queue:", text)
#             yield text.encode("utf-8")
#             await asyncio.sleep(0.3)  # Adjust the sleep time if needed
#
#     return StreamingResponse(stream_text(), media_type="text/plain")

@app.websocket("/api/chat") #, response_model=Chat)
async def post_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        prompt = await websocket.receive_text()
        response = agents_manager.chat(prompt=prompt)
        await websocket.send_text(response)
    ####
    #### HANDLE SETTING CACHE SEED prompt.cache_seed
    #### HANDLE SETTING GLOBAL MAX_CONSECURTIVE_REPLY_FIELD prompt.max_consecutive_reply
    return StreamingResponse(agents_manager.chat(prompt=prompt.prompt), media_type="text/plain")


@app.post("/api/prometheus/{port}")
async def deploy_exporter(port: Union[int, str]):
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

    config['log_config']['loggers']['quart'] = {
        "handlers": [
            "default"
        ],
        "level": "INFO"
    }

    uvicorn.run("genius_agent_api:app", host="0.0.0.0", port=3001, reload=True,
                log_level="debug", **config)
