from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, field_validator
from itertools import chain
import json
from autogen import (AssistantAgent as AutoAssistantAgent,
                     UserProxyAgent as AutoUserProxyAgent,
                     GroupChat as AutoGroupChat,
                     GroupChatManager as AutoGroupChatManager)
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent as AutoRetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent as AutoRetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent as AutoTeachableAgent
from agent_functions import *
import os
import importlib.util
import yaml
from pathlib import Path
from typing import List, Dict, Optional, Callable, Any
from pydantic import BaseModel, validator
from agent_functions import *


class LLMModel(BaseModel):
    model: str
    api_key: Optional[str] = "NA"
    api_base: Optional[str] = "NA"
    api_type: Optional[str] = "NA"
    api_version: Optional[str] = None


class FilterDict(BaseModel):
    model: Optional[List[str]]


class Parameters(BaseModel):
    type: str
    properties: Optional[Dict[str, Dict[str, str]]]
    required: Optional[List[str]]


class FunctionItem(BaseModel):
    name: str
    description: str
    parameters: Parameters


class FunctionMap(BaseModel):
    python: Callable
    bash: Callable
    media_download: Callable
    write_to_file: Callable
    read_from_file: Callable
    create_directory: Callable


class LLMConfig(BaseModel):
    seed: Optional[int] = 42
    temperature: Optional[float] = 0
    config_list: Optional[List[LLMModel]]
    filter_dict: Optional[FilterDict]
    request_timeout: Optional[float]
    repeat_penalty: Optional[float]
    functions: Optional[List[FunctionItem]]
    function_map: Optional[FunctionMap]

    # def __init__(self, **data: Any):
    #
    #     super().__init__(**data)
    #
    @validator("function_map", pre=True, always=True)
    def convert_to_callable(cls, value):
        converted_callables = {}
        for key, item in value.items():
            if isinstance(item, str):
                try:
                    # Attempt to evaluate the string as a Python expression
                    converted_callables[key] = eval(item)
                except Exception:
                    raise ValueError(f"Invalid callable string for value '{value}'")
            elif isinstance(item, Callable):
                converted_callables[key] = item
            else:
                raise ValueError(f"Invalid type for value '{value}', expected a string or callable")
        return converted_callables


class CodeExecutionConfig(BaseModel):
    work_dir: str


class RetrieveConfig(BaseModel):
    task: str
    docs_path: Optional[List[str]]
    chunk_token_size: Optional[float] = None
    model: Optional[str] = None
    collection_name: Optional[str] = None
    get_or_create: Optional[bool] = None


class TeachConfig(BaseModel):
    verbosity: Optional[int]
    reset_db: Optional[bool]
    path_to_db_dir: Optional[str]
    recall_threshold: Optional[float]


# Base Agent Class that contains all shared variables between Agent Types
class Agent(BaseModel):
    name: str
    llm_config: Optional[Union[LLMConfig, dict]] = None
    system_message: Optional[str] = None
    is_termination_msg: Optional[str] = None
    human_input_mode: Optional[str] = "NEVER"
    max_consecutive_auto_reply: Optional[int] = 10
    code_execution_config: Optional[CodeExecutionConfig] = None
    retrieve_config: Optional[RetrieveConfig] = None
    teach_config: Optional[TeachConfig] = None
    agent_type: str

    @field_validator('agent_type')
    def agent_type_selection(cls, value):
        if value not in ["user_proxy", "teachable", "assistant", "retrieve_user_proxy", "retrieve_assistant"]:
            raise ValueError
        return value

    # @field_validator('agent_type')
    # def agent_type_mapping(cls, value):
    #     if value != ["user_proxy", "teachable", "assistant", "retrieve_user_proxy", "retrieve_assistant_agents"]:
    #         raise ValueError

