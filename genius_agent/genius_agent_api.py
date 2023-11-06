from agent_constructs import Agents, AgentsConfig
from fastapi import FastAPI

agents_manager = Agents()
app = FastAPI()

@app.get("/agents_config/{name}")
async def get_agent_config_by_name(self, name: str) -> [AgentsConfig, dict]:
    agent_config = self.agents_manager.find_agent_config(name=name)
    if agent_config:
        return agent_config
    else:
        return {"error": "Object not found"}

@app.get("/agents_config")
async def get_agent_configs(self) -> AgentsConfig:
    return self.agents_manager.agents_config

@app.post("/agents_config/load")
async def post_load_agents_config(self, agents_config: dict):
    self.agents_manager.load_config(payload=agents_config)

@app.post("/agents/load")
async def post_load_agents(self):
    self.agents_manager.load_agents()

@app.post("/agents/chat_initiator/{chat_initiator_name}")
async def post_chat_initiator(self, chat_initiator_name: str = None):
    self.agents_manager.set_chat_initiator(name=chat_initiator_name)

@app.post("/group_chat/load")
async def post_load_group(self):
    self.agents_manager.load_group_chat()

@app.post("/chat/{prompt}")
async def post_chat(self, prompt: str):
    self.agents_manager.chat_initiator.initiate_chat(
        self.agents_manager.group_chat_manager,
        message=prompt,
    )
