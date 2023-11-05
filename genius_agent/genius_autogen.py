import os
import autogen
import yaml
import json
import openai
from agent_constructs import Agents
from pathlib import Path
from autogen import (AssistantAgent,
                     UserProxyAgent,
                     GroupChat,
                     GroupChatManager)
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
# Set the OpenAI token
openai.api_key = "YOUR_TOKEN"

# Set the OpenAI URL
openai.api_url = "https://localhost:8080/v1/"
autogen.ChatCompletion.start_logging()


def load_agents(agents: Agents):
    loaded_agents = []
    # print(f"AGENTS: {agents}")
    for agent in agents.agents:
        print(f"AGENT: {agent}")
        if agent.agent_type == "user_proxy":
            loaded_agents.append(UserProxyAgent(
                name=agent.name,
                is_termination_msg=agent.is_termination_msg,
                human_input_mode=agent.human_input_mode,
                system_message=agent.system_message,
                code_execution_config=agent.code_execution_config,
                llm_config=agent.llm_config,
            ))
        elif agent.agent_type == "assistant":
            loaded_agents.append(AssistantAgent(
                name=agent.name,
                is_termination_msg=agent.is_termination_msg,
                system_message=agent.system_message,
                code_execution_config=agent.code_execution_config,
                llm_config=agent.llm_config,
            ))
        elif agent.agent_type == "retrieve_user_proxy":
            loaded_agents.append(RetrieveUserProxyAgent(
                name=agent.name,
                is_termination_msg=agent.is_termination_msg,
                system_message=agent.system_message,
                human_input_mode=agent.human_input_mode or None,
                code_execution_config=agent.code_execution_config.model_dump(),
                retrieve_config=agent.retrieve_config.model_dump() or None,
                llm_config=agent.llm_config,
            ))
        elif agent.agent_type == "retrieve_assistant":
            loaded_agents.append(RetrieveAssistantAgent(
                name=agent.name,
                is_termination_msg=agent.is_termination_msg or None,
                system_message=agent.system_message or None,
                llm_config=agent.llm_config,
            ))
        elif agent.agent_type == "teachable":
            loaded_agents.append(TeachableAgent(
                name=agent.name,
                is_termination_msg=agent.is_termination_msg or None,
                system_message=agent.system_message or None,
                llm_config=agent.llm_config,
                teach_config=agent.teach_config
            ))
    return loaded_agents


def find_agent(agents, name):
    for agent in agents:
        print(f"NAMES: {agent.name}")
        if agent.name == name:
            print(f"MATCH: {agent.name}")
            return agent


def chat(prompt="Build snake game using pygame", chat_initiator_name: str = "user_proxy"):
    agents_data = yaml.safe_load(Path("agent_configs.yml").read_text())
    agents_models = Agents.model_validate(agents_data)
    print(f"AGENT MODELS: {len(agents_models.agents)}")
    agents = load_agents(agents_models)
    print(f"AGENTS: {agents}")
    chat_initiator = find_agent(agents, "executor")
    print(f"CHAT INITER: {chat_initiator}")
    group_chat = GroupChat(agents=agents, messages=[], max_round=12)
    print(f"LLMCONFIG: {chat_initiator.llm_config}")
    manager = GroupChatManager(groupchat=group_chat, llm_config=chat_initiator.llm_config)
    chat_initiator.initiate_chat(
        manager,
        message=prompt,
    )


chat(prompt="Build snake game using pygame")
