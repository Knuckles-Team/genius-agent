import importlib.metadata
import importlib

discovered_modules = set()
for dist in importlib.metadata.distributions():
    pkg = dist.metadata.get("Name")
    if not pkg or pkg in ["agent-utilities", "universal-skills", "genius-agent"]:
        continue
    module_name = pkg.replace("-", "_")
    if module_name in discovered_modules:
        continue
    print(f"Checking {module_name}...")
    try:
        agent_server = importlib.import_module(f"{module_name}.agent_server")
        print(f"Imported {module_name}.agent_server")
    except Exception as e:
        print(f"Failed {module_name}: {e}")
