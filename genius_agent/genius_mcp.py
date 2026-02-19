#!/usr/bin/python
# coding: utf-8
import asyncio
import os
import json

os.environ["GRAPHITI_TELEMETRY_ENABLED"] = "false"
import logging
import re
from pathlib import Path
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse

import uuid
import shutil
from pydantic import Field
from fastmcp import FastMCP, Context
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

try:
    from graphiti_core import Graphiti
    from graphiti_core.llm_client.openai_client import OpenAIClient
    from graphiti_core.llm_client.anthropic_client import AnthropicClient
    from graphiti_core.llm_client.gemini_client import GeminiClient
    from graphiti_core.llm_client.groq_client import GroqClient
    from graphiti_core.llm_client.azure_openai_client import AzureOpenAILLMClient
    from graphiti_core.llm_client.openai_generic_client import OpenAIGenericClient
    from graphiti_core.embedder.azure_openai import AzureOpenAIEmbedderClient
    from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig
    from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig
    from graphiti_core.cross_encoder.gemini_reranker_client import GeminiRerankerClient
    from graphiti_core.cross_encoder.openai_reranker_client import OpenAIRerankerClient
    from graphiti_core.llm_client.config import LLMConfig
    from graphiti_core.utils.bulk_utils import RawEpisode
    from graphiti_core.driver.falkordb_driver import FalkorDriver
    from graphiti_core.driver.neo4j_driver import Neo4jDriver
    from graphiti_core.driver.kuzu_driver import KuzuDriver
    from graphiti_core.nodes import EpisodeType
    from datetime import datetime, timezone
except ImportError as e:
    print(f"Warning: graphiti-core or dependencies not installed: {e}")
    Graphiti = None
    OpenAIClient = None
    AnthropicClient = None
    GeminiClient = None
    GroqClient = None
    AzureOpenAILLMClient = None
    OpenAIGenericClient = None
    AzureOpenAIEmbedderClient = None
    GeminiEmbedder = None
    OpenAIEmbedder = None
    GeminiRerankerClient = None
    OpenAIRerankerClient = None
    FalkorDriver = None
    Neo4jDriver = None
    KuzuDriver = None

# Monkeypatch OpenAIClient to fix JSON parsing and refusal error
try:
    from graphiti_core.llm_client.openai_client import OpenAIClient
    from genius_agent.utils.patch_utils import apply_patch

    # 1. Patch _extract_json (Legacy support)
    # The original method expected a string and returned a dict
    if hasattr(OpenAIClient, "_extract_json"):
        original_extract_json = OpenAIClient._extract_json

        def patched_extract_json(self, response: str) -> dict:
            if response.startswith("```json"):
                response = response[7:]
            elif response.startswith("```"):
                response = response[3:]
            if response.endswith("```"):
                response = response[:-3]
            return original_extract_json(self, response.strip())

        apply_patch(OpenAIClient, "_extract_json", patched_extract_json)

    # 2. Patch _handle_json_response
    if hasattr(OpenAIClient, "_handle_json_response"):
        original_handle_json_response = OpenAIClient._handle_json_response

        def patched_handle_json_response(self, response: Any) -> Dict[str, Any]:
            # Try to get content from response object
            content = None
            if hasattr(response, "choices") and response.choices:
                content = response.choices[0].message.content

            # If we got content, strip markdown
            if content and isinstance(content, str):
                if content.startswith("```json"):
                    content = content[7:]
                elif content.startswith("```"):
                    content = content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                content = content.strip()
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    pass  # Fallback to original

            return original_handle_json_response(self, response)

        apply_patch(OpenAIClient, "_handle_json_response", patched_handle_json_response)

    # 3. Patch _handle_structured_response
    if hasattr(OpenAIClient, "_handle_structured_response"):
        original_handle_structured_response = OpenAIClient._handle_structured_response

        def patched_handle_structured_response(self, response: Any) -> Dict[str, Any]:
            # Try to get content from response.output_text
            content = getattr(response, "output_text", None)

            if content and isinstance(content, str):
                # Strip markdown
                if content.startswith("```json"):
                    content = content[7:]
                elif content.startswith("```"):
                    content = content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                content = content.strip()

                try:
                    parsed = json.loads(content)

                    # FIX: Handle ExtractedEntities list vs object mismatch
                    # If parsed is a list, and items look like ExtractedEntity (have "entity_type_id"),
                    # wrap it in "extracted_entities" to match Pydantic model.
                    if isinstance(parsed, list):
                        if not parsed or (
                            isinstance(parsed[0], dict)
                            and "entity_type_id" in parsed[0]
                        ):
                            return {"extracted_entities": parsed}

                    return parsed
                except json.JSONDecodeError:
                    pass

            return original_handle_structured_response(self, response)

        apply_patch(
            OpenAIClient,
            "_handle_structured_response",
            patched_handle_structured_response,
        )

    # 3. Patch generate_response (Refusal Error)
    if hasattr(OpenAIClient, "generate_response"):
        original_generate_response = OpenAIClient.generate_response

        async def patched_generate_response(
            self, prompt: str, schema: Any = None, **kwargs
        ) -> Any:
            try:
                return await original_generate_response(self, prompt, schema, **kwargs)
            except AttributeError as e:
                # Catch specific refusal error commonly seen with some proxies/models
                if "'str' object has no attribute 'refusal'" in str(e):
                    logger.warning(
                        "Caught 'refusal' attribute error. This often means the library expected an object with a refusal attribute but got a string string."
                    )
                    # We re-raise because we can't easily fix the return structure here without more context
                    raise e
                raise e

        apply_patch(OpenAIClient, "generate_response", patched_generate_response)

