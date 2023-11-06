import os
import sys
import autogen
import getopt
import json
from agent_constructs import Agents
from pathlib import Path
import logging


def usage():
    print(f'Usage:\n'
          f'-h | --help               [ See usage for script ]\n'
          f'-p | --prompt             [ Prompt for chatbot ]\n'
          f'\nExample:\n'
          f'genius-agent --prompt "What is the 10th digit of Pi?"\n')


def genius_agent(argv):
    autogen.ChatCompletion.start_logging()
    run_flag = False
    api_flag = False
    data = None
    file = None
    prompt = 'Build Tic-Tac-Toe in Pygame'
    try:
        opts, args = getopt.getopt(argv, 'h:d:f:p:',
                                   ['help', 'prompt=', 'file=', 'data=', "chat-initiator="])
    except getopt.GetoptError as e:
        usage()
        logging.error("Error: {e}\nExiting...")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        # elif opt == '--api-host':
        #     api_host = arg
        #     api_flag = True
        # elif opt == '--api-port':
        #     api_port = arg
        elif opt in ('-d', '--data'):
            data = arg
        elif opt in ('-f', '--file'):
            file = arg
        # elif opt == '--openai-token':
        #     os.environ["OPENAI_API_KEY"] = arg
        #     openai.api_key = arg
        # elif opt == '--openai-api':
        #     os.environ["OPENAI_API_BASE"] = arg
        #     openai.api_url = arg
        elif opt in ('-p', '--prompt'):
            prompt = str(arg)
            run_flag = True
        elif opt == '--chat-initiator':
            chat_initiator = arg
        # elif opt == '--pgvector-user':
        #     agents_manager.pgvector_user = arg
        # elif opt == '--pgvector-password':
        #     agents_manager.pgvector_password = arg
        # elif opt == '--pgvector-host':
        #     agents_manager.pgvector_host = arg
        #     agents_manager.vectorstore = "pgvector"
        # elif opt == '--pgvector-port':
        #     agents_manager.pgvector_port = arg
        # elif opt == '--pgvector-driver':
        #     agents_manager.pgvector_driver = arg
        # elif opt == '--pgvector-database':
        #     agents_manager.pgvector_database = arg

    if run_flag:
        agents_manager = Agents()
        if file:
            agents_manager.load_config(file=file)
        elif data:
            agents_manager.load_config(payload=json.loads(data))
        else:
            agents_manager.load_config(file=f'{Path("agent_configs.yml")}')
        agents_manager.load_agents()
        agents_manager.set_chat_initiator(name=chat_initiator)
        agents_manager.load_group_chat()
        agents_manager.chat_initiator.initiate_chat(
            agents_manager.group_chat_manager,
            message=prompt,
        )
    if api_flag:
        from agent_constructs import GeniusAgentAPI
        genius_api_agent = GeniusAgentAPI(agents_manager=agents_manager)


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(2)
    genius_agent(sys.argv[1:])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(2)
    genius_agent(sys.argv[1:])
