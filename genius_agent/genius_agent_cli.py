#!/usr/bin/env python
# coding: utf-8

import sys
import autogen
import getopt
import json
from genius_agent.agent_construct import Agents
from pathlib import Path
import logging


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
    data = None
    file = None
    prompt = 'Build Tic-Tac-Toe in Pygame'
    try:
        opts, args = getopt.getopt(argv, 'h:d:f:p:',
                                   ['help', 'prompt=', 'file=', 'data=', "chat-initiator=", 'server='])
    except getopt.GetoptError as e:
        usage()
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
        elif opt in ('-s', '--server'):
            server_flag = arg

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
        config = {}

        config['log_config'] = {
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
        }

        # add your handler to it (in my case, I'm working with quart, but you can do this with Flask etc. as well, they're all the same)
        config['log_config']['loggers']['quart'] = {
            "handlers": [
                "default"
            ],
            "level": "INFO"
        }

        uvicorn.run("genius_agent_api:app", host="0.0.0.0", port=3001, reload=True,
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