except ImportError:
    pass

try:
    from crawl4ai import (
        AsyncWebCrawler,
        BrowserConfig,
        CrawlerRunConfig,
        CacheMode,
        MemoryAdaptiveDispatcher,
    )
except ImportError:
    print("Warning: crawl4ai not installed.")
    AsyncWebCrawler = None

from urllib.parse import urldefrag

from fastmcp import Client

from genius_agent.utils import to_boolean, to_integer

__version__ = "2.13.14"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    force=True,
)
logger = get_logger("GeniusAgentMCP")

# Silence noisy libraries
logging.getLogger("crawl4ai").setLevel(logging.ERROR)
logging.getLogger("graphiti_core").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)

config = {
    "enable_delegation": to_boolean(os.environ.get("ENABLE_DELEGATION", "False")),
    "audience": os.environ.get("AUDIENCE", None),
    "delegated_scopes": os.environ.get("DELEGATED_SCOPES", "api"),
    "token_endpoint": None,
    "oidc_client_id": os.environ.get("OIDC_CLIENT_ID", None),
    "oidc_client_secret": os.environ.get("OIDC_CLIENT_SECRET", None),
    "oidc_config_url": os.environ.get("OIDC_CONFIG_URL", None),
    "jwt_jwks_uri": os.getenv("FASTMCP_SERVER_AUTH_JWT_JWKS_URI", None),
    "jwt_issuer": os.getenv("FASTMCP_SERVER_AUTH_JWT_ISSUER", None),
    "jwt_audience": os.getenv("FASTMCP_SERVER_AUTH_JWT_AUDIENCE", None),
    "jwt_algorithm": os.getenv("FASTMCP_SERVER_AUTH_JWT_ALGORITHM", None),
    "jwt_secret": os.getenv("FASTMCP_SERVER_AUTH_JWT_PUBLIC_KEY", None),
    "jwt_required_scopes": os.getenv("FASTMCP_SERVER_AUTH_JWT_REQUIRED_SCOPES", None),
}

DEFAULT_TRANSPORT = os.environ.get("TRANSPORT", "stdio")
DEFAULT_HOST = os.environ.get("HOST", "0.0.0.0")
DEFAULT_PORT = to_integer(os.environ.get("PORT", "9000"))

DEFAULT_DOCUMENTS_DIRECTORY = os.environ.get("DOCUMENTS_DIRECTORY", "/documents")
DEFAULT_COLLECTIONS_DIRECTORY = os.environ.get("COLLECTIONS_DIRECTORY", "/collections")

DEFAULT_GRAPHDB_URI = os.environ.get("GRAPHDB_URI", "./kuzu_db")
DEFAULT_GRAPHDB_USERNAME = os.environ.get("GRAPHDB_USERNAME", None)
DEFAULT_GRAPHDB_PASSWORD = os.environ.get("GRAPHDB_PASSWORD", None)
DEFAULT_GRAPHDB_TYPE = os.environ.get("GRAPHDB_TYPE", "kuzu")
DEFAULT_GRAPHDB_NAME = os.environ.get("GRAPHDB_NAME", "neo4j")

DEFAULT_PROVIDER = os.getenv("PROVIDER", "openai")
DEFAULT_MODEL_ID = os.getenv("MODEL_ID", "zai-org/glm-4.7-flash")
DEFAULT_LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://host.docker.internal:1234/v1")
DEFAULT_LLM_API_KEY = os.getenv("LLM_API_KEY", "llama")

DEFAULT_EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", DEFAULT_PROVIDER)
DEFAULT_EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
DEFAULT_EMBEDDING_BASE_URL = os.getenv("EMBEDDING_BASE_URL", DEFAULT_LLM_BASE_URL)
DEFAULT_EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY", DEFAULT_LLM_API_KEY)
DEFAULT_EMBEDDING_DIM = to_integer(os.getenv("EMBEDDING_DIM", "768"))

DEFAULT_DATABASE_TYPE = os.getenv("DATABASE_TYPE", "chromadb")
VECTOR_MCP_URL = os.environ.get("VECTOR_MCP_URL", "http://vector-mcp:8000/sse")
DOCUMENTDB_MCP_URL = os.environ.get(
    "DOCUMENTDB_MCP_URL", "http://documentdb-mcp:8015/mcp"
)

