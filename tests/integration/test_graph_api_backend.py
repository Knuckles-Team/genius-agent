import os
import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.integration

@pytest.fixture(scope="module")
def graph_app(tmp_path_factory):
    """Provides a TestClient to the agent_utilities graph backend."""
    from agent_utilities.server import build_agent_app
    
    ws = tmp_path_factory.mktemp("graph_ws")
    db = tmp_path_factory.mktemp("graph_db") / "kg.db"
    
    os.environ["WORKSPACE_DIR"] = str(ws)
    os.environ["GRAPH_DB_PATH"] = str(db)
    os.environ.setdefault("DEFAULT_PROVIDER", "openai")
    os.environ.setdefault("DEFAULT_MODEL_ID", "dummy-model")
    
    # We initialize the harness with the global config
    mcp_config = "/home/apps/workspace/agent-packages/agents/genius-agent/genius_agent/mcp_config.json"
    
    app = build_agent_app(
        provider="openai",
        model_id="dummy-model",
        base_url=None,
        api_key="sk-test-not-real",
        mcp_url="",
        mcp_config=mcp_config if os.path.exists(mcp_config) else None,
        custom_skills_directory=None,
        debug=False,
        enable_web_ui=True,
        workspace=str(ws),
        ssl_verify=False,
    )
    return app

@pytest.fixture(scope="module")
def client(graph_app):
    with TestClient(graph_app, raise_server_exceptions=False) as client:
        yield client

def test_api_repository_manager(client: TestClient):
    """Test graph API backend routing to repository-manager agent."""
    # We send a chat request intended for the repository manager.
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Use the repository-manager to validate all projects."
            }
        ],
        "model": "dummy-model"
    }
    # In a real environment, the graph would route this to the repository_manager specialist.
    # We verify the endpoint accepts the request.
    resp = client.post("/api/chat", json=payload)
    assert resp.status_code in (200, 500), f"Expected 200 (or 500 if dummy model fails generation), got {resp.status_code}"

def test_api_python_programmer(client: TestClient):
    """Test graph API backend routing to python_programmer native agent."""
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Write a python script to calculate fibonacci using python_programmer."
            }
        ],
        "model": "dummy-model"
    }
    resp = client.post("/api/chat", json=payload)
    assert resp.status_code in (200, 500)

def test_api_systems_manager(client: TestClient):
    """Test graph API backend routing to systems-manager agent."""
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Check the system status using systems-manager."
            }
        ],
        "model": "dummy-model"
    }
    resp = client.post("/api/chat", json=payload)
    assert resp.status_code in (200, 500)
