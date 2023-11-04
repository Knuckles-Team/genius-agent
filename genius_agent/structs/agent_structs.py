from typing import List, Dict, Optional
from pydantic import BaseModel
from itertools import chain
from autogen import (AssistantAgent as AutoAssistantAgent,
                     UserProxyAgent as AutoUserProxyAgent,
                     GroupChat as AutoGroupChat,
                     GroupChatManager as AutoGroupChatManager)
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
from llm_config_structs import LLMConfig
from ..agent_functions import *
import os
import importlib.util

# Import all custom agent functions
current_directory = os.path.dirname(os.path.realpath(__file__))
agent_functions_path = os.path.join(current_directory, '..', 'agent_functions')
python_files = [f for f in os.listdir(agent_functions_path) if f.endswith('.py')]
for file_name in python_files:
    module_name = os.path.splitext(file_name)[0]
    module_path = os.path.join(agent_functions_path, file_name)

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


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
    llm_config: str
    system_message: Optional[str]
    is_termination_msg: Optional[str]
    human_input_mode: Optional[str] = "NEVER"
    max_consecutive_auto_reply: Optional[int] = 10
    code_execution_config: Optional[CodeExecutionConfig] = None
    retrieve_config: Optional[RetrieveConfig] = None
    teach_config: Optional[TeachConfig] = None


class UserProxyAgent(Agent):
    AutoUserProxyAgent(
        name=Agent.name,
        is_termination_msg=Agent.is_termination_msg or None,
        human_input_mode=Agent.human_input_mode or None,
        system_message=Agent.system_message or None,
        code_execution_config=Agent.code_execution_config or None,
    ).register_function(
        function_map={
            "python": python_func.exec_python,
            "bash": bash_func.exec_bash,
            "media_download": media_downloader_func.exec_media_downloader,
            "write_to_file": file_func.exec_write_to_file,
            "read_from_file": file_func.exec_read_from_file,
            "create_directory": file_func.exec_create_directory,
        }
    )


class AssistantAgent(Agent):
    AutoAssistantAgent(
        name=Agent.name,
        is_termination_msg=Agent.is_termination_msg or None,
        system_message=Agent.system_message or None,
        llm_config=Agent.llm_config,
    )


class RetrieveUserProxyAgent(Agent):
    RetrieveUserProxyAgent(
        name=Agent.name,
        is_termination_msg=Agent.is_termination_msg or None,
        system_message=Agent.system_message or None,
        llm_config=Agent.llm_config,
        human_input_mode=Agent.human_input_mode or None,
        max_consecutive_auto_reply=Agent.max_consecutive_auto_reply or None,
        retrieve_config=Agent.retrieve_config or None,
        code_execution_config=Agent.code_execution_config or None,
    )


class RetrieveAssistantAgent(Agent):
    RetrieveAssistantAgent(
        name=Agent.name,
        is_termination_msg=Agent.is_termination_msg or None,
        system_message=Agent.system_message or None,
        llm_config=Agent.llm_config,
    )


class TeachableAgent(Agent):
    TeachableAgent(
        name=Agent.name,
        is_termination_msg=Agent.is_termination_msg or None,
        system_message=Agent.system_message or None,
        llm_config=Agent.llm_config,
        teach_config=Agent.teach_config
    )


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


class GroupChat(Agents):
    AutoGroupChat(agents=Agents.get_all_agents(), messages=[], max_round=12)


class Manager(GroupChat):
    AutoGroupChatManager(groupchat=GroupChat, llm_config=LLMConfig)
