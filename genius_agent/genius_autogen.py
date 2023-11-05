import os
import autogen

import json
import openai
from agent_constructs import AgentsConfig, Agents
from pathlib import Path

openai.api_key = "YOUR_TOKEN"
openai.api_url = "https://localhost:8080/v1/"
autogen.ChatCompletion.start_logging()


def chat(prompt="Build snake game using pygame", chat_initiator_name: str = "executor"):
    agents_manager = Agents()
    agents_manager.load_config(file=f'{Path("agent_configs.yml")}')
    agents_manager.load_agents()
    agents_manager.set_chat_initiator(name=chat_initiator_name)
    agents_manager.load_group_chat()
    agents_manager.chat_initiator.initiate_chat(
        agents_manager.group_chat_manager,
        message=prompt,
    )


chat(prompt="Build snake game using pygame")
