from typing import List, Dict, Optional, Callable, Union
from pydantic import BaseModel, field_validator, validator


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


class Agents(BaseModel):
    agents: List[Agent]
