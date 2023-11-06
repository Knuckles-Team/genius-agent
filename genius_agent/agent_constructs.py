from typing import List, Dict, Optional, Callable, Union
from pydantic import BaseModel, field_validator, model_validator
import json
import yaml
from pathlib import Path
from autogen import (AssistantAgent,
                     UserProxyAgent,
                     GroupChat,
                     GroupChatManager)
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent


######################## Pydantic Classes for Models (Injesting YAML/JSON and Serving Models for API/CLI)###############

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

    @field_validator("function_map")
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
class AgentConfig(BaseModel):
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

    @field_validator("is_termination_msg")
    def convert_to_callable(cls, value):
        if isinstance(value, str):
            try:
                converted_callables = eval(value)
            except Exception:
                raise ValueError(f"Invalid callable string for value '{value}'")
        elif isinstance(value, Callable):
            converted_callables = value
        else:
            raise ValueError(f"Invalid type for value '{value}', expected a string or callable")
        return converted_callables

    @field_validator("retrieve_config")
    def validate_retrieve_config(cls, value):
        if isinstance(value, RetrieveConfig):
            try:
                retrieve_config = RetrieveConfig.model_validate(value)
            except Exception:
                raise ValueError(f"Invalid retrieve_config '{value}'")
        elif isinstance(value, RetrieveConfig):
            retrieve_config = value
        else:
            raise ValueError(f"Invalid type for retrieve_config '{value}', expected a dict with contents of retrieve_config")
        print(f"VALID RETRIEVE CONFIG: {retrieve_config}")
        return retrieve_config

    @field_validator("teach_config")
    def validate_teach_config(cls, value):
        if isinstance(value, TeachConfig):
            try:
                teach_config = TeachConfig.model_validate(value)
            except Exception:
                raise ValueError(f"Invalid teach_config '{value}'")
        elif isinstance(value, TeachConfig):
            teach_config = value
        else:
            raise ValueError(f"Invalid type for teach_config '{value}', expected a dict with contents of teach_config")
        print(f"VALID TEACH CONFIG: {teach_config}")
        return teach_config


class AgentsConfig(BaseModel):
    agents: List[AgentConfig]

######################## Python Agents Class with Autogen Models #######################################################

class Agents:
    def __init__(self):
        self.agents_config = None
        self.agents = None
        self.chat_initiator = None
        self.group_chat = None
        self.group_chat_manager = None

    def set_chat_initiator(self, name):
        self.chat_initiator = self.find_agent(name)

    def load_config(self, file: str = None, payload: dict = None):
        if file is not None:
            agents_data = yaml.safe_load(Path(file).read_text())
        else:
            agents_data = payload
        self.agents_config = AgentsConfig.model_validate(agents_data)

    def load_agents(self):
        loaded_agents = []
        # print(f"AGENTS: {agents}")
        for agent_config in self.agents_config.agents:
            print(f"AGENT: {agent_config}")
            if agent_config.agent_type == "user_proxy":
                agent = UserProxyAgent(
                    name=agent_config.name,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    human_input_mode=agent_config.human_input_mode or None,
                    system_message=agent_config.system_message or None,
                    code_execution_config=agent_config.code_execution_config or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "assistant":
                agent = AssistantAgent(
                    name=agent_config.name,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.system_message or None,
                    code_execution_config=agent_config.code_execution_config or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "retrieve_user_proxy":
                #print(f"\n\nRETRIEVE_CONFIG MODEL DUMP: {agent_config.retrieve_config}")
                agent = RetrieveUserProxyAgent(
                    name=agent_config.name,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.system_message or None,
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
                    system_message=agent_config.system_message or None,
                    llm_config=agent_config.llm_config,
                )
                loaded_agents.append(agent)
            elif agent_config.agent_type == "teachable":
                agent = TeachableAgent(
                    name=agent_config.name or None,
                    is_termination_msg=agent_config.is_termination_msg or None,
                    system_message=agent_config.system_message or None,
                    llm_config=agent_config.llm_config,
                    teach_config=agent_config.teach_config.model_dump() or None
                )
                loaded_agents.append(agent)
        self.agents = loaded_agents
        return loaded_agents

    def load_group_chat(self):
        self.group_chat = GroupChat(agents=self.agents, messages=[], max_round=12)
        print(f"LLMCONFIG: {self.chat_initiator.llm_config}")
        self.group_chat_manager = GroupChatManager(groupchat=self.group_chat, llm_config=self.chat_initiator.llm_config)

    def find_agent(self, name):
        for agent in self.agents:
            print(f"NAMES: {agent.name}")
            if agent.name == name:
                print(f"MATCH: {agent.name}")
                return agent

    def find_agent_config(self, name):
        for agent_config in self.agents_config.agents:
            print(f"NAMES: {agent_config.name}")
            if agent_config.name == name:
                print(f"MATCH: {agent_config.name}")
                return agent_config
