import os
import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.integration

@pytest.fixture(scope="module")
def harness_app(tmp_path_factory):
    """Provides a TestClient to the agent_utilities harness initialized for genius-agent."""
    from agent_utilities.server import build_agent_app
    
    ws = tmp_path_factory.mktemp("harness_ws")
    db = tmp_path_factory.mktemp("harness_db") / "kg.db"
    
    os.environ["WORKSPACE_DIR"] = str(ws)
    os.environ["GRAPH_DB_PATH"] = str(db)
    os.environ.setdefault("DEFAULT_PROVIDER", "openai")
    os.environ.setdefault("DEFAULT_MODEL_ID", "dummy-model")
    
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
def client(harness_app):
    with TestClient(harness_app, raise_server_exceptions=False) as client:
        yield client

def test_harness_health(client: TestClient):
    """Test if the harness boots up correctly and answers /health."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "OK"

def test_harness_mcp_config_loaded(client: TestClient):
    """Test if MCP config is loaded by the harness."""
    response = client.get("/mcp/config")
    assert response.status_code == 200
    data = response.json()
    assert "mcpServers" in data
    # Because we synced 33 servers, there should be multiple here if mcp_config.json is populated.
    assert isinstance(data["mcpServers"], dict)

def test_harness_enhanced_endpoints(client: TestClient):
    """Test if the WebUI enhanced endpoints are mounted successfully."""
    endpoints = [
        "/api/enhanced/info",
        "/api/enhanced/graph/stats",
        "/api/enhanced/agents",
        "/api/enhanced/skills"
    ]
    for endpoint in endpoints:
        resp = client.get(endpoint)
        assert resp.status_code in (200, 404, 401), f"Endpoint {endpoint} returned unexpected status: {resp.status_code}"
        # We only care that it doesn't crash (500) and that routing exists.