INGESTION_STATE: Dict[str, Dict[str, Any]] = {}


def create_graphiti_resources(
    provider: str = DEFAULT_PROVIDER,
    model_id: str = DEFAULT_MODEL_ID,
    base_url: Optional[str] = DEFAULT_LLM_BASE_URL,
    api_key: Optional[str] = DEFAULT_LLM_API_KEY,
    graph_type: str = DEFAULT_GRAPHDB_TYPE,
    graph_uri: str = DEFAULT_GRAPHDB_URI,
    graph_user: str = DEFAULT_GRAPHDB_USERNAME,
    graph_password: str = DEFAULT_GRAPHDB_PASSWORD,
    graph_name: str = DEFAULT_GRAPHDB_NAME,
) -> Dict[str, Any]:
    """Create Graphiti resources (LLM, Embedder, CrossEncoder, Driver) based on provider."""

    resources = {}

    if provider == "openai":
        base_url = os.environ.get("LLM_BASE_URL", base_url)
        api_key = os.environ.get("LLM_API_KEY", api_key)
        config = LLMConfig(api_key=api_key, model=model_id, base_url=base_url)
        resources["llm_client"] = OpenAIClient(config=config)

    elif provider == "azure":
        from graphiti_core.llm_client.azure_openai_client import AzureOpenAILLMClient

        from openai import AsyncOpenAI

        azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", base_url)
        azure_key = os.environ.get("AZURE_LLM_API_KEY", api_key)

        azure_client = AsyncOpenAI(
            base_url=azure_endpoint,
            api_key=azure_key,
            api_version=os.environ.get(
                "AZURE_OPENAI_API_VERSION", "2024-02-15-preview"
            ),
        )
        resources["llm_client"] = AzureOpenAILLMClient(
            azure_client=azure_client,
            config=LLMConfig(model=model_id, small_model=model_id),
        )

    elif provider == "google":
        api_key = (
            os.environ.get("LLM_API_KEY") or os.environ.get("LLM_API_KEY") or api_key
        )
        config = LLMConfig(api_key=api_key, model=model_id)
        resources["llm_client"] = GeminiClient(config=config)

    elif provider == "ollama":
        config = LLMConfig(
            api_key="llama",
            model=model_id,
            small_model=model_id,
            base_url=base_url or "http://host.docker.internal:1234/v1",
        )
        resources["llm_client"] = OpenAIGenericClient(config=config)

    elif provider == "anthropic":
        api_key = os.environ.get("LLM_API_KEY", api_key)
        config = LLMConfig(api_key=api_key, model=model_id)
        resources["llm_client"] = AnthropicClient(config=config)

    elif provider == "groq":
        api_key = os.environ.get("LLM_API_KEY", api_key)
        config = LLMConfig(api_key=api_key, model=model_id)
        resources["llm_client"] = GroqClient(config=config)

    else:
        logger.warning(f"Unknown provider {provider}, defaulting to OpenAIClient")
        config = LLMConfig(api_key=api_key, model=model_id, base_url=base_url)
        resources["llm_client"] = OpenAIClient(config=config)

    emb_provider = os.getenv("EMBEDDING_PROVIDER", provider)

    if emb_provider == "azure":
        from graphiti_core.embedder.azure_openai import AzureOpenAIEmbedderClient
        from openai import AsyncOpenAI

        azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", base_url)
        azure_key = os.environ.get("AZURE_LLM_API_KEY", api_key)

        if provider == "azure" and "llm_client" in resources:
            pass

        azure_client_emb = AsyncOpenAI(
            base_url=azure_endpoint,
            api_key=azure_key,
            api_version=os.environ.get(
                "AZURE_OPENAI_API_VERSION", "2024-02-15-preview"
            ),
        )
        resources["embedder"] = AzureOpenAIEmbedderClient(
            azure_client=azure_client_emb, model=DEFAULT_EMBEDDING_MODEL
        )

    elif emb_provider == "google":
        api_key = (
            os.environ.get("LLM_API_KEY") or os.environ.get("LLM_API_KEY") or api_key
        )
        resources["embedder"] = GeminiEmbedder(
            config=GeminiEmbedderConfig(
                api_key=api_key,
                embedding_model=DEFAULT_EMBEDDING_MODEL or "embedding-001",
            )
        )
        resources["cross_encoder"] = GeminiRerankerClient(
            config=LLMConfig(
                api_key=api_key,
                model="gemini-2.5-flash-lite",
            )
        )

    elif emb_provider == "ollama":
        resources["embedder"] = OpenAIEmbedder(
            config=OpenAIEmbedderConfig(
                api_key="ollama",
                embedding_model=DEFAULT_EMBEDDING_MODEL or "nomic-embed-text",
                embedding_dim=DEFAULT_EMBEDDING_DIM or 768,
                base_url=DEFAULT_EMBEDDING_BASE_URL
                or "http://host.docker.internal:1234/v1",
            )
        )
        resources["cross_encoder"] = OpenAIRerankerClient(
            client=resources["llm_client"], config=resources["llm_client"].config
        )

    else:
        resources["embedder"] = OpenAIEmbedder(
            config=OpenAIEmbedderConfig(
                api_key=api_key,
                embedding_model=DEFAULT_EMBEDDING_MODEL,
                base_url=DEFAULT_EMBEDDING_BASE_URL,
            )
        )

    if graph_type == "falkordb":
        try:
            from graphiti_core.driver.falkordb_driver import FalkorDriver
            from urllib.parse import urlparse

            parsed = urlparse(graph_uri)
            host = parsed.hostname or "localhost"
            port = parsed.port or 6379

            resources["graph_driver"] = FalkorDriver(
                host=host,
                port=port,
                username=graph_user,
                password=graph_password,
                database=graph_name,
            )
        except ImportError:
            logger.error("FalkorDB driver not available")
            raise
    elif graph_type == "kuzu":
        try:
            from graphiti_core.driver.kuzu_driver import KuzuDriver

            resources["graph_driver"] = KuzuDriver(db=graph_uri)
        except ImportError:
            logger.error("Kuzu driver not available")
            raise
    else:
        try:
            from graphiti_core.driver.neo4j_driver import Neo4jDriver

            resources["graph_driver"] = Neo4jDriver(
                uri=graph_uri,
                user=graph_user,
                password=graph_password,
                database=graph_name,
            )
        except ImportError:
            logger.error("Neo4j driver not available")
            raise

    return resources


