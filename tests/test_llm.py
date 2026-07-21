import asyncio
import os

import httpx
import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_llm():
    base_url = os.environ.get("LLM_BASE_URL")
    if not base_url:
        pytest.skip("LLM_BASE_URL is required for the live integration test")
    assert base_url is not None
    url = f"{base_url.rstrip('/')}/chat/completions"
    api_key = os.environ.get("LLM_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    payload = {
        "model": os.environ.get("MODEL_ID", "local-model"),
        "messages": [{"role": "user", "content": "hi"}],
        "max_tokens": 10,
    }

    print(f"Connecting to {url}...")
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, json=payload, headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Response received: {len(response.content)} bytes")
    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")


if __name__ == "__main__":
    asyncio.run(test_llm())
