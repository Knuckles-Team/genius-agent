from agent_model import AgentsConfig
from typing import List, Dict, Optional, Callable, Union
import yaml
from pathlib import Path
from autogen import (GroupChat, GroupChatManager)
try:
    from autogen import UserProxyAgent
except ImportError:
    pass
try:
    from autogen import AssistantAgent
except ImportError:
    pass
try:
    from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
except ImportError:
    pass
try:
    from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
except ImportError:
    pass
try:
    from autogen.agentchat.contrib.teachable_agent import TeachableAgent
except ImportError:
    pass
try:
    import memgpt.autogen.memgpt_agent as memgpt_autogen
    import memgpt.autogen.interface as autogen_interface
    import memgpt.presets as presets
    from memgpt.persistence_manager import (InMemoryStateManager,
                                            InMemoryStateManagerWithPreloadedArchivalMemory,
                                            InMemoryStateManagerWithFaiss)
except ImportError:
    pass
try:
    from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
except ImportError:
    pass
try:
    from autogen.agentchat.contrib.multimodal_conversable_agent import MultimodalConversableAgent
except ImportError:
    pass


# Python Agents Class with Autogen Models
class Agents:
    def __init__(self):
        self.agents_config = None
        self.agents = None
        self.agent_types = []
        self.chat_initiator = None
        self.group_chat = None
        self.agent_chat_manager = None
        self.group_chat_enabled = True

    def set_chat_initiator(self, name):
        self.chat_initiator = self.find_agent(name)

    def load_config(self, file: str = None, payload: dict = None) -> AgentsConfig:
        if file is not None:
            agents_data = yaml.safe_load(Path(file).read_text())
        else:
            agents_data = payload
        self.agents_config = AgentsConfig.model_validate(agents_data)
        return self.agents_config

    def get_agent_types(self) -> List[str]:
        for agent_config in self.agents_config.agents:
            if agent_config.agent_type == "user_proxy":
                self.agent_types.append("user_proxy")
            elif agent_config.agent_type == "assistant":
                self.agent_types.append("assistant")
            elif agent_config.agent_type == "retrieve_user_proxy":
                self.agent_types.append("retrieve_user_proxy")
            elif agent_config.agent_type == "retrieve_assistant":
                self.agent_types.append("retrieve_assistant")
            elif agent_config.agent_type == "teachable":
                self.agent_types.append("teachable")
            elif agent_config.agent_type == "memgpt":
                self.agent_types.append("memgpt")
            elif agent_config.agent_type == "gpt_assistant":
                self.agent_types.append("gpt_assistant")
            elif agent_config.agent_type == "multimodal_assistant":
                self.agent_types.append("multimodal_assistant")
        self.agent_types = list(set(self.agent_types))
        return self.agent_types

    def load_agents(self) -> List:
        loaded_agents = []
        # print(f"AGENTS: {agents}")
        for agent_config in self.agents_config.agents:
            print(f"AGENT: {agent_config}")
            if agent_config.agent_type == "user_proxy":
                agent = UserProxyAgent(
                    name=agent_config.name,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    human_input_mode=agent_config.human_input_mode or None,
                    system_message=agent_config.instructions or None,
                    code_execution_config=agent_config.code_execution_config or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "assistant":
                agent = AssistantAgent(
                    name=agent_config.name,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.instructions or None,
                    code_execution_config=agent_config.code_execution_config or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "retrieve_user_proxy":
                agent = RetrieveUserProxyAgent(
                    name=agent_config.name,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.instructions or None,
                    human_input_mode=agent_config.human_input_mode or None,
                    code_execution_config=agent_config.code_execution_config or None,
                    retrieve_config=agent_config.retrieve_config.model_dump(),
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "retrieve_assistant":
                agent = RetrieveAssistantAgent(
                    name=agent_config.name or None,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.instructions or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "teachable":
                agent = TeachableAgent(
                    name=agent_config.name or None,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.instructions or None,
                    llm_config=agent_config.llm_config,
                    teach_config=agent_config.teach_config.model_dump() or None
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "memgpt":
                interface = autogen_interface.AutoGenInterface()  # how MemGPT talks to AutoGen
                persistence_manager = InMemoryStateManager()
                memgpt_agent = presets.use_preset(presets.DEFAULT, 'gpt-4', agent.persona, agent.human, interface,
                                                  persistence_manager)
                agent = memgpt_autogen.MemGPTAgent(
                    name="MemGPT_coder",
                    agent=memgpt_agent,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "gpt_assistant":
                agent = GPTAssistantAgent(
                    name=agent_config.name or None,
                    instructions=agent_config.instructions or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "multimodal_assistant":
                agent = MultimodalConversableAgent(
                    name=agent_config.name or None,
                    max_consecutive_auto_reply=agent_config.max_consecutive_auto_reply or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
        self.agents = loaded_agents
        if len(self.agents) > 1:
            self.load_group_chat()
        else:
            self.agent_chat_manager = self.agents
        return loaded_agents

    def chat(self, prompt: str):
        self.chat_initiator.initiate_chat(
            self.agent_chat_manager,
            message=prompt,
        )

    def load_group_chat(self):
        self.group_chat = GroupChat(agents=self.agents, messages=[], max_round=12)
        print(f"LLMCONFIG: {self.chat_initiator.llm_config}")
        self.agent_chat_manager = GroupChatManager(groupchat=self.group_chat, llm_config=self.chat_initiator.llm_config)

    def find_agent(self, name: str) -> List:
        for agent in self.agents:
            print(f"NAMES: {agent.name}")
            if agent.name == name:
                print(f"MATCH: {agent.name}")
                return agent

    def find_agent_config(self, name: str) -> AgentsConfig:
        for agent_config in self.agents_config.agents:
            print(f"NAMES: {agent_config.name}")
            if agent_config.name == name:
                print(f"MATCH: {agent_config.name}")
                return agent_config
