import os
import autogen
import yaml
import json
from agent_constructs import Agents
from pathlib import Path
from autogen import (AssistantAgent,
                     UserProxyAgent,
                     GroupChat,
                     GroupChatManager)
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent


autogen.ChatCompletion.start_logging()


def load_agents(file: str = None, dictionary: dict = None):
    if file:
        agents_data = yaml.safe_load(Path(file).read_text())
        print(f"FILE DATA: {json.dumps(agents_data, indent=2)}")
    elif dictionary:
        agents_data = dictionary
    else:
        #print("Unable to load data")
        return 1
    agents = Agents.model_validate(agents_data)
    return agents

def chat(prompt="Build snake game using pygame"):
    agents = load_agents(f'{os.path.realpath(os.path.dirname(__file__))}/agent_configs.yml')
    group_chat = GroupChat(agents=agents.get_agents(), messages=[], max_round=12)
    manager = GroupChatManager(groupchat=group_chat, llm_config=agents[0].llm_config)
    agents.Admin.initiate_chat(
        manager.manager,
        message=prompt,
    )

chat(prompt="Build snake game using pygame")

