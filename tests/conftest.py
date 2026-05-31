"""Shared test fixtures for Genius Agent."""

import os
import pytest

# Set standard test environment variables at the module level so they are
# active before any module-scoped fixtures or imports start initializing the graph engine
os.environ.setdefault("OTEL_SDK_DISABLED", "true")
os.environ.setdefault("LOGFIRE_SEND_TO_LOGFIRE", "false")
os.environ.setdefault("ENABLE_GRAPH_INTEGRATION", "false")
os.environ.setdefault("AGENT_UTILITIES_TESTING", "true")
os.environ.setdefault("KNOWLEDGE_GRAPH_SYNC_BACKGROUND", "False")
os.environ.setdefault("GENIUS_URL", "https://test.example.com")
os.environ.setdefault("GENIUS_TOKEN", "test-token-12345")
os.environ.setdefault("GENIUS_SSL_VERIFY", "False")
os.environ.setdefault("OPENAI_API_KEY", "sk-test-not-real")
os.environ.setdefault("OPENAI_ADMIN_KEY", "sk-test-not-real")


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    """Set standard test environment variables."""
    monkeypatch.setenv("GENIUS_URL", "https://test.example.com")
    monkeypatch.setenv("GENIUS_TOKEN", "test-token-12345")
    monkeypatch.setenv("GENIUS_SSL_VERIFY", "False")
    monkeypatch.setenv("AGENT_UTILITIES_TESTING", "true")
