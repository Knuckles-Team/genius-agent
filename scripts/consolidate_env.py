import os
import re
import yaml
from pathlib import Path


def parse_env_file(file_path):
    variables = {}
    if not os.path.exists(file_path):
        return variables

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                variables[key.strip()] = value.strip()
    return variables


def parse_compose_file(file_path):
    variables = set()
    if not os.path.exists(file_path):
        return variables

    try:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
            if not data or "services" not in data:
                return variables

            for service_name, service_config in data["services"].items():
                env_config = service_config.get("environment")
                if not env_config:
                    continue

                if isinstance(env_config, list):
                    for entry in env_config:
                        if "=" in entry:
                            key = entry.split("=", 1)[0].strip()
                            variables.add(key)
                        elif ":" in entry:
                                                                                                   
                            key = entry.split(":", 1)[0].strip()
                            variables.add(key)
                        else:
                                                       
                            variables.add(entry.strip())
                elif isinstance(env_config, dict):
                    for key in env_config.keys():
                        variables.add(key)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")

    return variables


def main():
    root_dir = Path("/home/genius/Workspace/agent-packages")
    genius_agent_dir = root_dir / "genius-agent"

    master_env = {}
    master_compose_vars = set()

                                                                                     
                                                                                    

                                           
    genius_env_path = genius_agent_dir / ".env"
    master_env.update(parse_env_file(genius_env_path))

                   
    for env_file in root_dir.glob("*/.env"):
        if env_file.parent.name == "genius-agent":
            continue
        new_vars = parse_env_file(env_file)
        for k, v in new_vars.items():
            if k not in master_env:
                master_env[k] = v

                                      
    root_env = root_dir / ".env"
    if root_env.exists():
        new_vars = parse_env_file(root_env)
        for k, v in new_vars.items():
            if k not in master_env:
                master_env[k] = v

                                                 
    for compose_file in root_dir.glob("**/compose.y*ml"):
        master_compose_vars.update(parse_compose_file(compose_file))

                                                                       
    for var in master_compose_vars:
        if var not in master_env:
                                                                                
                                                                              
                                                                                  
            if var.isupper():
                master_env[var] = ""

                          
    with open(genius_env_path, "w") as f:
        f.write("# Master .env consolidated from agent-packages\n")
                               
        for k in sorted(master_env.keys()):
            f.write(f"{k}={master_env[k]}\n")

    print(f"Updated {genius_env_path} with {len(master_env)} variables.")

                                         
    genius_compose_path = genius_agent_dir / "compose.yaml"
    if genius_compose_path.exists():
        with open(genius_compose_path, "r") as f:
            compose_data = yaml.safe_load(f)

        if "services" in compose_data and "genius-agent" in compose_data["services"]:
                                                                                           
                                    
            env_list = []
            for k in sorted(master_env.keys()):
                                                                                    
                                              
                env_list.append(f"{k}=${{{k}}}")

            compose_data["services"]["genius-agent"]["environment"] = env_list

            with open(genius_compose_path, "w") as f:
                yaml.dump(compose_data, f, sort_keys=False, default_flow_style=False)
            print(f"Updated {genius_compose_path} environment section.")


if __name__ == "__main__":
    main()
