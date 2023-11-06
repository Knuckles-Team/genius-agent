# Genius Agents 

Deploy agents to solve problems using Autogen

This python library will accept an agent configuration file in YAML/JSON, or as a JSON String payload in CLI 
or as a standalone uvicorn FastAPI Server

This repository comes with a Dockerfile and a docker-compose.yml file to host this yourself.


## Run through CLI

```bash
python ./genius_autogen.py --prompt "Create Snake using Pygame" --file "./agent_configs.yml"
```


## Standalone API Server

```bash
uvicorn genius_agent_api:app --reload --host "0.0.0.0" --port 7999
```

## Agent Config in YAML

```yaml
---
agents:
  - name: admin
    system_message: A human admin. Interact with the planner to discuss the plan. Plan
      execution needs to be approved by this admin. Reply `TERMINATE` in the end when
      everything is done.
    llm_config:
      seed: 42
      temperature: 0.9
      config_list:
        - model: yarn-mistral-7b-128k.Q3_K_L
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - yarn-mistral-7b-128k.Q3_K_L
      request_timeout: 3600
      repeat_penalty: 1.1
    agent_type: user_proxy
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
  - name: engineer
    llm_config:
      seed: 42
      temperature: 0.9
      config_list:
        - model: llama-2-7b-chat.ggmlv3.q4_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
        - model: mistral-7b--instruct-v0.1.Q5_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - llama-2-7b-chat.ggmlv3.q4_K_S
          - mistral-7b--instruct-v0.1.Q5_K_S
      request_timeout: 3600
      repeat_penalty: 1.1
      functions:
        - name: python
          description: run arbitrary python and return the result
          parameters:
            type: object
            properties:
              cell:
                type: string
                description: Valid Python code to execute.
            required:
              - cell
        - name: bash
          description: run a shell script and return the execution result.
          parameters:
            type: object
            properties:
              script:
                type: string
                description: Valid shell script to execute
            required:
              - script
        - name: media_downloader
          description: run media-downloader to download a video or audio from the internet
          parameters:
            type: object
            properties:
              url:
                type: string
                description: Valid url to download
              audio:
                type: bool
                description: This optional argument is used if the link wants to be saved
                  as an mp3 or audio only
              directory:
                type: string
                description: Directory to save the video
            required:
              - url
        - name: write_to_file
          description: Use this function to write content to a file
          parameters:
            type: object
            properties:
              filename:
                type: string
                description: The filename to write to
              content:
                type: string
                description: The content to write
            required:
              - filename
              - content
        - name: read_from_file
          description: Use this function to read the content of a file
          parameters:
            type: object
            properties:
              filename:
                type: string
                description: The filename to read from
            required:
              - filename
        - name: read_pdf
          description: Use this function to read the content of a pdf file
          parameters:
            type: object
            properties:
              filename:
                type: string
                description: The filename to read from
            required:
              - filename
        - name: create_directory
          description: Use this function to create a directory
          parameters:
            type: object
            properties:
              directory_path:
                type: string
                description: The directory path to create
            required:
              - directory_path
      function_map:
        python: exec_python
        bash: exec_bash
        media_download: exec_media_downloader
        write_to_file: exec_write_to_file
        read_from_file: exec_read_from_file
        create_directory: exec_create_directory
    system_message: Engineer. You follow an approved plan. You write python/shell code
      to solve tasks. Wrap the code in a code block that specifies the script type.
      The user can't modify your code. So do not suggest incomplete code which requires
      others to modify. Don't use a code block if it's not intended to be executed by
      the executor. Don't include multiple code blocks in one response. Do not ask others
      to copy and paste the result. Check the execution result returned by the executor.
      If the result indicates there is an error, fix the error and output the code again.
      Suggest the full code instead of partial code or code changes. If the error can't
      be fixed or if the task is not solved even after the code is executed successfully,
      analyze the problem, revisit your assumption, collect additional info you need,
      and think of a different approach to try. Reply `TERMINATE` in the end when everything
      is done.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    agent_type: assistant
  - name: genius_engineer
    llm_config:
      seed: 42
      temperature: 0.9
      config_list:
        - model: gpt-4-32k-0314
          api_key: NA
          api_base: NA
          api_type: azure
          api_version: 2023-06-01-preview
      filter_dict:
        model:
          - gpt-4-32k-0314
      request_timeout: 3600
    system_message: Geniusbot Engineer. You are the engineer that developed the Python
      modules in the documents retrieved. Reply `TERMINATE` in the end when everything
      is done.
    human_input_mode: NEVER
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    max_consecutive_auto_reply: 10
    retrieve_config:
      task: code
      docs_path:
        - "https://raw.githubusercontent.com/Knuckles-Team/media-downloader/main/README.md"
        - "https://raw.githubusercontent.com/Knuckles-Team/repository-manager/main/README.md"
      get_or_create: true
      embedding_model: "all-mpnet-base-v2"
      chunk_token_size: 3000
      model: "gpt-4" # Only for determining token size: Options are: 32k 32000 , 16k for 16000 gpt-4 8000 or something else for 4000
    agent_type: retrieve_user_proxy
  - name: genius_learner
    llm_config:
      seed: 42
      temperature: 0.9
      config_list:
        - model: yarn-mistral-7b-128k.Q3_K_L
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - yarn-mistral-7b-128k.Q3_K_L
      request_timeout: 3600
    system_message: Critic. Double check plan, claims, code from other agents and provide
      feedback. "Check whether the plan includes adding verifiable info such as source
      URL. Reply `TERMINATE` in the end when everything is done.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    teach_config:
      verbosity: 0
      reset_db: true
      path_to_db_dir: "."
      recall_threshold: 1.5
    agent_type: teachable
```

