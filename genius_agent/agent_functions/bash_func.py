#!/usr/bin/env python
# coding: utf-8

def exec_bash(agent, script):
    return agent.execute_code_blocks([("bash", script)])