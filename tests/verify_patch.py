print("Attempting to import genius_mcp...")
try:
    from genius_agent import genius_mcp

    print("SUCCESS: genius_mcp imported without error.")
except ImportError as e:
    print(f"FAILURE: ImportError during import: {e}")
except AttributeError as e:
    print(f"FAILURE: AttributeError during import (Patch failed?): {e}")
except Exception as e:
    print(f"FAILURE: Unexpected error during import: {e}")
