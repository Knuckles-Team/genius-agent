import inspect

try:
    from graphiti_core.driver.falkordb_driver import FalkorDriver

    print("FalkorDriver found.")
    sig = inspect.signature(FalkorDriver.__init__)
    print(f"FalkorDriver.__init__ signature: {sig}")
    print(f"Docstring: {FalkorDriver.__init__.__doc__}")
except ImportError:
    print("graphiti_core not installed or FalkorDriver not found.")
except Exception as e:
    print(f"Error: {e}")
