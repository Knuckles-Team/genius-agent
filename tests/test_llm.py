import httpx
import asyncio


async def test_llm():
    url = "http://10.0.0.18:1234/v1/chat/completions"
    headers = {"Authorization": "Bearer llama"}
    payload = {
        "model": "google/gemma-4-31b",
        "messages": [{"role": "user", "content": "hi"}],
        "max_tokens": 10,
    }

    print(f"Connecting to {url}...")
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, json=payload, headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_llm())
