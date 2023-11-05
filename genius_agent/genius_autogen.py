import os
import autogen

import json
import openai
from agent_constructs import AgentsConfig, Agents
from pathlib import Path

# Set the OpenAI token
openai.api_key = "YOUR_TOKEN"

# Set the OpenAI URL
openai.api_url = "https://localhost:8080/v1/"
autogen.ChatCompletion.start_logging()


def chat(prompt="Build snake game using pygame", chat_initiator_name: str = "executor"):
    agents_manager = Agents()
    agents_manager.load_config(file=f'{Path("agent_configs.yml")}')
    agents_manager.load_agents()
    agents_manager.set_chat_initiator(name=chat_initiator_name)
    # print(f"AGENT MODELS: {len(agents_manager.agents_config)}")
    #print(f"AGENTS: {agents_manager.agents}")
    #chat_initiator = agents_manager.find_agent(name=chat_initiator_name)
    #print(f"CHAT INITIATOR: {chat_initiator}")
    #group_chat = GroupChat(agents=agents, messages=[], max_round=12)
    #print(f"LLMCONFIG: {chat_initiator.llm_config}")
    #manager = GroupChatManager(groupchat=group_chat, llm_config=chat_initiator.llm_config)
    agents_manager.load_group_chat()
    agents_manager.chat_initiator.initiate_chat(
        agents_manager.group_chat_manager,
        message=prompt,
    )


chat(prompt="Build snake game using pygame")