def get_collection_name_from_url(url: str) -> str:
    """Generate a collection name from a URL."""
    parsed = urlparse(url)
    domain = parsed.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    if "." in domain:
        domain = domain.rsplit(".", 1)[0]

    clean_name = re.sub(r"[^a-zA-Z0-9_]", "_", domain)
    return clean_name.lower()


def is_url(path: str) -> bool:
    """Check if a path is a URL."""
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


async def ingest_to_graphiti(doc_dir: Path, collection_name: str, job_id: str = None):
    """Ingest markdown files from directory to Graphiti."""
    if not Graphiti:
        logger.error("Graphiti not available")
        if job_id and job_id in INGESTION_STATE:
            INGESTION_STATE[job_id]["status"] = "failed"
            INGESTION_STATE[job_id]["error"] = "Graphiti not available"
        return

    logger.info("Initializing Graphiti...")
    if job_id and job_id in INGESTION_STATE:
        INGESTION_STATE[job_id]["current_step"] = "Initializing Graphiti"

    resources = create_graphiti_resources(
        provider=DEFAULT_PROVIDER,
        model_id=DEFAULT_MODEL_ID,
        base_url=DEFAULT_LLM_BASE_URL,
        api_key=DEFAULT_LLM_API_KEY,
        graph_name=DEFAULT_GRAPHDB_NAME,
    )

    graphiti = Graphiti(
        uri=DEFAULT_GRAPHDB_URI,
        user=DEFAULT_GRAPHDB_USERNAME,
        password=DEFAULT_GRAPHDB_PASSWORD,
        llm_client=resources.get("llm_client"),
        embedder=resources.get("embedder"),
        cross_encoder=resources.get("cross_encoder"),
        graph_driver=resources.get("graph_driver"),
    )

    try:
        await graphiti.build_indices_and_constraints()
    except Exception as e:
        logger.error(f"Failed to build indices/constraints: {e}")

    if job_id and job_id in INGESTION_STATE:
        INGESTION_STATE[job_id]["current_step"] = "Reading files"

    md_files = list(doc_dir.glob("**/*.md")) + list(doc_dir.glob("**/*.mdx"))
    logger.info(f"Found {len(md_files)} markdown files to ingest.")

    episodes = []
    for file in md_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            episodes.append(
                RawEpisode(
                    name=file.stem,
                    content=content,
                    source=EpisodeType.text,
                    source_description="Documentation page",
                    reference_time=datetime.now(timezone.utc),
                )
            )
        except Exception as e:
            logger.error(f"Failed to read file {file}: {e}")

    if episodes:
        total_episodes = len(episodes)
        logger.info(f"Ingesting {total_episodes} episodes to Graphiti...")

        if job_id and job_id in INGESTION_STATE:
            INGESTION_STATE[job_id]["total"] = total_episodes
            INGESTION_STATE[job_id]["current_step"] = "Ingesting to Graphiti"

        CHUNK_SIZE = 10
        chunks = [
            episodes[i : i + CHUNK_SIZE] for i in range(0, total_episodes, CHUNK_SIZE)
        ]

        for i, chunk in enumerate(chunks):
            try:
                logger.info(
                    f"Ingesting chunk {i+1}/{len(chunks)} ({len(chunk)} episodes)..."
                )
                await graphiti.add_episode_bulk(chunk, group_id=collection_name)

                if job_id and job_id in INGESTION_STATE:
                    processed = min((i + 1) * CHUNK_SIZE, total_episodes)
                    INGESTION_STATE[job_id]["processed"] = processed

            except Exception as e:
                logger.error(f"Failed to ingest chunk {i}: {e}")
                if job_id and job_id in INGESTION_STATE:
                    INGESTION_STATE[job_id]["error"] = f"Chunk {i} failed: {str(e)}"

        logger.info("Graphiti ingestion complete.")


