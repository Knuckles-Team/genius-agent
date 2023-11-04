from typing import List, Dict, Optional, Callable
from pydantic import BaseModel


class LLMModel(BaseModel):
    model: str
    api_key: str
    api_base: str
    api_type: str
    api_version: Optional[str] = None


class FilterDict(BaseModel):
    model: List[str]


class Parameters(BaseModel):
    type: str
    properties: Dict[str, Dict[str, str]]
    required: List[str]


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
    seed: int
    temperature: float
    config_list: List[LLMModel]
    filter_dict: FilterDict
    request_timeout: int
    repeat_penalty: float
    functions: List[FunctionItem]
    function_map: FunctionMap