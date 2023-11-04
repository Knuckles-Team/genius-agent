from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent
import yaml
from pathlib import Path
from llm_config_structs import LLMConfig

termination_msg = lambda x: isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

llm_config_data = yaml.safe_load(Path('../config_examples/llm_configs.yml').read_text())
llm_config = LLMConfig.parse_obj(llm_config_data)

admin_user_proxy = UserProxyAgent(
    name="Admin",
    system_message="A human admin. Interact with the planner to discuss the plan. "
                   "Plan execution needs to be approved by this admin. "
                   "Reply `TERMINATE` in the end when everything is done."
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "coding"},
    human_input_mode="NEVER",
    is_termination_msg=termination_msg,
    max_consecutive_auto_reply=10,
)

engineer = AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message='''Engineer. You follow an approved plan. You write python/shell code to solve tasks. 
Wrap the code in a code block that specifies the script type. The user can't modify your code. 
So do not suggest incomplete code which requires others to modify. 
Don't use a code block if it's not intended to be executed by the executor.
Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. 
Check the execution result returned by the executor.
If the result indicates there is an error, fix the error and output the code again. 
Suggest the full code instead of partial code or code changes. 
If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
Reply `TERMINATE` in the end when everything is done.
''',
    is_termination_msg=termination_msg,
)
scientist = AssistantAgent(
    name="Scientist",
    llm_config=llm_config,
    system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their abstracts printed. You don't write code.""",
    is_termination_msg=termination_msg,
)
planner = AssistantAgent(
    name="Planner",
    system_message='''Planner. Suggest a plan. Revise the plan based on feedback from admin, critic, and aid, until admin approval.
The plan may involve an engineer who can write code and a scientist who doesn't write code.
Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
Reply `TERMINATE` in the end when everything is done.
''',
    llm_config=llm_config,
    is_termination_msg=termination_msg,
)
executor = UserProxyAgent(

    name="Executor",
    system_message="Executor. Execute the code written by the engineer and report the result. "
                   "Reply `TERMINATE` in the end when everything is done.",
    human_input_mode="NEVER",
    code_execution_config={"last_n_messages": 3, "work_dir": "paper"},
    is_termination_msg=termination_msg,
)
critic = AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. "
                   "Check whether the plan includes adding verifiable info such as source URL. "
                   "Reply `TERMINATE` in the end when everything is done.",
    llm_config=llm_config,
    is_termination_msg=termination_msg,
)
geniusbot = RetrieveAssistantAgent(
    name="Geniusbot",
    system_message="Geniusbot. You can perform any tasks in media-downloader python library. "
                   "This library allows you to download videos from the internet or download them as audio only."
                   "Reply `TERMINATE` in the end when everything is done.",
    llm_config=llm_config,
    is_termination_msg=termination_msg,
)
geniusbot_qa = RetrieveUserProxyAgent(
    name="Geniusbot Assistant",
    human_input_mode="NEVER",
    is_termination_msg=termination_msg,
    max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "qa",
        "docs_path": "https://raw.githubusercontent.com/Knuckles-Team/media-downloader/main/README.md",
    },
)

geniusbot_learn = TeachableAgent(
    name="Geniusbot Assimilator",
    llm_config=llm_config,
    teach_config={
        "verbosity": 0,
        "reset_db": True,
        # "path_to_db_dir": ".",
        "recall_threshold": 1.5,
    }
)

boss = UserProxyAgent(
    name="Boss",
    is_termination_msg=termination_msg,
    human_input_mode="TERMINATE",
    system_message="The boss who ask questions and give tasks. Reply `TERMINATE` in the end when everything is done.",
    code_execution_config=False,  # we don't want to execute code in this case.
)

