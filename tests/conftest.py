"""Shared test fixtures for Genius Agent."""

import pytest


@pytest.fixture
def mock_env(monkeypatch):
    """Set standard test environment variables."""
    monkeypatch.setenv("GENIUS_URL", "https://test.example.com")
    monkeypatch.setenv("GENIUS_TOKEN", "test-token-12345")
    monkeypatch.setenv("GENIUS_SSL_VERIFY", "False")