## Agent Config in JSON

```JSON
{
  "agents": [
    {
      "name": "admin",
      "system_message": "A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin. Reply `TERMINATE` in the end when everything is done.",
      "llm_config": {
        "seed": 42,
        "temperature": 0.9,
        "config_list": [
          {
            "model": "yarn-mistral-7b-128k.Q3_K_L",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "yarn-mistral-7b-128k.Q3_K_L"
          ]
        },
        "request_timeout": 3600,
        "repeat_penalty": 1.1
      },
      "agent_type": "user_proxy",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()"
    },
    {
      "name": "engineer",
      "llm_config": {
        "seed": 42,
        "temperature": 0.9,
        "config_list": [
          {
            "model": "llama-2-7b-chat.ggmlv3.q4_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          },
          {
            "model": "mistral-7b--instruct-v0.1.Q5_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "llama-2-7b-chat.ggmlv3.q4_K_S",
            "mistral-7b--instruct-v0.1.Q5_K_S"
          ]
        },
        "request_timeout": 3600,
        "repeat_penalty": 1.1,
        "functions": [
          {
            "name": "python",
            "description": "run arbitrary python and return the result",
            "parameters": {
              "type": "object",
              "properties": {
                "cell": {
                  "type": "string",
                  "description": "Valid Python code to execute."
                }
              },
              "required": [
                "cell"
              ]
            }
          },
          {
            "name": "bash",
            "description": "run a shell script and return the execution result.",
            "parameters": {
              "type": "object",
              "properties": {
                "script": {
                  "type": "string",
                  "description": "Valid shell script to execute"
                }
              },
              "required": [
                "script"
              ]
            }
          },
          {
            "name": "media_downloader",
            "description": "run media-downloader to download a video or audio from the internet",
            "parameters": {
              "type": "object",
              "properties": {
                "url": {
                  "type": "string",
                  "description": "Valid url to download"
                },
                "audio": {
                  "type": "bool",
                  "description": "This optional argument is used if the link wants to be saved as an mp3 or audio only"
                },
                "directory": {
                  "type": "string",
                  "description": "Directory to save the video"
                }
              },
              "required": [
                "url"
              ]
            }
          },
          {
            "name": "write_to_file",
            "description": "Use this function to write content to a file",
            "parameters": {
              "type": "object",
              "properties": {
                "filename": {
                  "type": "string",
                  "description": "The filename to write to"
                },
                "content": {
                  "type": "string",
                  "description": "The content to write"
                }
              },
              "required": [
                "filename",
                "content"
              ]
            }
          },
          {
            "name": "read_from_file",
            "description": "Use this function to read the content of a file",
            "parameters": {
              "type": "object",
              "properties": {
                "filename": {
                  "type": "string",
                  "description": "The filename to read from"
                }
              },
              "required": [
                "filename"
              ]
            }
          },
          {
            "name": "read_pdf",
            "description": "Use this function to read the content of a pdf file",
            "parameters": {
              "type": "object",
              "properties": {
                "filename": {
                  "type": "string",
                  "description": "The filename to read from"
                }
              },
              "required": [
                "filename"
              ]
            }
          },
          {
            "name": "create_directory",
            "description": "Use this function to create a directory",
            "parameters": {
              "type": "object",
              "properties": {
                "directory_path": {
                  "type": "string",
                  "description": "The directory path to create"
                }
              },
              "required": [
                "directory_path"
              ]
            }
          }
        ],
        "function_map": {
          "python": "exec_python",
          "bash": "exec_bash",
          "media_download": "exec_media_downloader",
          "write_to_file": "exec_write_to_file",
          "read_from_file": "exec_read_from_file",
          "create_directory": "exec_create_directory"
        }
      },
      "system_message": "Engineer. You follow an approved plan. You write python/shell code to solve tasks. Wrap the code in a code block that specifies the script type. The user can't modify your code. So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor. Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. Check the execution result returned by the executor. If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try. Reply `TERMINATE` in the end when everything is done.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "assistant"
    },
    {
      "name": "genius_engineer",
      "llm_config": {
        "seed": 42,
        "temperature": 0.9,
        "config_list": [
          {
            "model": "gpt-4-32k-0314",
            "api_key": "NA",
            "api_base": "NA",
            "api_type": "azure",
            "api_version": "2023-06-01-preview"
          }
        ],
        "filter_dict": {
          "model": [
            "gpt-4-32k-0314"
          ]
        },
        "request_timeout": 3600
      },
      "system_message": "Geniusbot Engineer. You are the engineer that developed the Python modules in the documents retrieved. Reply `TERMINATE` in the end when everything is done.",
      "human_input_mode": "NEVER",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "max_consecutive_auto_reply": 10,
      "retrieve_config": {
        "task": "code",
        "docs_path": [
          "https://raw.githubusercontent.com/Knuckles-Team/media-downloader/main/README.md",
          "https://raw.githubusercontent.com/Knuckles-Team/repository-manager/main/README.md"
        ],
        "get_or_create": true,
        "embedding_model": "all-mpnet-base-v2",
        "chunk_token_size": 3000,
        "model": "gpt-4"
      },
      "agent_type": "retrieve_user_proxy"
    },
    {
      "name": "genius_learner",
      "llm_config": {
        "seed": 42,
        "temperature": 0.9,
        "config_list": [
          {
            "model": "yarn-mistral-7b-128k.Q3_K_L",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "yarn-mistral-7b-128k.Q3_K_L"
          ]
        },
        "request_timeout": 3600
      },
      "system_message": "Critic. Double check plan, claims, code from other agents and provide feedback. \"Check whether the plan includes adding verifiable info such as source URL. Reply `TERMINATE` in the end when everything is done.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "teach_config": {
        "verbosity": 0,
        "reset_db": true,
        "path_to_db_dir": ".",
        "recall_threshold": 1.5
      },
      "agent_type": "teachable"
    }
  ]
}
```
