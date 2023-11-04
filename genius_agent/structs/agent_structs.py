from typing import List, Dict, Optional, Any
from pydantic import BaseModel
from itertools import chain
from autogen import (AssistantAgent as AutoAssistantAgent,
                     UserProxyAgent as AutoUserProxyAgent,
                     GroupChat as AutoGroupChat,
                     GroupChatManager as AutoGroupChatManager)
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent as AutoRetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent as AutoRetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent as AutoTeachableAgent
from structs.llm_config_structs import LLMConfig
from agent_functions import *
import os
import importlib.util
import yaml
from pathlib import Path
from structs.llm_config_structs import LLMConfig


# # Import all custom agent functions
# current_directory = os.path.dirname(os.path.realpath(__file__))
# agent_functions_path = os.path.join(current_directory, '..', 'agent_functions')
# python_files = [f for f in os.listdir(agent_functions_path) if f.endswith('.py')]
# for file_name in python_files:
#     module_name = os.path.splitext(file_name)[0]
#     module_path = os.path.join(agent_functions_path, file_name)
#
#     spec = importlib.util.spec_from_file_location(module_name, module_path)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)


class CodeExecutionConfig(BaseModel):
    work_dir: str


class RetrieveConfig(BaseModel):
    task: str
    docs_path: List[str]
    chunk_token_size: Optional[int]
    model: Optional[str]
    collection_name: Optional[str]
    get_or_create: Optional[bool]


class TeachConfig(BaseModel):
    verbosity: Optional[int]
    reset_db: Optional[bool]
    path_to_db_dir: Optional[str]
    recall_threshold: Optional[int]


class Agent(BaseModel):
    name: str
    llm_config: LLMConfig
    system_message: Optional[str]
    is_termination_msg: Optional[str]
    human_input_mode: Optional[str] = "NEVER"
    max_consecutive_auto_reply: Optional[int] = 10
    code_execution_config: Optional[CodeExecutionConfig] = None
    retrieve_config: Optional[RetrieveConfig] = None
    teach_config: Optional[TeachConfig] = None

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.llm_config_data = yaml.safe_load(Path('../config_examples/llm_configs.yml').read_text())
        self.llm_config = LLMConfig.model_validate(self.llm_config_data)


class UserProxyAgent(Agent):
    def __init__(self, name, llm_config, is_termination_msg=None, human_input_mode=None, system_message=None, code_execution_config=None):
        super().__init__(
            name=name,
            llm_config=llm_config,
            system_message=system_message,
            is_termination_msg=is_termination_msg,
            human_input_mode=human_input_mode,
            code_execution_config=code_execution_config)
        self.agent = (AutoUserProxyAgent(
            name=self.name,
            is_termination_msg=self.is_termination_msg,
            human_input_mode=self.human_input_mode,
            system_message=self.system_message,
            code_execution_config=self.code_execution_config
        ))


    def map_functions(self, functions_mapping):
        self.user_proxy_agent.register_function(
            function_map=functions_mapping
        )


class AssistantAgent(Agent):
    def __init__(self, name, llm_config, is_termination_msg=None, human_input_mode=None, system_message=None, code_execution_config=None):
        super().__init__(
            name=name,
            llm_config=llm_config,
            system_message=system_message,
            is_termination_msg=is_termination_msg,
            human_input_mode=human_input_mode,
            code_execution_config=code_execution_config)
        self.agent = (AutoAssistantAgent(
            name=self.name,
            is_termination_msg=self.is_termination_msg,
            system_message=self.system_message,
            code_execution_config=self.code_execution_config,
            llm_config=Agent.llm_config,
        ))


class RetrieveUserProxyAgent(Agent):
    def __init__(self, name, llm_config, is_termination_msg=None, human_input_mode=None, system_message=None, code_execution_config=None):
        super().__init__(
            name=name,
            llm_config=llm_config,
            system_message=system_message,
            is_termination_msg=is_termination_msg,
            human_input_mode=human_input_mode,
            code_execution_config=code_execution_config)
        self.agent = (AutoRetrieveUserProxyAgent(
            name=self.name,
            is_termination_msg=self.is_termination_msg,
            system_message=self.system_message,
            human_input_mode=self.human_input_mode or None,
            code_execution_config=self.code_execution_config,
            retrieve_config=self.retrieve_config or None,
            llm_config=self.llm_config,
        ))


class RetrieveAssistantAgent(Agent):
    def __init__(self, name, llm_config, is_termination_msg=None, system_message=None):
        super().__init__(
            name=name,
            llm_config=llm_config,
            system_message=system_message,
            is_termination_msg=is_termination_msg)
        self.agent = (AutoRetrieveAssistantAgent(
            name=self.name,
            is_termination_msg=self.is_termination_msg or None,
            system_message=self.system_message or None,
            llm_config=self.llm_config,
        ))


class TeachableAgent(Agent):
    def __init__(self, name, llm_config, is_termination_msg=None, system_message=None, teach_config=None):
        super().__init__(
            name=name,
            llm_config=llm_config,
            system_message=system_message,
            is_termination_msg=is_termination_msg,
            teach_config=teach_config)
        self.agent = (AutoTeachableAgent(
            name=self.name,
            is_termination_msg=self.is_termination_msg or None,
            system_message=self.system_message or None,
            llm_config=self.llm_config,
            teach_config=self.teach_config
        ))



class Agents(BaseModel):
    user_proxy_agents: List[UserProxyAgent] or None
    assistant_agents: List[AssistantAgent] or None
    retrieve_user_proxy_agents: List[RetrieveUserProxyAgent] or None
    retrieve_assistant_agents: List[RetrieveAssistantAgent] or None
    teachable_agents: List[TeachableAgent] or None

    def get_all_agents(self) -> List[BaseModel]:
        return list(chain(
            self.user_proxy_agents,
            self.assistant_agents,
            self.retrieve_user_proxy_agents,
            self.retrieve_assistant_agents,
            self.teachable_agents
        ))

    def map_functions(self):
        llm_config = LLMConfig
        for user in self.user_proxy_agents:
            user.map_functions(llm_config.function_map)


class GroupChat(BaseModel):
    def __init__(self, **data: Any):
        super().__init__(**data)
        self.group_chat = AutoGroupChat(agents=self.get_all_agents(), messages=[], max_round=12)


class Manager(BaseModel):
    def __init__(self, **data: Any):
        super().__init__(**data)

        self.manager = AutoGroupChatManager(groupchat=self.group_chat, llm_config=LLMConfig)
