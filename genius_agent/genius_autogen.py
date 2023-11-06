import os
import sys
import autogen
import getopt
from langchain.embeddings import HuggingFaceEmbeddings
import json
import openai
from agent_constructs import Agents
from pathlib import Path
import logging


def usage():
    print(f'Usage:\n'
          f'-h | --help               [ See usage for script ]\n'
          f'-a | --assimilate         [ Assimilate knowledge from media provided in directory ]\n'
          f'   | --batch-token        [ Number of tokens per batch ]\n'
          f'   | --chromadb-directory [ Directory for chromadb persistent storage ]\n'
          f'   | --chunks             [ Number of chunks to use ]\n'
          f'-e | --embeddings-model   [ Embeddings model to use https://www.sbert.net/docs/pretrained_models.html ]\n'
          f'   | --hide-source        [ Hide source of answer ]\n'
          f'-j | --json               [ Export to JSON ]\n'
          f'   | --openai-token       [ OpenAI token ]\n'
          f'   | --openai-api         [ OpenAI API Url ]\n'
          f'   | --pgvector-user      [ PGVector user ]\n'
          f'   | --pgvector-password  [ PGVector password ]\n'
          f'   | --pgvector-host      [ PGVector host ]\n'
          f'   | --pgvector-port      [ PGVector port ]\n'
          f'   | --pgvector-database  [ PGVector database ]\n'
          f'   | --pgvector-driver    [ PGVector driver ]\n'
          f'-p | --prompt             [ Prompt for chatbot ]\n'
          f'   | --mute-stream        [ Mute stream of generation ]\n'
          f'-m | --model              [ Model to use from GPT4All https://gpt4all.io/index.html ]\n'
          f'   | --max-token-limit    [ Maximum token to generate ]\n'
          f'   | --model-directory    [ Directory to store models ]\n'
          f'   | --model-engine       [ GPT4All, LlamaCPP, or OpenAI ]\n'
          f'\nExample:\n'
          f'genius-agent --prompt "What is the 10th digit of Pi?"\n')


def genius_agent(argv):
    autogen.ChatCompletion.start_logging()

    # def chat(prompt="Build snake game using pygame", chat_initiator_name: str = "executor"):
    #
    #
    #
    # chat(prompt="Build snake game using pygame")

    run_flag = False
    api_flag = False
    data = None
    file = None
    prompt = 'Geniusbot is the smartest chatbot in existence.'
    try:
        opts, args = getopt.getopt(argv, 'h:d:f:p:',
                                   ['help', 'prompt=', 'data=', 'api-host=', 'api-port=', "chat-initiator="])
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
