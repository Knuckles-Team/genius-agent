# Genius Agent

![PyPI - Version](https://img.shields.io/pypi/v/genius-agent)
![PyPI - Downloads](https://img.shields.io/pypi/dd/genius-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/genius-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/genius-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/genius-agent)
![PyPI - License](https://img.shields.io/pypi/l/genius-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/genius-agent)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/genius-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/genius-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/genius-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/genius-agent)

![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/genius-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/genius-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/genius-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/genius-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/genius-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/genius-agent)

*Version: 2.6.0*

Deploy agents to solve problems using Autogen

This python library will accept an agent configuration file in YAML/JSON, or as a JSON String payload in CLI 
or as a standalone uvicorn FastAPI Server

This repository comes with a Dockerfile and a docker-compose.yml file to host this yourself.

Agent Types:
- Assistant
- User Proxy
- Retrieve Assistant
- Retrieve User Proxy
- Teachable
- MemGPT
- GPT Assistant
- Multimodal Assistant

<details>
  <summary><b>Usage:</b></summary>

### CLI
| Short Flag | Long Flag | Description                                     |
|------------|-----------|-------------------------------------------------|
| -h         | --help    | See Usage                                       |
| -f         | --file    | YAML/JSON file for agent configurations to load |
| -d         | --data    | JSON data for agent configurations to load      |
| -p         | --prompt  | Prompt for chat conversation                    |

### API Endpoints
| Method | Endpoint           | Parameters | Payload                                       | Description                           |
|--------|--------------------|------------|-----------------------------------------------|---------------------------------------| 
| GET    | /api/health        |            |                                               | Health of API Server                  |
| GET    | /api/agents/{name} | name       |                                               | Get Agent configuration by name       |
| GET    | /api/agents        |            |                                               | Get all Agent configurations          | 
| POST   | /api/agents        |            | {"name": "agent_name", "llm_config": {...}}   | Load agent configurations             | 
| POST   | /api/chat/         | prompt     | {"prompt": "This is a prompt for the agents"} | Prompt the agents provided            | 

</details>

<details>
  <summary><b>Example:</b></summary>

### CLI Example
```bash
genius-agent --prompt "Create Snake using Pygame" --file "./agent_configs.yml"
```

<details>
  <summary><b>Agent Config in YAML:</b></summary>

```yaml
---
agents:
  - name: user_proxy
    code_execution_config:
      work_dir: coding
      user_docker: false
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: mistral-7b-instruct-v0.1.Q4_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - mistral-7b-instruct-v0.1.Q4_K_S
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
    human_input_mode: NEVER # Never - Never wait for human input, Alawys - Always waits for input from user before AI begins, Terminate - Wait for input for user when conversation terminates
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    max_consecutive_auto_reply: 10
    agent_type: user_proxy

  - name: validator
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: mistral-7b-instruct-v0.1.Q4_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - mistral-7b-instruct-v0.1.Q4_K_S
      request_timeout: 3600
      repeat_penalty: 1.1
      functions:
      function_map:
    instructions: Validator. Execute the code written by the engineer and report the
      result. Reply `TERMINATE` in the end when everything is done.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    agent_type: user_proxy

  - name: engineer
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: mistral-7b-instruct-v0.1.Q4_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - mistral-7b-instruct-v0.1.Q4_K_S
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
    instructions: Engineer. You follow an approved plan. You write python/shell code
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

  - name: financial_advisor
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: mistral-7b-instruct-v0.1.Q4_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - mistral-7b-instruct-v0.1.Q4_K_S
      request_timeout: 3600
      repeat_penalty: 1.1
      functions:
        - name: get_stock_price
          description: Get the latest closing price of a stock using its ticker symbol
          parameters:
            type: object
            properties:
              cell:
                type: string
                description: The ticker symbol of the stock
            required:
              - symbol
      function_map:
        get_stock_price: exec_get_stock_price
    instructions: Scientist. You follow an approved plan. You are able to categorize
      papers after seeing their abstracts printed. You don't write code.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    agent_type: assistant

  - name: planner
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: mistral-7b-instruct-v0.1.Q4_K_S
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - mistral-7b-instruct-v0.1.Q4_K_S
      request_timeout: 3600
      repeat_penalty: 1.1
      functions:
      function_map:
    instructions: Planner. Suggest a plan. Revise the plan based on feedback from
      admin, critic, and aid, until admin approval. The plan may involve an engineer
      who can write code and a scientist who doesn't write code. Explain the plan first.
      Be clear which step is performed by an engineer, and which step is performed by
      a scientist. Reply `TERMINATE` in the end when everything is done.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    agent_type: assistant

  - name: retrieve_engineer
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: yarn-mistral-7b-128k.Q3_K_L
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
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
        - model: TheBloke/WizardLM-13B-V1.2-GGML/wizardlm-13b-v1.2.ggmlv3.q2_K.bin
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
        - model: codellama-7b-instruct
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
        - model: gpt-4-32k
          api_key: NA
        - model: gpt-4-32k
          api_key: NA
          api_base: NA
          api_type: azure
          api_version: 2023-06-01-preview
        - model: gpt-4-32k-0314
          api_key: NA
          api_base: NA
          api_type: azure
          api_version: 2023-06-01-preview
      filter_dict:
        model:
          - yarn-mistral-7b-128k.Q3_K_L
          - llama-2-7b-chat.ggmlv3.q4_K_S
          - mistral-7b--instruct-v0.1.Q5_K_S
          - TheBloke/WizardLM-13B-V1.2-GGML/wizardlm-13b-v1.2.ggmlv3.q2_K.bin
          - mistral-7b-instruct-v0.1.Q8_0
          - codellama-7b-instruct
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
    instructions: Geniusbot Engineer. You are the engineer that developed the Python
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

  - name: retrieve_assistant
    llm_config:
      seed: 42
      temperature: 0
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
      functions:
      function_map:
    instructions: Retrieve assistant. You are in charge of providing information to the other agents relevant to the task at hand.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    agent_type: retrieve_assistant

  - name: teachable_assistant
    llm_config:
      seed: 42
      temperature: 0
      config_list:
        - model: codellama-7b-instruct
          api_key: NA
          api_base: http://localhost:8080/v1
          api_type: openai
          api_version: v1
      filter_dict:
        model:
          - codellama-7b-instruct
      request_timeout: 3600
      repeat_penalty: 1.1
      functions:
      function_map:
    instructions: Critic. Double check plan, claims, code from other agents and provide
      feedback. "Check whether the plan includes adding verifiable info such as source
      URL. Reply `TERMINATE` in the end when everything is done.
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    teach_config:
      verbosity: 0
      reset_db: true
      path_to_db_dir: "."
      recall_threshold: 1.5
    agent_type: teachable

  - name: gpt_assistant
    llm_config:
      seed: 42
      temperature: 0
      assistant_id: ""
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
      tools:
        - type: "function"
          function: ossinsight_api_schema
      function_map:
        get_oss_insights: exec_get_ossinsight
    instructions: Hello, Open Source Project Analyst. You'll conduct comprehensive evaluations of open source projects 
      or organizations on the GitHub platform, 
      analyzing project trajectories, contributor engagements, open source trends, and other vital parameters. 
      Please carefully read the context of the conversation to identify the current analysis question or problem that needs add
    is_termination_msg: 'lambda x: isinstance(x, dict) and x.get("content") is not None and "TERMINATE" == str(x.get("content", ""))[-9:].upper()'
    agent_type: gpt_assistant


```


</details>


<details>
  <summary><b>Agent Config in JSON:</b></summary>

```json
{
  "agents": [
    {
      "name": "user_proxy",
      "code_execution_config": {
        "work_dir": "coding",
        "user_docker": false
      },
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "mistral-7b-instruct-v0.1.Q4_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "mistral-7b-instruct-v0.1.Q4_K_S"
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
      "human_input_mode": "NEVER",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "max_consecutive_auto_reply": 10,
      "agent_type": "user_proxy"
    },
    {
      "name": "validator",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "mistral-7b-instruct-v0.1.Q4_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "mistral-7b-instruct-v0.1.Q4_K_S"
          ]
        },
        "request_timeout": 3600,
        "repeat_penalty": 1.1,
        "functions": null,
        "function_map": null
      },
      "instructions": "Validator. Execute the code written by the engineer and report the result. Reply `TERMINATE` in the end when everything is done.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "user_proxy"
    },
    {
      "name": "engineer",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "mistral-7b-instruct-v0.1.Q4_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "mistral-7b-instruct-v0.1.Q4_K_S"
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
      "instructions": "Engineer. You follow an approved plan. You write python/shell code to solve tasks. Wrap the code in a code block that specifies the script type. The user can't modify your code. So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor. Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. Check the execution result returned by the executor. If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try. Reply `TERMINATE` in the end when everything is done.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "assistant"
    },
    {
      "name": "financial_advisor",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "mistral-7b-instruct-v0.1.Q4_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "mistral-7b-instruct-v0.1.Q4_K_S"
          ]
        },
        "request_timeout": 3600,
        "repeat_penalty": 1.1,
        "functions": [
          {
            "name": "get_stock_price",
            "description": "Get the latest closing price of a stock using its ticker symbol",
            "parameters": {
              "type": "object",
              "properties": {
                "cell": {
                  "type": "string",
                  "description": "The ticker symbol of the stock"
                }
              },
              "required": [
                "symbol"
              ]
            }
          }
        ],
        "function_map": {
          "get_stock_price": "exec_get_stock_price"
        }
      },
      "instructions": "Scientist. You follow an approved plan. You are able to categorize papers after seeing their abstracts printed. You don't write code.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "assistant"
    },
    {
      "name": "planner",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "mistral-7b-instruct-v0.1.Q4_K_S",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "mistral-7b-instruct-v0.1.Q4_K_S"
          ]
        },
        "request_timeout": 3600,
        "repeat_penalty": 1.1,
        "functions": null,
        "function_map": null
      },
      "instructions": "Planner. Suggest a plan. Revise the plan based on feedback from admin, critic, and aid, until admin approval. The plan may involve an engineer who can write code and a scientist who doesn't write code. Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist. Reply `TERMINATE` in the end when everything is done.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "assistant"
    },
    {
      "name": "retrieve_engineer",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "yarn-mistral-7b-128k.Q3_K_L",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          },
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
          },
          {
            "model": "TheBloke/WizardLM-13B-V1.2-GGML/wizardlm-13b-v1.2.ggmlv3.q2_K.bin",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          },
          {
            "model": "codellama-7b-instruct",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          },
          {
            "model": "gpt-4-32k",
            "api_key": "NA"
          },
          {
            "model": "gpt-4-32k",
            "api_key": "NA",
            "api_base": "NA",
            "api_type": "azure",
            "api_version": "2023-06-01-preview"
          },
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
            "yarn-mistral-7b-128k.Q3_K_L",
            "llama-2-7b-chat.ggmlv3.q4_K_S",
            "mistral-7b--instruct-v0.1.Q5_K_S",
            "TheBloke/WizardLM-13B-V1.2-GGML/wizardlm-13b-v1.2.ggmlv3.q2_K.bin",
            "mistral-7b-instruct-v0.1.Q8_0",
            "codellama-7b-instruct"
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
      "instructions": "Geniusbot Engineer. You are the engineer that developed the Python modules in the documents retrieved. Reply `TERMINATE` in the end when everything is done.",
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
      "name": "retrieve_assistant",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
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
        "repeat_penalty": 1.1,
        "functions": null,
        "function_map": null
      },
      "instructions": "Retrieve assistant. You are in charge of providing information to the other agents relevant to the task at hand.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "retrieve_assistant"
    },
    {
      "name": "teachable_assistant",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "config_list": [
          {
            "model": "codellama-7b-instruct",
            "api_key": "NA",
            "api_base": "http://localhost:8080/v1",
            "api_type": "openai",
            "api_version": "v1"
          }
        ],
        "filter_dict": {
          "model": [
            "codellama-7b-instruct"
          ]
        },
        "request_timeout": 3600,
        "repeat_penalty": 1.1,
        "functions": null,
        "function_map": null
      },
      "instructions": "Critic. Double check plan, claims, code from other agents and provide feedback. \"Check whether the plan includes adding verifiable info such as source URL. Reply `TERMINATE` in the end when everything is done.",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "teach_config": {
        "verbosity": 0,
        "reset_db": true,
        "path_to_db_dir": ".",
        "recall_threshold": 1.5
      },
      "agent_type": "teachable"
    },
    {
      "name": "gpt_assistant",
      "llm_config": {
        "seed": 42,
        "temperature": 0,
        "assistant_id": "",
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
        "request_timeout": 3600,
        "tools": [
          {
            "type": "function",
            "function": "ossinsight_api_schema"
          }
        ],
        "function_map": {
          "get_oss_insights": "exec_get_ossinsight"
        }
      },
      "instructions": "Hello, Open Source Project Analyst. You'll conduct comprehensive evaluations of open source projects or organizations on the GitHub platform, analyzing project trajectories, contributor engagements, open source trends, and other vital parameters. Please carefully read the context of the conversation to identify the current analysis question or problem that needs add",
      "is_termination_msg": "lambda x: isinstance(x, dict) and x.get(\"content\") is not None and \"TERMINATE\" == str(x.get(\"content\", \"\"))[-9:].upper()",
      "agent_type": "gpt_assistant"
    }
  ]
}

```            


</details>

### Standalone API Server

```bash
uvicorn genius_agent_api:app --reload --host "0.0.0.0" --port 7999
```

Test server

```bash
curl --header "Content-Type: application/json" --request POST --data '{"prompt":"Write a game in python"}'  http://localhost:3001/api/chat
```

### Docker API Server

Dockerfile

```dockerfile
FROM python:3.11.6-slim-bookworm AS base
RUN apt update && apt upgrade -y && pip install --upgrade pip
RUN pip install --upgrade genius-agent[rag,openai,chromadb,pgvector,api,memgpt]
CMD ["uvicorn", "genius_agent_api:app", "--reload", "--host", "0.0.0.0", "--port", "7999"]
```

docker-compose.yml

```yaml
---
version: '3.9'

services:
  genius-agent:
    build: .
    container_name: genius-agent
    hostname: genius-agent
    restart: unless-stopped
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    environment:
      - VIRTUAL_HOST=genius-agent.com  # NGINX Reverse Proxy
      - VIRTUAL_PORT=7999
    ports:
      - "7999:7999"
```

Run: 

```bash
docker compose up --build -d
```

### Execute API Call
```bash
curl -vX POST http://localhost:7999/agents_config/load -d @agent_configs.json --header "Content-Type: application/json"
```

</details>

<details>
  <summary><b>Installation Instructions:</b></summary>

Core dependencies
```bash
python -m pip install genius-agent
```

All dependencies
```bash
python -m pip install genius-agent[rag,openai,chromadb,pgvector,api,memgpt]
```

</details>

<details>
  <summary><b>Repository Owners:</b></summary>


<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)
</details>


Credits to OpenAI and Microsoft for usage in project!