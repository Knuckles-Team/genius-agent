import os
import re
import tempfile
from pathlib import Path

import yaml

_ENV_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def parse_env_file(file_path):
    """Return variable names only; never retain or aggregate secret values."""

    variables: set[str] = set()
    if not os.path.exists(file_path):
        return variables

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key = line.split("=", 1)[0].strip()
                if _ENV_KEY.fullmatch(key):
                    variables.add(key)
    return variables


def parse_compose_file(file_path):
    variables: set[str] = set()
    if not os.path.exists(file_path):
        return variables

    try:
        with open(file_path) as f:
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
                            if _ENV_KEY.fullmatch(key):
                                variables.add(key)
                        elif ":" in entry:
                            key = entry.split(":", 1)[0].strip()
                            if _ENV_KEY.fullmatch(key):
                                variables.add(key)
                        else:
                            key = entry.strip()
                            if _ENV_KEY.fullmatch(key):
                                variables.add(key)
                elif isinstance(env_config, dict):
                    for key in env_config.keys():
                        if isinstance(key, str) and _ENV_KEY.fullmatch(key):
                            variables.add(key)
    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")

    return variables


def _atomic_write(path: Path, payload: str, *, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            descriptor = -1
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        os.chmod(path, mode)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if os.path.exists(temporary):
            os.unlink(temporary)


def main():
    root_dir = Path(__file__).parent.parent.parent.parent
    variable_names: set[str] = set()
    master_compose_vars = set()

    for env_file in root_dir.glob("*/.env"):
        variable_names.update(parse_env_file(str(env_file)))

    root_env = root_dir / ".env"
    if root_env.exists():
        variable_names.update(parse_env_file(str(root_env)))

    for compose_file in root_dir.glob("**/compose.y*ml"):
        master_compose_vars.update(parse_compose_file(str(compose_file)))

    variable_names.update(var for var in master_compose_vars if _ENV_KEY.fullmatch(var))

    xdg_config = Path(
        os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))
    )
    template_path = xdg_config / "agent-utilities" / "genius-agent" / "env.template"
    template = "# Variable-name template generated without source values\n" + "".join(
        f"{key}=\n" for key in sorted(variable_names)
    )
    _atomic_write(template_path, template, mode=0o644)

    print(f"Updated value-free environment template ({len(variable_names)} variables).")


if __name__ == "__main__":
    main()
