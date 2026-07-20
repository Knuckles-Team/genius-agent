#!/usr/bin/env python3
import ast
import json
import os
import sys
import tempfile
from pathlib import Path

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
        return ""

    with open(toml_path, "rb") as f:
        data = tomllib.load(f)

    scripts = data.get("project", {}).get("scripts", {})
    for cmd, entry in scripts.items():
        if "mcp_server" in entry:
            return cmd
    return ""


def extract_env_and_tags(mcp_file: Path) -> tuple[dict[str, str], set[str]]:
    """Extract os.environ.get variables and tags from mcp.tool"""
    env_vars: dict[str, str] = {}
    tags: set[str] = set()

    with open(mcp_file, encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except Exception as exc:
        print(f"Failed to parse MCP module: {type(exc).__name__}", file=sys.stderr)
        return env_vars, tags

    for node in ast.walk(tree):
        # Find os.environ.get calls
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr == "get":
                if (
                    isinstance(node.func.value, ast.Attribute)
                    and node.func.value.attr == "environ"
                ):
                    if node.args and isinstance(node.args[0], ast.Constant):
                        key = node.args[0].value
                        if isinstance(key, str):
                            env_vars[key] = f"${{{key}}}"
                            # Runtime defaults remain in source/AgentConfig; generated
                            # configuration contains references, never copied values.

        # Find @mcp.tool(tags={"tag"})
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call):
                    # Check if it's mcp.tool
                    func = decorator.func
                    if isinstance(func, ast.Attribute) and func.attr == "tool":
                        for keyword in decorator.keywords:
                            if keyword.arg == "tags" and isinstance(
                                keyword.value, ast.Set
                            ):
                                for elt in keyword.value.elts:
                                    if isinstance(elt, ast.Constant) and isinstance(
                                        elt.value, str
                                    ):
                                        tags.add(elt.value)

    return env_vars, tags


def generate_global_mcp_config():
    base_dir = Path(__file__).resolve().parents[2]
    xdg_config = Path(
        os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))
    )
    output_file = xdg_config / "agent-utilities" / "mcp_config.json"

    agents = get_agent_directories(base_dir)
    mcp_servers = {}

    for agent_dir in sorted(agents):
        cmd = parse_pyproject(agent_dir)
        if not cmd:
            print("Warning: no MCP server script found in configured agent", file=sys.stderr)
            continue

        mcp_files = list(agent_dir.rglob("mcp_server.py"))
        mcp_files = [f for f in mcp_files if ".venv" not in f.parts]
        if not mcp_files:
            continue

        env_vars, tags = extract_env_and_tags(mcp_files[0])

        # Build tool toggles
        for tag in sorted(tags):
            tag_formatted = tag.upper().replace("-", "_") + "TOOL"
            env_vars[tag_formatted] = f"${{{tag_formatted}:-true}}"

        mcp_servers[agent_dir.name] = {
            "command": cmd,
            "args": ["--transport", "stdio"],
            "env": env_vars,
        }

    config = {"mcpServers": mcp_servers}

    # Save the file
    output_file.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=".mcp-config.", dir=output_file.parent
    )
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            descriptor = -1
            json.dump(config, handle, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output_file)
        os.chmod(output_file, 0o600)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if os.path.exists(temporary):
            os.unlink(temporary)

    print(f"Successfully generated global configuration with {len(mcp_servers)} servers")

if __name__ == "__main__":
    generate_global_mcp_config()
