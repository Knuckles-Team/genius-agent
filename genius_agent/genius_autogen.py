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
                code_execution_config=agent.code_execution_config,
                retrieve_config=agent.retrieve_config or None,
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


# def load_agents(file: str = None, dictionary: dict = None):
#     # if file:
#     agents_data = yaml.safe_load(Path(file).read_text())
#     print(f"FILE DATA: {json.dumps(agents_data, indent=2)}")
# elif dictionary:
#     agents_data = dictionary
# else:
#     #print("Unable to load data")
#     return 1
# agents = Agents.model_validate(agents_data)
# return agents


def chat(prompt="Build snake game using pygame", chat_initiator_name: str = "admin"):
    agents_data = yaml.safe_load(Path("agent_configs.yml").read_text())
    agents_models = Agents.model_validate(agents_data)
    agents = load_agents(agents_models)
    chat_initiator = None
    group_chat = GroupChat(agents=agents, messages=[], max_round=12)
    print(f"LLMCONFIG: {agents[0].llm_config}")

    for agent in agents:
        if agent.name == chat_initiator_name:
            chat_initiator = agent
            print(f"CHAT INITIATOR FOUND: {chat_initiator.name}")
            break

    manager = GroupChatManager(groupchat=group_chat, llm_config=chat_initiator.llm_config)
    chat_initiator.initiate_chat(
        manager,
        message=prompt,
    )


chat(prompt="Build snake game using pygame")
