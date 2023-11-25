#!/usr/bin/env python
# coding: utf-8

import sys
import autogen
import getopt
import json
from genius_agent.agent_construct import Agents
from pathlib import Path


try:
    import uvicorn
except ImportError:
    print("uvicorn was not installed, please install with pip install genius-agent[api]")


def usage():
    print(f'Usage:\n'
          f'-h | --help               [ See usage for script ]\n'
          f'-p | --prompt             [ Prompt for chatbot ]\n'
          f'\nExample:\n'
          f'genius-agent --prompt "What is the 10th digit of Pi?"\n')


def genius_agent(argv):
    autogen.ChatCompletion.start_logging()
    run_flag = False
    server_flag = False
    server_address = ''
    server_port = ''
    data = None
    file = None
    prompt = 'Build Tic-Tac-Toe in Pygame'
    try:
        opts, args = getopt.getopt(argv, 'h:d:f:p:',
                                   ['help', 'prompt=', 'file=', 'data=', "chat-initiator=", 'server-host=',
                                    'server-port='])
    except getopt.GetoptError as e:
        usage()
        import logging
        logging.error("Error: {e}\nExiting...")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-d', '--data'):
            data = arg
        elif opt in ('-f', '--file'):
            file = arg
        elif opt in ('-p', '--prompt'):
            prompt = str(arg)
            run_flag = True
        elif opt in ('-s', '--server-host'):
            server_flag = True
            server_address = arg
        elif opt in ('-p', '--server-port'):
            server_flag = True
            server_port = int(arg)


    if run_flag:
        agents_manager = Agents()
        if file:
            agents_manager.load_config(file=file)
        elif data:
            agents_manager.load_config(payload=json.loads(data))
        else:
            agents_manager.load_config(file=f'{Path("agent_configs.yml")}')

        agents_manager.load_agents()
        agents_manager.chat(prompt)

    if server_flag:
        import logging

        logging.basicConfig(level=logging.DEBUG)
        config = {'log_config': {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s %(message)s",
                    "use_colors": "None"
                },
                "access": {
                    "()": "uvicorn.logging.AccessFormatter",
                    "fmt": "%(levelprefix)s %(client_addr)s - \"%(request_line)s\" %(status_code)s"
                }
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stderr"
                },
                "access": {
                    "formatter": "access",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout"
                }
            },
            "loggers": {
                "uvicorn": {
                    "handlers": [
                        "default"
                    ],
                    "level": "INFO"
                },
                "uvicorn.error": {
                    "level": "INFO",
                    "handlers": [
                        "default"
                    ],
                    "propagate": True
                },
                "uvicorn.access": {
                    "handlers": [
                        "access"
                    ],
                    "level": "INFO",
                    "propagate": False
                }
            }
        }}

        config['log_config']['loggers']['quart'] = {
            "handlers": [
                "default"
            ],
            "level": "INFO"
        }

        uvicorn.run("genius_agent_api:app", host=server_address, port=server_port, reload=True,
                    log_level="debug", **config)


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
