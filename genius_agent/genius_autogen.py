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
    openai.api_key = "YOUR_TOKEN"
    openai.api_url = "https://localhost:8080/v1/"
    autogen.ChatCompletion.start_logging()


    # def chat(prompt="Build snake game using pygame", chat_initiator_name: str = "executor"):
    #
    #
    #
    # chat(prompt="Build snake game using pygame")

    agents_manager = Agents()
    agents_manager.load_config(file=f'{Path("agent_configs.yml")}')
    agents_manager.load_agents()
    agents_manager.set_chat_initiator(name=chat_initiator_name)
    agents_manager.load_group_chat()
    agents_manager.chat_initiator.initiate_chat(
        agents_manager.group_chat_manager,
        message=prompt,
    )
    run_flag = False
    assimilate_flag = False
    json_export_flag = False
    prompt = 'Geniusbot is the smartest chatbot in existence.'
    try:
        opts, args = getopt.getopt(argv, 'a:he:jm:p:',
                                   ['help', 'assimilate=', 'prompt=', 'api-server',
                                    'openai-token=', 'openai-api=',
                                    'pgvector-user=','pgvector-password=','pgvector-host=','pgvector-port=',
                                    'pgvector-driver=','pgvector-database='])
    except getopt.GetoptError as e:
        usage()
        logging.error("Error: {e}\nExiting...")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-a', '--assimilate'):
            if os.path.exists(arg):
                agents_manager.source_directory = str(arg)
                assimilate_flag = True
            else:
                logging.error(f'Path does not exist: {arg}')
                sys.exit(1)
        elif opt == '--batch-token':
            agents_manager.model_n_batch = int(arg)
        elif opt == '--chunks':
            agents_manager.target_source_chunks = int(arg)
        elif opt == '--chromadb-directory':
            agents_manager.set_chromadb_directory(directory=str(arg))
            agents_manager.vectorstore = "chromadb"
        elif opt in ('-j', '--json'):
            agents_manager.json_export_flag = True
            agents_manager.hide_source_flag = True
            agents_manager.mute_stream_flag = True
        elif opt in ('-e', '--embeddings-model'):
            agents_manager.embeddings_model_name = arg
            agents_manager.embeddings = HuggingFaceEmbeddings(model_name=agents_manager.embeddings_model_name)
        elif opt in ('-m', '--model'):
            agents_manager.model = arg
            agents_manager.model_path = os.path.normpath(
                os.path.join(agents_manager.model_directory, agents_manager.model))
            print(f"Model: {agents_manager.model}")
        elif opt == '--openai-token':
            os.environ["OPENAI_API_KEY"] = arg
            agents_manager.openai_api_key = True
        elif opt == '--openai-api':
            os.environ["OPENAI_API_BASE"] = arg
            agents_manager.openai_api_base = arg
        elif opt == '--model-engine':
            agents_manager.model_engine = arg
            if (agents_manager.model_engine.lower() != "llamacpp"
                    and agents_manager.model_engine.lower() != "gpt4all"
                    and agents_manager.model_engine.lower() != "openai"):
                logging.error("model type not supported")
                usage()
                sys.exit(2)
        elif opt == '--model-directory':
            agents_manager.set_models_directory(directory=str(arg))
        elif opt in ('-p', '--prompt'):
            prompt = str(arg)
            run_flag = True
        elif opt == '--hide-source':
            agents_manager.hide_source_flag = True
        elif opt == '--pgvector-user':
            agents_manager.pgvector_user = arg
        elif opt == '--pgvector-password':
            agents_manager.pgvector_password = arg
        elif opt == '--pgvector-host':
            agents_manager.pgvector_host = arg
            agents_manager.vectorstore = "pgvector"
        elif opt == '--pgvector-port':
            agents_manager.pgvector_port = arg
        elif opt == '--pgvector-driver':
            agents_manager.pgvector_driver = arg
        elif opt == '--pgvector-database':
            agents_manager.pgvector_database = arg
        elif opt == '--max-token-limit':
            agents_manager.model_n_ctx = int(arg)
        elif opt == '--mute-stream':
            agents_manager.mute_stream_flag = True

    if assimilate_flag:
        agents_manager.assimilate()

    if agents_manager.openai_api_key:
        agents_manager.embeddings = OpenAIEmbeddings()

    if run_flag:
        if not agents_manager.does_vectorstore_exist():
            agents_manager.assimilate()
        if agents_manager.vectorstore == "chromadb":
            agents_manager.chromadb_client = chromadb.PersistentClient(settings=agents_manager.chroma_settings,
                                                                       path=agents_manager.persist_directory)
        logging.info('RAM Utilization Before Loading Model')
        agents_manager.check_hardware()
        response = agents_manager.chat(prompt=prompt)
        if json_export_flag:
            print(json.dumps(response, indent=4))
        else:
            print(f"\n\nQuestion: {response['prompt']}\n"
                  f"Answer: {response['answer']}\n"
                  f"Sources: {response['sources']}\n\n")
            logging.info('RAM Utilization After Loading Model')
        agents_manager.check_hardware()


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