async def call_vector_mcp_create_collection(
    collection_name: str,
    document_directory: str = os.path.normpath("/documents"),
    db_type: str = DEFAULT_DATABASE_TYPE,
):
    """Call Vector MCP to create a collection."""
    logger.info(f"Connecting to Vector MCP at {VECTOR_MCP_URL}...")

    try:
        async with Client(VECTOR_MCP_URL) as client:
            logger.info(f"Calling create_collection for {collection_name}...")
            result = await client.call_tool(
                "create_collection",
                arguments={
                    "collection_name": collection_name,
                    "overwrite": True,
                    "document_directory": document_directory,
                    "db_type": db_type,
                },
            )
            logger.info(f"Vector MCP Result: {result}")
            return result
    except Exception as e:
        logger.error(f"Failed to call Vector MCP: {e}")
        raise RuntimeError(f"Vector MCP interaction failed: {e}")


async def call_documentdb_mcp_insert(
    collection_name: str,
    doc_dir: Path,
    job_id: str = None,
):
    """
    Reads markdown files from doc_dir and inserts them into DocumentDB.
    """
    logger.info(f"Connecting to DocumentDB MCP at {DOCUMENTDB_MCP_URL}...")

    if not DOCUMENTDB_MCP_URL:
        logger.warning("DOCUMENTDB_MCP_URL not set, skipping DocumentDB ingestion.")
        return

    try:
        # 1. Create Collection (if not exists)
        async with Client(DOCUMENTDB_MCP_URL) as client:
            # We don't have an explicit create_collection in the list effectively,
            # but usually MongoDB creates specific collections implicitly on insert.
            # However, the README says 'create_collection' is a tool.
            # Let's try to create it to be safe, or just insert.
            # The user request says: "add those documents to documentdb in a named collection"
            try:
                await client.call_tool(
                    "create_collection",
                    arguments={
                        "collection_name": collection_name,
                        "database_name": "genius",
                    },
                )
            except Exception as e:
                # Ignore if it already exists or if tool fails, we'll try insert anyway
                logger.warning(f"Failed to create collection (might exist): {e}")

            # 2. Iterate and Insert
            md_files = list(doc_dir.glob("**/*.md")) + list(doc_dir.glob("**/*.mdx"))
            logger.info(f"Found {len(md_files)} files for DocumentDB ingestion.")

            inserted_count = 0
            for file_path in md_files:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    document = {
                        "filename": file_path.name,
                        "path": str(file_path),
                        "content": content,
                        "ingestion_job_id": job_id,
                        "ingested_at": datetime.now(timezone.utc).isoformat(),
                    }

                    await client.call_tool(
                        "insert_one",
                        arguments={
                            "collection_name": collection_name,
                            "document": document,
                            "database_name": "genius",
                        },
                    )
                    inserted_count += 1
                except Exception as e:
                    logger.error(f"Failed to insert file {file_path.name}: {e}")

            logger.info(f"Inserted {inserted_count} documents into DocumentDB.")

    except Exception as e:
        logger.error(f"Failed to call DocumentDB MCP: {e}")
        # We don't raise here to allow other ingestions to proceed
        if job_id and job_id in INGESTION_STATE:
            current_err = INGESTION_STATE[job_id].get("error", "")
            sep = " | " if current_err else ""
            INGESTION_STATE[job_id][
                "error"
            ] = f"{current_err}{sep}DocumentDB failed: {e}"