# class UserProxyAgent(Agent):
#     agent: AutoUserProxyAgent = None
#     def __init__(self, name, llm_config: Union[LLMConfig, dict] = None, is_termination_msg=None, human_input_mode=None,
#                  system_message=None, code_execution_config=None):
#         #print(f"LLM_CONFIG: {llm_config}")
#         super().__init__(
#             name=name,
#             llm_config=llm_config,
#             system_message=system_message,
#             is_termination_msg=is_termination_msg,
#             human_input_mode=human_input_mode,
#             code_execution_config=code_execution_config)
#         self.agent = (AutoUserProxyAgent(
#             name=self.name,
#             is_termination_msg=self.is_termination_msg,
#             human_input_mode=self.human_input_mode,
#             system_message=self.system_message,
#             code_execution_config=self.code_execution_config
#         ))
#
#     def map_functions(self, functions_mapping):
#         self.user_proxy_agent.register_function(
#             function_map=functions_mapping
#         )
#
#
# class AssistantAgent(Agent):
#     agent: AutoAssistantAgent = None
#     def __init__(self, name, llm_config:Union[LLMConfig, dict] = None, is_termination_msg=None, human_input_mode=None,
#                  system_message=None,
#                  code_execution_config=None):
#         super().__init__(
#             name=name,
#             llm_config=llm_config,
#             system_message=system_message,
#             is_termination_msg=is_termination_msg,
#             human_input_mode=human_input_mode,
#             code_execution_config=code_execution_config)
#         self.agent = (AutoAssistantAgent(
#             name=self.name,
#             is_termination_msg=self.is_termination_msg,
#             system_message=self.system_message,
#             code_execution_config=self.code_execution_config,
#             llm_config=self.llm_config.model_dump(),
#         ))
#
#
# class RetrieveUserProxyAgent(Agent):
#     agent: AutoRetrieveUserProxyAgent = None
#
#     def __init__(self, name, llm_config:Union[LLMConfig, dict] = None, is_termination_msg=None, human_input_mode=None,
#                  system_message=None,
#                  code_execution_config=None):
#         super().__init__(
#             name=name,
#             llm_config=llm_config,
#             system_message=system_message,
#             is_termination_msg=is_termination_msg,
#             human_input_mode=human_input_mode,
#             code_execution_config=code_execution_config)
#         self.agent = (AutoRetrieveUserProxyAgent(
#             name=self.name,
#             is_termination_msg=self.is_termination_msg,
#             system_message=self.system_message,
#             human_input_mode=self.human_input_mode or None,
#             code_execution_config=self.code_execution_config,
#             retrieve_config=self.retrieve_config or None,
#             llm_config=self.llm_config,
#         ))
#
#
# class RetrieveAssistantAgent(Agent):
#     agent: AutoRetrieveAssistantAgent = None
#     def __init__(self, name, llm_config:Union[LLMConfig, dict] = None, is_termination_msg=None, system_message=None):
#         super().__init__(
#             name=name,
#             llm_config=llm_config,
#             system_message=system_message,
#             is_termination_msg=is_termination_msg)
#         self.agent = (AutoRetrieveAssistantAgent(
#             name=self.name,
#             is_termination_msg=self.is_termination_msg or None,
#             system_message=self.system_message or None,
#             llm_config=self.llm_config,
#         ))
#
#
# class TeachableAgent(Agent):
#     agent: AutoTeachableAgent = None
#     def __init__(self, name, llm_config:Union[LLMConfig, dict] = None, is_termination_msg=None, system_message=None,
#                  teach_config=None):
#         super().__init__(
#             name=name,
#             llm_config=llm_config,
#             system_message=system_message,
#             is_termination_msg=is_termination_msg,
#             teach_config=teach_config)
#         self.agent = (AutoTeachableAgent(
#             name=self.name,
#             is_termination_msg=self.is_termination_msg or None,
#             system_message=self.system_message or None,
#             llm_config=self.llm_config,
#             teach_config=self.teach_config
#         ))


class Agents(BaseModel):
    agents: List[Agent]

    # def __init__(self, user_proxy_agents, assistant_agents, retrieve_user_proxy_agents,
    #              retrieve_assistant_agents, teachable_agents):
    #     super().__init__(user_proxy_agents=[UserProxyAgent.model_validate(user_proxy_agent) for user_proxy_agent in user_proxy_agents],
    #                      assistant_agents=[AssistantAgent.model_validate(assistant_agent) for assistant_agent in assistant_agents],
    #                      retrieve_user_proxy_agents=[RetrieveUserProxyAgent.model_validate(retrieve_user_proxy_agent) for retrieve_user_proxy_agent in retrieve_user_proxy_agents],
    #                      retrieve_assistant_agents=[RetrieveAssistantAgent.model_validate(retrieve_assistant_agent) for retrieve_assistant_agent in retrieve_assistant_agents],
    #                      teachable_agents=[TeachableAgent.model_validate(teachable_agent) for teachable_agent in teachable_agents])
    #     print(f"ALL user_proxy_agents: {json.dumps(user_proxy_agents, indent=2)}")
    #     # for user_proxy_agent in user_proxy_agents:
    #     #     self.user_proxy_agents.append(Agents.model_validate(user_proxy_agent))
    #     # #self.user_proxy_agents = user_proxy_agents
    #     # self.assistant_agents = assistant_agents
    #     # self.retrieve_user_proxy_agents = retrieve_user_proxy_agents
    #     # self.retrieve_assistant_agents = retrieve_assistant_agents
    #     # self.teachable_agents = teachable_agents
    #     self.agents = (self.user_proxy_agents + self.assistant_agents + self.retrieve_user_proxy_agents +
    #                    self.retrieve_assistant_agents + self.teachable_agents)
    #
    #
    # def get_agents(self):
    #     return self.agents

#
# class GroupChat(BaseModel):
#     group_chat = AutoGroupChat or None

#     def __init__(self, agents: Agents = None):
#         super().__init__()
#         self.agents = agents
#         self.group_chat = AutoGroupChat(agents=self.agents.get_agents(), messages=[], max_round=12)

#
# class Manager(BaseModel):
#     def __init__(self, file: str):
#         super().__init__()
#         print(f"FILE {file}")
#         self.agents = self.load_agents(file)
#         self.group_chat = AutoGroupChat(agents=self.agents.get_agents(), messages=[], max_round=12)
#         self.manager = AutoGroupChatManager(groupchat=self.group_chat, llm_config=LLMConfig)
#
#     def load_agents(self, file: str = None, dictionary: dict = None):
#         if file:
#             agents_data = yaml.safe_load(Path(file).read_text())
#             #print(f"FILE DATA: {json.dumps(agents_data, indent=2)}")
#         elif dictionary:
#             agents_data = dictionary
#         else:
#             #print("Unable to load data")
#             return 1
#         self.agents = Agents.model_validate(agents_data)
#         return self.agents
#
#     def get_agents(self):
#         return self.agents
#
#     def reset_agents(self):
#         for agent_list in self.agents:
#             for agent in agent_list:
#                 agent.reset()
