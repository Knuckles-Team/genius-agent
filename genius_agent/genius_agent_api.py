from agent_constructs import Agents, AgentsConfig
from fastapi import FastAPI
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

agents_manager = Agents()
app = FastAPI()

@app.get("/agents_config/{name}")
async def get_agent_config_by_name(name: str) -> [AgentsConfig, dict]:
    agent_config = agents_manager.find_agent_config(name=name)
    if agent_config:
        return agent_config
    else:
        return {"error": "Object not found"}

@app.get("/health", response_model=HealthResponse)
async def get_health() -> HealthResponse:
    health_response = HealthResponse.model_validate({"status": "200 OK"})
    return health_response

@app.get("/agents_config", response_model=AgentsConfig)
async def get_agent_configs() -> AgentsConfig:
    return agents_manager.agents_config

@app.post("/agents_config/load")
async def post_load_agents_config(agents_config: dict):
    agents_manager.load_config(payload=agents_config)

@app.post("/agents/load")
async def post_load_agents():
    agents_manager.load_agents()

@app.post("/agents/chat_initiator/{chat_initiator_name}")
async def post_chat_initiator(chat_initiator_name: str = None):
    agents_manager.set_chat_initiator(name=chat_initiator_name)

@app.post("/group_chat/load")
async def post_load_group():
    agents_manager.load_group_chat()

@app.post("/chat/{prompt}")
async def post_chat(prompt: str):
    agents_manager.chat_initiator.initiate_chat(
        agents_manager.group_chat_manager,
        message=prompt,
    )
