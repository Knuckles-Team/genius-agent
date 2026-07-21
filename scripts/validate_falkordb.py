import asyncio
import os
import sys
from urllib.parse import urlparse

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

    uri = os.environ.get("FALKORDB_URI", "redis://127.0.0.1:6379")
    password = os.environ.get("GRAPHDB_PASSWORD")
    host, port = get_falkordb_params(uri)
    print(
        "Extracted connection settings: "
        f"host_configured={bool(host)}, port_configured={bool(port)}, "
        f"password_configured={bool(password)}"
    )

    try:
        print("Attempting to initialize FalkorDriver...")
        driver = FalkorDriver(
            host=host, port=port, password=password, database="default_db"
        )
        print("✅ FalkorDriver initialized successfully with configured authentication")
    except TypeError as e:
        print(f"Operation failed: {type(e).__name__}")
    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")


if __name__ == "__main__":
    asyncio.run(test_driver_init())
