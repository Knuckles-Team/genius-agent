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
    config_list: List[LLMModel]
    filter_dict: Optional[FilterDict]
    request_timeout: Optional[int]
    repeat_penalty: Optional[float]
    functions: Optional[List[FunctionItem]]
    function_map: Optional[FunctionMap]

    def __init__(self, **data: Any):

        super().__init__(**data)

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
