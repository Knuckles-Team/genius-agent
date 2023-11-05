import autogen
from structs.agent_structs import Manager, GroupChat, Agents

autogen.ChatCompletion.start_logging()


def chat(prompt="Build snake game using pygame"):
    agents_instance = Agents(file="./config_examples/agent_configs.yml")
    agents = agents_instance.get_all_agents()
    agents.Admin.initiate_chat(
        agents_instance.manager,
        message=prompt,
    )


chat(prompt="Build snake game using pygame")
