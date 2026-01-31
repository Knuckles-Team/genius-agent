
import os
import sys
from pathlib import Path

# Add the project root to the python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# try:
from genius_agent.genius_mcp import create_graphiti_resources
from graphiti_core.driver.kuzu_driver import KuzuDriver
# except ImportError as e:
#     print(f"ImportError: {e}")
#     sys.exit(1)

def test_kuzu_initialization():
    print("Testing Kuzu Initialization...")
    
    # Mock environment variables if needed
    os.environ["GRAPHDB_TYPE"] = "kuzu"
    os.environ["GRAPHDB_URI"] = "./test_kuzu_db"
    
    try:
        resources = create_graphiti_resources(
            graph_type="kuzu",
            graph_uri="./test_kuzu_db"
        )
        
        graph_driver = resources.get("graph_driver")
        
        if isinstance(graph_driver, KuzuDriver):
            print("SUCCESS: Graph driver is instance of KuzuDriver")
        else:
            print(f"FAILURE: Graph driver is {type(graph_driver)}, expected KuzuDriver")
            sys.exit(1)
            
    except Exception as e:
        print(f"FAILURE: Exception during initialization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_kuzu_initialization()
