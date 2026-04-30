#!/usr/bin/env python3
import ast
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any

try:
    import tomllib
except ImportError:
    import tomli as tomllib

def get_agent_directories(base_dir: Path) -> list[Path]:
    """Find all agent packages containing mcp_server.py"""
    dirs = []
    for child in base_dir.iterdir():
        if child.is_dir() and child.name != "genius-agent":
            # Check if there is an mcp_server.py inside
            mcp_files = list(child.rglob("mcp_server.py"))
            # Exclude virtual environments
            mcp_files = [f for f in mcp_files if ".venv" not in f.parts]
            if mcp_files:
                dirs.append(child)
    return dirs

def parse_pyproject(agent_dir: Path) -> str:
    """Extract the mcp command name from pyproject.toml"""
    toml_path = agent_dir / "pyproject.toml"
    if not toml_path.exists():
        return None

    with open(toml_path, "rb") as f:
        data = tomllib.load(f)

    scripts = data.get("project", {}).get("scripts", {})
    for cmd, entry in scripts.items():
        if "mcp_server" in entry:
            return cmd
    return None

def extract_env_and_tags(mcp_file: Path) -> tuple[Dict[str, str], set[str]]:
    """Extract os.environ.get variables and tags from mcp.tool"""
    env_vars = {}
    tags = set()

    with open(mcp_file, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"Failed to parse {mcp_file}: {e}", file=sys.stderr)
        return env_vars, tags

    for node in ast.walk(tree):
        # Find os.environ.get calls
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr == "get":
                if isinstance(node.func.value, ast.Attribute) and node.func.value.attr == "environ":
                    if node.args and isinstance(node.args[0], ast.Constant):
                        key = node.args[0].value
                        env_vars[key] = f"${{{key}}}"
                        # Try to capture default value if present to format like ${KEY:-default}
                        if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                            default_val = node.args[1].value
                            if default_val is not None and str(default_val) != "":
                                env_vars[key] = f"${{{key}:-{default_val}}}"

        # Find @mcp.tool(tags={"tag"})
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call):
                    # Check if it's mcp.tool
                    func = decorator.func
                    if isinstance(func, ast.Attribute) and func.attr == "tool":
                        for keyword in decorator.keywords:
                            if keyword.arg == "tags" and isinstance(keyword.value, ast.Set):
                                for elt in keyword.value.elts:
                                    if isinstance(elt, ast.Constant):
                                        tags.add(elt.value)

    return env_vars, tags

def generate_global_mcp_config():
    base_dir = Path("/home/apps/workspace/agent-packages/agents")
    output_file = base_dir / "genius-agent" / "genius_agent" / "mcp_config.json"

    agents = get_agent_directories(base_dir)
    mcp_servers = {}

    for agent_dir in sorted(agents):
        cmd = parse_pyproject(agent_dir)
        if not cmd:
            print(f"Warning: No mcp_server script found in {agent_dir.name}", file=sys.stderr)
            continue

        mcp_files = list(agent_dir.rglob("mcp_server.py"))
        mcp_files = [f for f in mcp_files if ".venv" not in f.parts]
        if not mcp_files:
            continue

        env_vars, tags = extract_env_and_tags(mcp_files[0])

        # Build tool toggles
        for tag in sorted(tags):
            tag_formatted = tag.upper().replace("-", "_") + "TOOL"
            env_vars[tag_formatted] = f"${{ {tag_formatted}:-True }}"

        mcp_servers[agent_dir.name] = {
            "command": cmd,
            "args": ["--transport", "stdio"],
            "env": env_vars
        }

    config = {"mcpServers": mcp_servers}

    # Save the file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Successfully generated global configuration with {len(mcp_servers)} servers at {output_file}")

if __name__ == "__main__":
    generate_global_mcp_config()
