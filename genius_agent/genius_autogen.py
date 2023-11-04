import autogen
import yaml
import yaml
from pathlib import Path
# from structs.llm_config_structs import LLMConfig
from structs.agent_structs import Manager, Agents
import json

# # Load LLM Configuration Data from YAML file
# llm_config_data = yaml.safe_load(Path('../config_examples/llm_configs.yml').read_text())
# llm_config = LLMConfig.model_validate(llm_config_data)

# Load Agent COnfiguration Data from YAML file
# agent_config_data = yaml.safe_load(Path('../config_examples/agent_configs.yml').read_text())
# print(f"AGENT DATA: {json.dumps(agent_config_data, indent=2)}")
# agents = Agents.model_validate(agent_config_data)

#agents.get

autogen.ChatCompletion.start_logging()

# def _reset_agents():
#     for agent_list in lists:
#         for agent in agent_list:
#             agent.reset()
#     agent_constructs.boss.reset()
#     agent_constructs.boss_aid.reset()
#     agent_constructs.coder.reset()
#     agent_constructs.pm.reset()
#     agent_constructs.reviewer.reset()
#     agent_constructs.manager.reset()
#     agent_constructs.geniusbot_qa.reset()
#     agent_constructs.engineer.reset()
#     agent_constructs.executor.reset()



def chat(prompt="Build snake game using pygame"):
    manager = Manager

    # Start chatting with boss as this is the user proxy agent.
    agents.Admin.initiate_chat(
        manager,
        message=prompt,
    )


#[agent_constructs.media_downloader_aid, agent_constructs.coder, agent_constructs.pm, agent_constructs.reviewer]
# def rag_chat(max_round: int = 18):
#     _reset_agents()
#     groupchat = autogen.GroupChat(
#         agents=[agent_constructs.planner, agent_constructs.aid, agent_constructs.engineer,
#                 agent_constructs.scientist, agent_constructs.executor, agent_constructs.critic],
#         messages=[],
#         max_round=max_round
#     )
#     manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=agent_constructs.llm_config)
#
#     # Start chatting with boss_aid as this is the user proxy agent.
#     agent_constructs.aid.initiate_chat(
#         manager,
#         problem=PROBLEM,
#         n_results=3,
#     )
#
#
# def norag_chat():
#     _reset_agents()
#     groupchat = autogen.GroupChat(
#         agents=[agent_constructs.boss_aid, agent_constructs.coder,
#                 agent_constructs.pm, agent_constructs.reviewer], messages=[], max_round=12
#     )
#     manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=agent_constructs.llm_config)
#
#     # Start chatting with boss as this is the user proxy agent.
#     agent_constructs.boss.initiate_chat(
#         manager,
#         message=PROBLEM,
#     )
#
#
# def call_rag_chat():
#     _reset_agents()
#
#     # In this case, we will have multiple user proxy agents and we don't initiate the chat
#     # with RAG user proxy agent.
#     # In order to use RAG user proxy agent, we need to wrap RAG agents in a function and call
#     # it from other agents.
#     def retrieve_content(message, n_results=3):
#         agent_constructs.boss_aid.n_results = n_results  # Set the number of results to be retrieved.
#         # Check if we need to update the context.
#         update_context_case1, update_context_case2 = agent_constructs.boss_aid._check_update_context(message)
#         if (update_context_case1 or update_context_case2) and agent_constructs.boss_aid.update_context:
#             agent_constructs.boss_aid.problem = message if not hasattr(agent_constructs.boss_aid,
#                                                                        "problem") else agent_constructs.boss_aid.problem
#             _, ret_msg = agent_constructs.boss_aid._generate_retrieve_user_reply(message)
#         else:
#             ret_msg = agent_constructs.boss_aid.generate_init_message(message, n_results=n_results)
#         return ret_msg if ret_msg else message
#
#     agent_constructs.boss_aid.human_input_mode = "NEVER"  # Disable human input for boss_aid since it only retrieves content.
#
#     llm_config = {
#         "functions": [
#             {
#                 "name": "retrieve_content",
#                 "description": "retrieve content for code generation and question answering.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "message": {
#                             "type": "string",
#                             "description": "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering.",
#                         }
#                     },
#                     "required": ["message"],
#                 },
#             },
#         ],
#         "config_list": agent_constructs.local_config_list,
#         "request_timeout": 600,
#         "seed": 42,
#     }
#
#     for agent in [agent_constructs.geniusbot, agent_constructs.coder,
#                   agent_constructs.pm, agent_constructs.reviewer]:
#         # update llm_config for assistant agents.
#         agent.llm_config.update(llm_config)
#
#     for agent in [agent_constructs.boss, agent_constructs.geniusbot,
#                   agent_constructs.coder, agent_constructs.pm, agent_constructs.reviewer]:
#         # register functions for all agents.
#         agent.register_function(
#             function_map={
#                 "retrieve_content": retrieve_content,
#             }
#         )
#
#     groupchat = autogen.GroupChat(
#         agents=[agent_constructs.boss, agent_constructs.coder, agent_constructs.pm, agent_constructs.reviewer],
#         messages=[], max_round=12
#     )
#     manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
#
#     # Start chatting with boss as this is the user proxy agent.
#     agent_constructs.boss.initiate_chat(
#         manager,
#         message=PROBLEM,
#     )

#call_rag_chat()
#rag_chat()

chat()
