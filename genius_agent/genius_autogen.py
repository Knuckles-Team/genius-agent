import os
import autogen
from agent_constructs import Manager

autogen.ChatCompletion.start_logging()


def chat(prompt="Build snake game using pygame"):
    #agents_instance = Agents(file="./config_examples/agent_configs.yml")
    #agents = agents_instance.get_all_agents()
    manager = Manager(file=f'{os.path.realpath(os.path.dirname(__file__))}/agent_configs.yml')
    manager.agents.Admin.initiate_chat(
        manager.manager,
        message=prompt,
    )

chat(prompt="Build snake game using pygame")
