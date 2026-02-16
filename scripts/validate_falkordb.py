import asyncio
from urllib.parse import urlparse
import sys
import os

try:
    from graphiti_core.driver.falkordb_driver import FalkorDriver

    print("FalkorDriver imported successfully.")
except ImportError:
    print("Failed to import FalkorDriver. Is graphiti-core installed?")
    sys.exit(1)


def get_falkordb_params(uri):
    print(f"Parsing URI: {uri}")
    parsed = urlparse(uri)
    host = parsed.hostname or "localhost"
    port = parsed.port or 6379
    return host, port


async def test_driver_init():
    # Test with the standard URI format found in compose.yaml
    uri = "redis://falkordb:6379"
    password = os.environ.get("GRAPHDB_PASSWORD", "letmein")
    host, port = get_falkordb_params(uri)
    print(f"Extracted -> Host: {host}, Port: {port}, Password: {password}")

    try:
        print("Attempting to initialize FalkorDriver...")
        driver = FalkorDriver(
            host=host, port=port, password=password, database="default_db"
        )
        print("✅ FalkorDriver initialized successfully with password!")
    except TypeError as e:
        print(f"❌ Initialization failed with TypeError: {e}")
    except Exception as e:
        print(f"❌ Initialization failed with Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_driver_init())