async def process_ingestion_background(
    doc_dir_path: Path, collection_name: str, job_id: str
):
    """
    Background task to handle Graphiti ingestion and Vector MCP update.
    This is run in the background to avoid timing out the main MCP tool call.
    """
    logger.info(
        f"Background task started for collection: {collection_name}, Job ID: {job_id}"
    )

    if job_id in INGESTION_STATE:
        INGESTION_STATE[job_id]["status"] = "running"

    if job_id in INGESTION_STATE:
        INGESTION_STATE[job_id]["status"] = "running"
        INGESTION_STATE[job_id][
            "current_step"
        ] = "Ingesting to Graphiti, Vector DB & DocumentDB"

    async def run_graphiti():
        logger.info("Starting Graphiti ingestion...")
        if job_id in INGESTION_STATE:
            INGESTION_STATE[job_id]["graph_status"] = "running"
        try:
            await ingest_to_graphiti(
                doc_dir_path, collection_name=collection_name, job_id=job_id
            )
            if job_id in INGESTION_STATE:
                INGESTION_STATE[job_id]["graph_status"] = "completed"
        except Exception as e:
            logger.error(f"Graphiti ingestion failed: {e}")
            if job_id in INGESTION_STATE:
                INGESTION_STATE[job_id]["error"] = str(e)
                INGESTION_STATE[job_id]["graph_status"] = "failed"

    async def run_vector_mcp():
        logger.info("Calling Vector MCP...")
        if job_id in INGESTION_STATE:
            INGESTION_STATE[job_id]["vector_status"] = "running"
        try:
            await call_vector_mcp_create_collection(
                collection_name=collection_name, document_directory=str(doc_dir_path)
            )
            logger.info("Vector MCP collection creation requested successfully.")
            if job_id in INGESTION_STATE:
                INGESTION_STATE[job_id]["vector_status"] = "completed"
        except Exception as e:
            logger.error(f"Vector MCP failed: {e}")
            if job_id in INGESTION_STATE:
                current_err = INGESTION_STATE[job_id].get("error", "")
                sep = " | " if current_err else ""
                INGESTION_STATE[job_id][
                    "error"
                ] = f"{current_err}{sep}Vector MCP failed: {e}"
                INGESTION_STATE[job_id]["vector_status"] = "failed"

    async def run_documentdb_mcp():
        logger.info("Starting DocumentDB ingestion...")
        if job_id in INGESTION_STATE:
            INGESTION_STATE[job_id]["document_status"] = "running"
        try:
            await call_documentdb_mcp_insert(
                collection_name=collection_name, doc_dir=doc_dir_path, job_id=job_id
            )
            if job_id in INGESTION_STATE:
                INGESTION_STATE[job_id]["document_status"] = "completed"
        except Exception as e:
            logger.error(f"DocumentDB ingestion failed: {e}")
            if job_id in INGESTION_STATE:
                INGESTION_STATE[job_id]["document_status"] = "failed"

    await asyncio.gather(run_graphiti(), run_vector_mcp(), run_documentdb_mcp())

    if job_id in INGESTION_STATE:
        INGESTION_STATE[job_id]["status"] = "completed"
        INGESTION_STATE[job_id]["current_step"] = "Finished"

    logger.info("Background ingestion task finished.")


