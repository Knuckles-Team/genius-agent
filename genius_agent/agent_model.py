#!/usr/bin/env python
# coding: utf-8

import glob
import os
from typing import List, Dict, Optional, Callable, Union
from pydantic import BaseModel, field_validator, model_validator
from agent_functions import *  # Used for all dynamically loaded agent functions


# Pydantic Classes for Models (Ingesting YAML/JSON and Serving Models for API/CLI)
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


class ToolItem(BaseModel):
    type: str
    function: str


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
    functions_directory: Optional[str]  # Directory to load custom python functions for agent
    functions: Optional[List[FunctionItem]]  # Autogen Functions
    tools: Optional[List[ToolItem]]  # OpenAI Functions
    function_map: Optional[FunctionMap]


    @field_validator("functions_directory")
    def get_custom_functions(cls, value):
        python_files = glob.glob(os.path.join(value, "*.py"))
        # Import each module dynamically
        for python_file in python_files:
            # Extract the module name from the file path
            module_name = os.path.splitext(os.path.basename(python_file))[0]
            # Import the module
            try:
                module = __import__(module_name)
                globals()[module_name] = module
            except ImportError as e:
                print(f"Error importing module {module_name}: {e}")
        return python_files

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
    assistant_id: Optional[str] = None
    llm_config: Optional[Union[LLMConfig, dict]] = None
    chat_initiator: Optional[bool] = False
    instructions: Optional[str] = None
    is_termination_msg: Optional[str] = None
    human_input_mode: Optional[str] = "NEVER"
    max_consecutive_auto_reply: Optional[int] = 10
    code_execution_config: Optional[CodeExecutionConfig] = None
    retrieve_config: Optional[RetrieveConfig] = None  # Autogen RAG
    file_ids: Optional[List[str]] = None  # OpenAI RAG - File IDs from OpenAI Account
    teach_config: Optional[TeachConfig] = None
    human: Optional[str] = None
    persona: Optional[str] = None
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
            raise ValueError(
                f"Invalid type for retrieve_config '{value}', expected a dict with contents of retrieve_config")
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