boss_aid = RetrieveUserProxyAgent(
    name="Boss_Assistant",
    is_termination_msg=termination_msg,
    system_message="Assistant who has extra content retrieval power for the related function calls available to agents. Reply `TERMINATE` in the end when everything is done.",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=3,
    retrieve_config={
        "task": "code",
        "docs_path": [
            "https://raw.githubusercontent.com/Knuckles-Team/media-downloader/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/media-downloader/main/media_downloader/media_downloader.py",
            "https://raw.githubusercontent.com/Knuckles-Team/repository-manager/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/repository-manager/main/repository_manager/repository_manager.py",
            "https://raw.githubusercontent.com/Knuckles-Team/subshift/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/subshift/main/subshift/subshift.py",
            "https://raw.githubusercontent.com/Knuckles-Team/webarchiver/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/webarchiver/main/webarchiver/webarchiver.py",
            "https://raw.githubusercontent.com/Knuckles-Team/audio-transcriber/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/audio-transcriber/main/audio_transcriber/audio_transcriber.py",
            "https://raw.githubusercontent.com/Knuckles-Team/media-manager/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/media-manager/main/media_manager/media_manager.py",
            "https://raw.githubusercontent.com/Knuckles-Team/systems-manager/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/systems-manager/main/systems_manager/systems_manager.py",
            "https://raw.githubusercontent.com/Knuckles-Team/servicenow-api/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/servicenow-api/main/servicenow_api/servicenow_api.py",
            "https://raw.githubusercontent.com/Knuckles-Team/report-manager/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/report-manager/main/report_manager/report_manager.py",
            "https://raw.githubusercontent.com/Knuckles-Team/barchart-api/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/barchart-api/main/barchart_api/barchart_api.py",
            "https://raw.githubusercontent.com/Knuckles-Team/gitlab-api/main/README.md",
            # "https://raw.githubusercontent.com/Knuckles-Team/gitlab-api/main/gitlab_api/gitlab_api.py",
        ],
        "chunk_token_size": 8000,
        "model": config_list[0]["model"],
        # "client": chromadb.PersistentClient(path="/tmp/chromadb"),
        "collection_name": "groupchat",
        "get_or_create": True,
    },
    code_execution_config=False,  # we don't want to execute code in this case.
)

media_downloader_assistant = RetrieveAssistantAgent(
    name="media_downloader_assistant",
    system_message="You are a helpful assistant that will use the media_downloader function call to download content from YouTube, Rumble, Twitter, or other platforms as video or audio. Reply `TERMINATE` in the end when everything is done.",
    llm_config={
        "request_timeout": 600,
        "seed": 42,
        "config_list": config_list,
    },
)

aid = RetrieveUserProxyAgent(
    name="aid",
    is_termination_msg=termination_msg,
    system_message="Assistant who has extra content retrieval power for solving difficult problems. Reply `TERMINATE` in the end when everything is done.",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=3,
    retrieve_config={
        "task": "code",
        "docs_path": [
            "https://raw.githubusercontent.com/Knuckles-Team/media-downloader/main/README.md"
        ],
        "chunk_token_size": 8000,
        "model": config_list[0]["model"],
        # "client": chromadb.PersistentClient(path="/tmp/chromadb"),
        "collection_name": "groupchat",
        "get_or_create": True,
    },
    code_execution_config=False,  # we don't want to execute code in this case.
)

coder = AssistantAgent(
    name="Senior_Python_Engineer",
    is_termination_msg=termination_msg,
    system_message="You are a senior python engineer. "
                   "Reply `TERMINATE` in the end when everything is done.",
    llm_config=llm_config,
)

pm = AssistantAgent(
    name="Product_Manager",
    is_termination_msg=termination_msg,
    system_message="You are a product manager. "
                   "Reply `TERMINATE` in the end when everything is done.",
    llm_config=llm_config,
)

reviewer = AssistantAgent(
    name="Code_Reviewer",
    is_termination_msg=termination_msg,
    system_message="You are a code reviewer. You will review the code for accuracy, precision, security "
                   "vulnerabilities, syntax, and optimization. Reply `TERMINATE` in the end when everything is done.",
    llm_config=llm_config,
)

from IPython import get_ipython


def exec_python(cell):
    # p = Popen(["python", "-c", f"{code}"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # log = str(p.returncode)
    ipython = get_ipython()
    result = ipython.run_cell(cell)
    log = str(result.result)
    if result.error_before_exec is not None:
        log += f"\n{result.error_before_exec}"
    if result.error_in_exec is not None:
        log += f"\n{result.error_in_exec}"
    return log


def exec_bash(script):
    return user_proxy.execute_code_blocks([("sh", script)])


from media_downloader import MediaDownloader


def exec_media_downloader(url, directory, audio=False):
    video_downloader_instance = MediaDownloader()
    video_downloader_instance.append_link(url)
    video_downloader_instance.set_save_path(directory)
    video_downloader_instance.set_audio(audio=audio)
    return user_proxy.execute_function(func_call=video_downloader_instance.download_all())


def exec_write_to_file(filename: str, content: str) -> str:
    with open(filename,'w') as f:
        f.write(content)
    return "file created successfully"

def exec_read_from_file(filename: str,) -> str:
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

def exec_create_directory(directory_path: str) -> str:
    import os
    path = directory_path
    if not os.path.exists(directory_path):
        path = os.makedirs(directory_path)
    return path


user_proxy.register_function(
    function_map={
        "python": exec_python,
        "bash": exec_bash,
        "media_download": exec_media_downloader,
        "write_to_file": exec_write_to_file,
        "read_from_file": exec_read_from_file,
        "create_directory": exec_create_directory,
    }
)

groupchat = GroupChat(agents=[user_proxy, engineer, scientist, planner, executor, critic], messages=[], max_round=50)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)