def register_tools(mcp: FastMCP):
    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    @mcp.tool(
        annotations={
            "title": "Get Ingestion Progress",
            "description": "Check the progress of a background ingestion job.",
        }
    )
    async def get_ingestion_progress(
        job_id: Optional[str] = Field(
            description="The Job ID of the ingestion task", default=None
        ),
        collection_name: Optional[str] = Field(
            description="Filter by collection name", default=None
        ),
    ) -> Dict[str, Any]:
        """
        Returns the current state of ingestion jobs.
        """
        if job_id:
            state = INGESTION_STATE.get(job_id)
            if not state:
                return {"status": 404, "error": "Job ID not found"}
            return state

        if collection_name:
            matches = [
                s
                for s in INGESTION_STATE.values()
                if s.get("collection") == collection_name
            ]
            if not matches:
                return {"status": 404, "error": "No jobs found for collection"}
            return matches[-1]

        running_jobs = {
            k: v for k, v in INGESTION_STATE.items() if v["status"] == "running"
        }
        return {
            "running_jobs": running_jobs,
            "total_jobs_tracked": len(INGESTION_STATE),
        }

    @mcp.tool(
        annotations={
            "title": "Ingest Documentation",
            "description": "Recursively crawl a URL, save as markdown, and ingest to Graphiti, Vector DB & DocumentDB. (Crawls in foreground, Ingests in background). CRITICAL: Ingestion is a background task. Inform the user it has started and then TERMINATE your turn. Do NOT poll for progress.",
        }
    )
    async def ingest(
        path: List[str] = Field(
            description="List of URLs or local file paths to ingest", default=[]
        ),
        crawl: bool = Field(
            description="Whether to crawl the URLs found in the path list. If False, only the specific URL pages are ingested.",
            default=False,
        ),
        collection_name: Optional[str] = Field(
            description="Name of the collection. Generated from first URL/path if not provided.",
            default="memory",
        ),
        document_directory: str = Field(
            description="Directory to ingest documents from. This is also the directory that crawled URLs get saved to as Markdown",
            default=DEFAULT_DOCUMENTS_DIRECTORY,
        ),
        collections_directory: str = Field(
            description="This is the directory that we will store our organized collections. There will be a directory with the collection name and all documents in that collection in the directory.",
            default=DEFAULT_COLLECTIONS_DIRECTORY,
        ),
        max_depth: int = Field(
            description="Maximum depth to crawl recursively if crawl is True. Default: 3",
            default=3,
        ),
        max_concurrent: int = Field(
            description="Max concurrent pages to crawl. Default: 6", default=6
        ),
        ctx: Context = Field(default=None),
    ) -> Dict[str, Any]:
        """
        Ingests documentation from a list of URLs and/or local file paths.
        1. Processes each item in `path`:
           - If URL and crawl=True: Recursively crawls (up to max_depth).
           - If URL and crawl=False: Scrapes single page.
           - If Directory: Ingests all .md/.mdx files recursively.
           - If File: Ingests the specific file.
        2. Saves content to `document_directory`.
        3. Triggers BACKGROUND task for Graphiti, Vector DB & DocumentDB ingestion.
        """
        logger.info(f"Starting ingestion for {len(path)} paths, crawl={crawl}")

        # Determine effective depth for URLs
        crawl_depth = max_depth if crawl else 1

        # Generate collection name if needed
        if not collection_name or collection_name == "memory":
            # Try to get a meaningful name from the first item
            if path:
                first_item = path[0]
                if is_url(first_item):
                    collection_name = get_collection_name_from_url(first_item)
                else:
                    collection_name = Path(first_item).stem.lower()

            if not collection_name:
                collection_name = (
                    f"ingest_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
                )

            # Sanitize
            collection_name = re.sub(r"[^a-zA-Z0-9_]", "_", collection_name).lower()
            logger.info(f"Generated collection name: {collection_name}")

        # Create subdirectory for the collection in the collections directory
        # This keeps the source /documents directory clean
        collection_dir_path = Path(collections_directory) / collection_name
        collection_dir_path.mkdir(parents=True, exist_ok=True)

        # We also need to know the document directory to check if we should move or copy
        source_doc_dir = Path(document_directory)

        if ctx:
            await ctx.report_progress(10, 100)

        total_saved = 0
        urls_to_process = []

        # 1. Process Local Paths & Collect URLs
        for p in path:
            if is_url(p):
                urls_to_process.append(p)
            else:
                local_path = Path(p)
                if not local_path.exists():
                    logger.warning(f"Path does not exist: {p}")
                    continue

                if local_path.is_file():
                    try:
                        # Use filename directly inside collection folder
                        dest_name = local_path.name
                        dest_path = collection_dir_path / dest_name

                        # Decide whether to move or copy
                        # If file is in source_doc_dir, we MOVE it to keep source clean
                        # Otherwise we COPY it
                        is_in_doc_dir = False
                        try:
                            # Check if local_path is relative to source_doc_dir
                            local_path.relative_to(source_doc_dir)
                            is_in_doc_dir = True
                        except ValueError:
                            is_in_doc_dir = False

                        if is_in_doc_dir:
                            shutil.move(str(local_path), str(dest_path))
                            logger.info(f"Moved file: {local_path} -> {dest_path}")
                        else:
                            shutil.copy2(local_path, dest_path)
                            logger.info(f"Copied file: {local_path} -> {dest_path}")

                        total_saved += 1
                    except Exception as e:
                        logger.error(f"Failed to process file {local_path}: {e}")

                elif local_path.is_dir():
                    # Walk directory for .md and .mdx
                    for ext in ["**/*.md", "**/*.mdx"]:
                        for f in local_path.glob(ext):
                            if f.is_file():
                                try:
                                    # Create a unique name to avoid collisions
                                    rel_path = f.relative_to(local_path)
                                    safe_rel_path = str(rel_path).replace(os.sep, "_")
                                    # Use relative path as filename inside collection folder
                                    dest_name = safe_rel_path
                                    dest_path = collection_dir_path / dest_name
                                    shutil.copy2(f, dest_path)
                                    total_saved += 1
                                except Exception as e:
                                    logger.error(f"Failed to copy from dir {f}: {e}")

        # 2. Process URLs with Crawl4AI
        if urls_to_process:
            logger.info(
                f"Processing {len(urls_to_process)} URLs with crawl={crawl}, depth={crawl_depth}"
            )

            if AsyncWebCrawler:
                browser_config = BrowserConfig(
                    headless=True,
                    verbose=False,
                    extra_args=[
                        "--disable-gpu",
                        "--disable-dev-shm-usage",
                        "--no-sandbox",
                    ],
                )
                run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
                dispatcher = MemoryAdaptiveDispatcher(
                    memory_threshold_percent=70.0,
                    check_interval=1.0,
                    max_session_permit=max_concurrent,
                )

                visited = set()

                def normalize_url(u):
                    return urldefrag(u)[0]

                # We can't easily do a single 'arun_many' for all if they have different domains and we want recursive.
                # But we can loop over them or batch them by domain.
                # For simplicity, let's treat each root URL as a start point for a crawl session.
                # To support mixed domains in one go, we can just add all to the initial queue.

                current_urls = {normalize_url(u) for u in urls_to_process}

                # We need to track approved domains for recursion
                # If crawl=True, we typically only want to crawl within the same domains as the inputs.
                allowed_domains = {urlparse(u).netloc for u in urls_to_process}

                async with AsyncWebCrawler(config=browser_config) as crawler:
                    for depth in range(crawl_depth):
                        logger.info(
                            f"Crawling Depth {depth+1}, URLs: {len(current_urls)}"
                        )
                        if ctx:
                            await ctx.report_progress(
                                20 + int((depth + 1) / crawl_depth * 60), 100
                            )

                        urls_to_crawl = []
                        for u in current_urls:
                            if u not in visited:
                                # Start or same domain check
                                if depth == 0 or urlparse(u).netloc in allowed_domains:
                                    urls_to_crawl.append(u)

                        if not urls_to_crawl:
                            break

                        results = await crawler.arun_many(
                            urls=urls_to_crawl, config=run_config, dispatcher=dispatcher
                        )

                        next_level_urls = set()
                        for result in results:
                            norm_url = normalize_url(result.url)
                            visited.add(norm_url)

                            if result.success and result.markdown:
                                path_slug = (
                                    urlparse(norm_url).path.strip("/").replace("/", "_")
                                    or "index"
                                )
                                if not path_slug.endswith(".md"):
                                    path_slug += ".md"
                                # Use path_slug directly as filename inside collection folder
                                filename = path_slug
                                filename = re.sub(r"[^a-zA-Z0-9_\-\.]", "", filename)

                                file_path = os.path.join(collection_dir_path, filename)
                                try:
                                    with open(file_path, "w", encoding="utf-8") as f:
                                        f.write(result.markdown.raw_markdown)
                                    total_saved += 1
                                except Exception as e:
                                    logger.error(f"Failed to save {norm_url}: {e}")

                                if (
                                    crawl
                                ):  # Only collect links if we are crawling recursively
                                    links = result.links.get("internal", [])
                                    for link in links:
                                        next_url = normalize_url(link["href"])
                                        if next_url not in visited:
                                            next_level_urls.add(next_url)
                            else:
                                logger.error(
                                    f"Failed to crawl {norm_url}: {result.error_message}"
                                )

                        current_urls = next_level_urls

                logger.info(
                    f"Crawl complete. Total files saved (local+web): {total_saved}"
                )
            else:
                logger.error("Crawl4AI not installed, skipping URL crawl step.")
                # We don't error out entirely if we processed local files, but should warn.
                if not total_saved and not urls_to_process:
                    return {
                        "status": 500,
                        "error": "Crawl4AI not installed and no local files found",
                    }

        job_id = str(uuid.uuid4())

        INGESTION_STATE[job_id] = {
            "status": "pending",
            "collection": collection_name,
            "total": 0,
            "processed": 0,
            "current_step": "Starting",
            "graph_status": "pending",
            "vector_status": "pending",
            "document_status": "pending",
            "start_time": datetime.now(timezone.utc).isoformat(),
        }

        asyncio.create_task(
            process_ingestion_background(collection_dir_path, collection_name, job_id)
        )

        if ctx:
            await ctx.report_progress(100, 100)

        response = {
            "status": 200,
            "message": "Recursive crawl complete. Background ingestion started.",
            "job_id": job_id,
            "collection": collection_name,
            "directory": str(collection_dir_path),
            "files_saved": total_saved,
            "note": "INGESTION IS RUNNING IN THE BACKGROUND. Inform the user that ingestion has started and provided the job_id, then END YOUR TURN. Do not call get_ingestion_progress unless the user asks in a NEW query.",
        }

        if job_id in INGESTION_STATE:
            response.update(INGESTION_STATE[job_id])
            logger.info(f"Ingestion response: {response}")
            # Get global stats directly from state to avoid Field default issues
            running_jobs = {
                k: v for k, v in INGESTION_STATE.items() if v.get("status") == "running"
            }
            response["running_jobs"] = running_jobs
            response["total_jobs_tracked"] = len(INGESTION_STATE)

        return response


def genius_agent_mcp():
    print(f"genius_mcp v{__version__}")
    import argparse

    parser = argparse.ArgumentParser(
        add_help=False, description="Genius Agent MCP Server"
    )
    parser.add_argument(
        "-t",
        "--transport",
        default=DEFAULT_TRANSPORT,
        choices=["stdio", "streamable-http", "sse"],
        help="Transport method",
    )
    parser.add_argument("-s", "--host", default=DEFAULT_HOST, help="Host address")
    parser.add_argument(
        "-p", "--port", type=int, default=DEFAULT_PORT, help="Port number"
    )

    parser.add_argument("--auth-type", default="none")
    parser.add_argument("--token-jwks-uri", default=None)
    parser.add_argument("--token-issuer", default=None)
    parser.add_argument("--token-audience", default=None)

    args, unknown = parser.parse_known_args()

    mcp = FastMCP(name="GeniusAgentMCP")
    register_tools(mcp)

    print(f"Starting Genius Agent MCP on {args.host}:{args.port}")

    if args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    genius_agent_mcp()
