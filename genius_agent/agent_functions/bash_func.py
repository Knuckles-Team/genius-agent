def exec_bash(agent, script):
    return agent.execute_code_blocks([("sh", script)])