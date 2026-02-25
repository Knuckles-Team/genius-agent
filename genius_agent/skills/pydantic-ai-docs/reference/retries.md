[ Skip to content ](https://ai.pydantic.dev/retries/#http-request-retries)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
HTTP Request Retries
Type to start searching
[ pydantic/pydantic-ai
  * v1.63.0
  * 15.1k
  * 1.7k

](https://github.com/pydantic/pydantic-ai "Go to repository")
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI") Pydantic AI
[ pydantic/pydantic-ai
  * v1.63.0
  * 15.1k
  * 1.7k

](https://github.com/pydantic/pydantic-ai "Go to repository")
  * [ Pydantic AI  ](https://ai.pydantic.dev/)
  * [ Installation  ](https://ai.pydantic.dev/install/)
  * [ Getting Help  ](https://ai.pydantic.dev/help/)
  * [ Troubleshooting  ](https://ai.pydantic.dev/troubleshooting/)
  * [ Pydantic AI Gateway  ](https://ai.pydantic.dev/gateway/)
  * Documentation
    * Core Concepts
      * [ Agents  ](https://ai.pydantic.dev/agent/)
      * [ Dependencies  ](https://ai.pydantic.dev/dependencies/)
      * [ Function Tools  ](https://ai.pydantic.dev/tools/)
      * [ Output  ](https://ai.pydantic.dev/output/)
      * [ Messages and chat history  ](https://ai.pydantic.dev/message-history/)
      * [ Direct Model Requests  ](https://ai.pydantic.dev/direct/)
    * Models & Providers
      * [ Overview  ](https://ai.pydantic.dev/models/overview/)
      * [ OpenAI  ](https://ai.pydantic.dev/models/openai/)
      * [ Anthropic  ](https://ai.pydantic.dev/models/anthropic/)
      * [ Google  ](https://ai.pydantic.dev/models/google/)
      * [ xAI  ](https://ai.pydantic.dev/models/xai/)
      * [ Bedrock  ](https://ai.pydantic.dev/models/bedrock/)
      * [ Cerebras  ](https://ai.pydantic.dev/models/cerebras/)
      * [ Cohere  ](https://ai.pydantic.dev/models/cohere/)
      * [ Groq  ](https://ai.pydantic.dev/models/groq/)
      * [ Hugging Face  ](https://ai.pydantic.dev/models/huggingface/)
      * [ Mistral  ](https://ai.pydantic.dev/models/mistral/)
      * [ OpenRouter  ](https://ai.pydantic.dev/models/openrouter/)
      * [ Outlines  ](https://ai.pydantic.dev/models/outlines/)
    * Tools & Toolsets
      * [ Function Tools  ](https://ai.pydantic.dev/tools/)
      * [ Advanced Tool Features  ](https://ai.pydantic.dev/tools-advanced/)
      * [ Toolsets  ](https://ai.pydantic.dev/toolsets/)
      * [ Deferred Tools  ](https://ai.pydantic.dev/deferred-tools/)
      * [ Built-in Tools  ](https://ai.pydantic.dev/builtin-tools/)
      * [ Common Tools  ](https://ai.pydantic.dev/common-tools/)
      * [ Third-Party Tools  ](https://ai.pydantic.dev/third-party-tools/)
    * Advanced Features
      * [ Image, Audio, Video & Document Input  ](https://ai.pydantic.dev/input/)
      * [ Thinking  ](https://ai.pydantic.dev/thinking/)
      * HTTP Request Retries  [ HTTP Request Retries  ](https://ai.pydantic.dev/retries/)
        * [ Overview  ](https://ai.pydantic.dev/retries/#overview)
        * [ Installation  ](https://ai.pydantic.dev/retries/#installation)
        * [ Usage Example  ](https://ai.pydantic.dev/retries/#usage-example)
        * [ Wait Strategies  ](https://ai.pydantic.dev/retries/#wait-strategies)
          * [ wait_retry_after  ](https://ai.pydantic.dev/retries/#wait_retry_after)
        * [ Transport Classes  ](https://ai.pydantic.dev/retries/#transport-classes)
          * [ AsyncTenacityTransport  ](https://ai.pydantic.dev/retries/#asynctenacitytransport)
          * [ TenacityTransport  ](https://ai.pydantic.dev/retries/#tenacitytransport)
        * [ Common Retry Patterns  ](https://ai.pydantic.dev/retries/#common-retry-patterns)
          * [ Rate Limit Handling with Retry-After Support  ](https://ai.pydantic.dev/retries/#rate-limit-handling-with-retry-after-support)
          * [ Network Error Handling  ](https://ai.pydantic.dev/retries/#network-error-handling)
          * [ Custom Retry Logic  ](https://ai.pydantic.dev/retries/#custom-retry-logic)
        * [ Using with Different Providers  ](https://ai.pydantic.dev/retries/#using-with-different-providers)
          * [ OpenAI  ](https://ai.pydantic.dev/retries/#openai)
          * [ Anthropic  ](https://ai.pydantic.dev/retries/#anthropic)
          * [ Any OpenAI-Compatible Provider  ](https://ai.pydantic.dev/retries/#any-openai-compatible-provider)
        * [ Best Practices  ](https://ai.pydantic.dev/retries/#best-practices)
        * [ Error Handling  ](https://ai.pydantic.dev/retries/#error-handling)
        * [ Performance Considerations  ](https://ai.pydantic.dev/retries/#performance-considerations)
        * [ Provider-Specific Retry Behavior  ](https://ai.pydantic.dev/retries/#provider-specific-retry-behavior)
          * [ AWS Bedrock  ](https://ai.pydantic.dev/retries/#aws-bedrock)
    * MCP
      * [ Overview  ](https://ai.pydantic.dev/mcp/overview/)
      * [ Client  ](https://ai.pydantic.dev/mcp/client/)
      * [ FastMCP Client  ](https://ai.pydantic.dev/mcp/fastmcp-client/)
      * [ Server  ](https://ai.pydantic.dev/mcp/server/)
    * [ Multi-Agent Patterns  ](https://ai.pydantic.dev/multi-agent-applications/)
    * [ Web Chat UI  ](https://ai.pydantic.dev/web/)
    * [ Embeddings  ](https://ai.pydantic.dev/embeddings/)
    * [ Testing  ](https://ai.pydantic.dev/testing/)
  * Pydantic Evals
    * [ Overview  ](https://ai.pydantic.dev/evals/)
    * Getting Started
      * [ Quick Start  ](https://ai.pydantic.dev/evals/quick-start/)
      * [ Core Concepts  ](https://ai.pydantic.dev/evals/core-concepts/)
    * Evaluators
      * [ Overview  ](https://ai.pydantic.dev/evals/evaluators/overview/)
      * [ Built-in Evaluators  ](https://ai.pydantic.dev/evals/evaluators/built-in/)
      * [ LLM Judge  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/)
      * [ Custom Evaluators  ](https://ai.pydantic.dev/evals/evaluators/custom/)
      * [ Report Evaluators  ](https://ai.pydantic.dev/evals/evaluators/report-evaluators/)
      * [ Span-Based  ](https://ai.pydantic.dev/evals/evaluators/span-based/)
    * How-To Guides
      * [ Logfire Integration  ](https://ai.pydantic.dev/evals/how-to/logfire-integration/)
      * [ Dataset Management  ](https://ai.pydantic.dev/evals/how-to/dataset-management/)
      * [ Dataset Serialization  ](https://ai.pydantic.dev/evals/how-to/dataset-serialization/)
      * [ Concurrency & Performance  ](https://ai.pydantic.dev/evals/how-to/concurrency/)
      * [ Multi-Run Evaluation  ](https://ai.pydantic.dev/evals/how-to/multi-run/)
      * [ Retry Strategies  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/)
      * [ Metrics & Attributes  ](https://ai.pydantic.dev/evals/how-to/metrics-attributes/)
    * Examples
      * [ Simple Validation  ](https://ai.pydantic.dev/evals/examples/simple-validation/)
  * Pydantic Graph
    * [ Overview  ](https://ai.pydantic.dev/graph/)
    * [ Beta API  ](https://ai.pydantic.dev/graph/beta/)
      * [ Steps  ](https://ai.pydantic.dev/graph/beta/steps/)
      * [ Joins & Reducers  ](https://ai.pydantic.dev/graph/beta/joins/)
      * [ Decisions  ](https://ai.pydantic.dev/graph/beta/decisions/)
      * [ Parallel Execution  ](https://ai.pydantic.dev/graph/beta/parallel/)
  * Integrations
    * [ Debugging & Monitoring with Pydantic Logfire  ](https://ai.pydantic.dev/logfire/)
    * Durable Execution
      * [ Overview  ](https://ai.pydantic.dev/durable_execution/overview/)
      * [ Temporal  ](https://ai.pydantic.dev/durable_execution/temporal/)
      * [ DBOS  ](https://ai.pydantic.dev/durable_execution/dbos/)
      * [ Prefect  ](https://ai.pydantic.dev/durable_execution/prefect/)
    * UI Event Streams
      * [ Overview  ](https://ai.pydantic.dev/ui/overview/)
      * [ AG-UI  ](https://ai.pydantic.dev/ui/ag-ui/)
      * [ Vercel AI  ](https://ai.pydantic.dev/ui/vercel-ai/)
    * [ Agent2Agent (A2A)  ](https://ai.pydantic.dev/a2a/)
  * Related Packages
    * [ clai  ](https://ai.pydantic.dev/cli/)
  * Examples
    * [ Setup  ](https://ai.pydantic.dev/examples/setup/)
    * Getting Started
      * [ Pydantic Model  ](https://ai.pydantic.dev/examples/pydantic-model/)
      * [ Weather agent  ](https://ai.pydantic.dev/examples/weather-agent/)
    * Conversational Agents
      * [ Chat App with FastAPI  ](https://ai.pydantic.dev/examples/chat-app/)
      * [ Bank support  ](https://ai.pydantic.dev/examples/bank-support/)
    * Data & Analytics
      * [ SQL Generation  ](https://ai.pydantic.dev/examples/sql-gen/)
      * [ Data Analyst  ](https://ai.pydantic.dev/examples/data-analyst/)
      * [ RAG  ](https://ai.pydantic.dev/examples/rag/)
    * Streaming
      * [ Stream markdown  ](https://ai.pydantic.dev/examples/stream-markdown/)
      * [ Stream whales  ](https://ai.pydantic.dev/examples/stream-whales/)
    * Complex Workflows
      * [ Flight booking  ](https://ai.pydantic.dev/examples/flight-booking/)
      * [ Question Graph  ](https://ai.pydantic.dev/examples/question-graph/)
    * Business Applications
      * [ Slack Lead Qualifier with Modal  ](https://ai.pydantic.dev/examples/slack-lead-qualifier/)
    * UI Examples
      * [ Agent User Interaction (AG-UI)  ](https://ai.pydantic.dev/examples/ag-ui/)
  * API Reference
    * pydantic_ai
      * [ pydantic_ai.ag_ui  ](https://ai.pydantic.dev/api/ag_ui/)
      * [ pydantic_ai.agent  ](https://ai.pydantic.dev/api/agent/)
      * [ pydantic_ai.builtin_tools  ](https://ai.pydantic.dev/api/builtin_tools/)
      * [ pydantic_ai.common_tools  ](https://ai.pydantic.dev/api/common_tools/)
      * [ pydantic_ai — Concurrency  ](https://ai.pydantic.dev/api/concurrency/)
      * [ pydantic_ai.direct  ](https://ai.pydantic.dev/api/direct/)
      * [ pydantic_ai.durable_exec  ](https://ai.pydantic.dev/api/durable_exec/)
      * [ pydantic_ai.embeddings  ](https://ai.pydantic.dev/api/embeddings/)
      * [ pydantic_ai.exceptions  ](https://ai.pydantic.dev/api/exceptions/)
      * [ pydantic_ai.ext  ](https://ai.pydantic.dev/api/ext/)
      * [ pydantic_ai.format_prompt  ](https://ai.pydantic.dev/api/format_prompt/)
      * [ pydantic_ai.mcp  ](https://ai.pydantic.dev/api/mcp/)
      * [ pydantic_ai.messages  ](https://ai.pydantic.dev/api/messages/)
      * [ pydantic_ai.models.anthropic  ](https://ai.pydantic.dev/api/models/anthropic/)
      * [ pydantic_ai.models  ](https://ai.pydantic.dev/api/models/base/)
      * [ pydantic_ai.models.bedrock  ](https://ai.pydantic.dev/api/models/bedrock/)
      * [ pydantic_ai.models.cerebras  ](https://ai.pydantic.dev/api/models/cerebras/)
      * [ pydantic_ai.models.cohere  ](https://ai.pydantic.dev/api/models/cohere/)
      * [ pydantic_ai.models.fallback  ](https://ai.pydantic.dev/api/models/fallback/)
      * [ pydantic_ai.models.function  ](https://ai.pydantic.dev/api/models/function/)
      * [ pydantic_ai.models.google  ](https://ai.pydantic.dev/api/models/google/)
      * [ pydantic_ai.models.xai  ](https://ai.pydantic.dev/api/models/xai/)
      * [ pydantic_ai.models.groq  ](https://ai.pydantic.dev/api/models/groq/)
      * [ pydantic_ai.models.huggingface  ](https://ai.pydantic.dev/api/models/huggingface/)
      * [ pydantic_ai.models.instrumented  ](https://ai.pydantic.dev/api/models/instrumented/)
      * [ pydantic_ai.models.mcp_sampling  ](https://ai.pydantic.dev/api/models/mcp-sampling/)
      * [ pydantic_ai.models.mistral  ](https://ai.pydantic.dev/api/models/mistral/)
      * [ pydantic_ai.models.openai  ](https://ai.pydantic.dev/api/models/openai/)
      * [ pydantic_ai.models.openrouter  ](https://ai.pydantic.dev/api/models/openrouter/)
      * [ pydantic_ai.models.outlines  ](https://ai.pydantic.dev/api/models/outlines/)
      * [ pydantic_ai.models.test  ](https://ai.pydantic.dev/api/models/test/)
      * [ pydantic_ai.models.wrapper  ](https://ai.pydantic.dev/api/models/wrapper/)
      * [ pydantic_ai.output  ](https://ai.pydantic.dev/api/output/)
      * [ pydantic_ai.profiles  ](https://ai.pydantic.dev/api/profiles/)
      * [ pydantic_ai.providers  ](https://ai.pydantic.dev/api/providers/)
      * [ pydantic_ai.result  ](https://ai.pydantic.dev/api/result/)
      * [ pydantic_ai.retries  ](https://ai.pydantic.dev/api/retries/)
      * [ pydantic_ai.run  ](https://ai.pydantic.dev/api/run/)
      * [ pydantic_ai.settings  ](https://ai.pydantic.dev/api/settings/)
      * [ pydantic_ai.tools  ](https://ai.pydantic.dev/api/tools/)
      * [ pydantic_ai.toolsets  ](https://ai.pydantic.dev/api/toolsets/)
      * [ pydantic_ai.ui.ag_ui  ](https://ai.pydantic.dev/api/ui/ag_ui/)
      * [ pydantic_ai.ui  ](https://ai.pydantic.dev/api/ui/base/)
      * [ pydantic_ai.ui.vercel_ai  ](https://ai.pydantic.dev/api/ui/vercel_ai/)
      * [ pydantic_ai.usage  ](https://ai.pydantic.dev/api/usage/)
    * pydantic_evals
      * [ pydantic_evals.dataset  ](https://ai.pydantic.dev/api/pydantic_evals/dataset/)
      * [ pydantic_evals.evaluators  ](https://ai.pydantic.dev/api/pydantic_evals/evaluators/)
      * [ pydantic_evals.reporting  ](https://ai.pydantic.dev/api/pydantic_evals/reporting/)
      * [ pydantic_evals.otel  ](https://ai.pydantic.dev/api/pydantic_evals/otel/)
      * [ pydantic_evals.generation  ](https://ai.pydantic.dev/api/pydantic_evals/generation/)
    * pydantic_graph
      * [ pydantic_graph  ](https://ai.pydantic.dev/api/pydantic_graph/graph/)
      * [ pydantic_graph.nodes  ](https://ai.pydantic.dev/api/pydantic_graph/nodes/)
      * [ pydantic_graph.persistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/)
      * [ pydantic_graph.mermaid  ](https://ai.pydantic.dev/api/pydantic_graph/mermaid/)
      * [ pydantic_graph.exceptions  ](https://ai.pydantic.dev/api/pydantic_graph/exceptions/)
      * Beta API
        * [ pydantic_graph.beta  ](https://ai.pydantic.dev/api/pydantic_graph/beta/)
        * [ pydantic_graph.beta.graph  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/)
        * [ pydantic_graph.beta.graph_builder  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/)
        * [ pydantic_graph.beta.step  ](https://ai.pydantic.dev/api/pydantic_graph/beta_step/)
        * [ pydantic_graph.beta.join  ](https://ai.pydantic.dev/api/pydantic_graph/beta_join/)
        * [ pydantic_graph.beta.decision  ](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/)
        * [ pydantic_graph.beta.node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_node/)
    * fasta2a
      * [ fasta2a  ](https://ai.pydantic.dev/api/fasta2a/)
  * Project
    * [ Contributing  ](https://ai.pydantic.dev/contributing/)
    * [ Upgrade Guide  ](https://ai.pydantic.dev/changelog/)
    * [ Version policy  ](https://ai.pydantic.dev/version-policy/)


  * [ Overview  ](https://ai.pydantic.dev/retries/#overview)
  * [ Installation  ](https://ai.pydantic.dev/retries/#installation)
  * [ Usage Example  ](https://ai.pydantic.dev/retries/#usage-example)
  * [ Wait Strategies  ](https://ai.pydantic.dev/retries/#wait-strategies)
    * [ wait_retry_after  ](https://ai.pydantic.dev/retries/#wait_retry_after)
  * [ Transport Classes  ](https://ai.pydantic.dev/retries/#transport-classes)
    * [ AsyncTenacityTransport  ](https://ai.pydantic.dev/retries/#asynctenacitytransport)
    * [ TenacityTransport  ](https://ai.pydantic.dev/retries/#tenacitytransport)
  * [ Common Retry Patterns  ](https://ai.pydantic.dev/retries/#common-retry-patterns)
    * [ Rate Limit Handling with Retry-After Support  ](https://ai.pydantic.dev/retries/#rate-limit-handling-with-retry-after-support)
    * [ Network Error Handling  ](https://ai.pydantic.dev/retries/#network-error-handling)
    * [ Custom Retry Logic  ](https://ai.pydantic.dev/retries/#custom-retry-logic)
  * [ Using with Different Providers  ](https://ai.pydantic.dev/retries/#using-with-different-providers)
    * [ OpenAI  ](https://ai.pydantic.dev/retries/#openai)
    * [ Anthropic  ](https://ai.pydantic.dev/retries/#anthropic)
    * [ Any OpenAI-Compatible Provider  ](https://ai.pydantic.dev/retries/#any-openai-compatible-provider)
  * [ Best Practices  ](https://ai.pydantic.dev/retries/#best-practices)
  * [ Error Handling  ](https://ai.pydantic.dev/retries/#error-handling)
  * [ Performance Considerations  ](https://ai.pydantic.dev/retries/#performance-considerations)
  * [ Provider-Specific Retry Behavior  ](https://ai.pydantic.dev/retries/#provider-specific-retry-behavior)
    * [ AWS Bedrock  ](https://ai.pydantic.dev/retries/#aws-bedrock)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ Documentation  ](https://ai.pydantic.dev/agent/)
  3. [ Advanced Features  ](https://ai.pydantic.dev/input/)


# HTTP Request Retries
Pydantic AI provides retry functionality for HTTP requests made by model providers through custom HTTP transports. This is particularly useful for handling transient failures like rate limits, network timeouts, or temporary server errors.
## Overview
The retry functionality is built on top of the [tenacity](https://github.com/jd/tenacity) library and integrates seamlessly with httpx clients. You can configure retry behavior for any provider that accepts a custom HTTP client.
## Installation
To use the retry transports, you need to install `tenacity`, which you can do via the `retries` dependency group:
[pip](https://ai.pydantic.dev/retries/#__tabbed_1_1)[uv](https://ai.pydantic.dev/retries/#__tabbed_1_2)
```
pip install 'pydantic-ai-slim[retries]'

```

```
uv add 'pydantic-ai-slim[retries]'

```

## Usage Example
Here's an example of adding retry functionality with smart retry handling:
smart_retry_example.py```
from httpx import AsyncClient, HTTPStatusError
from tenacity import retry_if_exception_type, stop_after_attempt, wait_exponential

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after


def create_retrying_client():
    """Create a client with smart retry handling for multiple error types."""

    def should_retry_status(response):
        """Raise exceptions for retryable HTTP status codes."""
        if response.status_code in (429, 502, 503, 504):
            response.raise_for_status()  # This will raise HTTPStatusError

    transport = AsyncTenacityTransport(
        config=RetryConfig(
            # Retry on HTTP errors and connection issues
            retry=retry_if_exception_type((HTTPStatusError, ConnectionError)),
            # Smart waiting: respects Retry-After headers, falls back to exponential backoff
            wait=wait_retry_after(
                fallback_strategy=wait_exponential(multiplier=1, max=60),
                max_wait=300
            ),
            # Stop after 5 attempts
            stop=stop_after_attempt(5),
            # Re-raise the last exception if all retries fail
            reraise=True
        ),
        validate_response=should_retry_status
    )
    return AsyncClient(transport=transport)

# Use the retrying client with a model
client = create_retrying_client()
model = OpenAIChatModel('gpt-5.2', provider=OpenAIProvider(http_client=client))
agent = Agent(model)

```

## Wait Strategies
### wait_retry_after
The `wait_retry_after` function is a smart wait strategy that automatically respects HTTP `Retry-After` headers:
wait_strategy_example.py```
from tenacity import wait_exponential

from pydantic_ai.retries import wait_retry_after

# Basic usage - respects Retry-After headers, falls back to exponential backoff
wait_strategy_1 = wait_retry_after()

# Custom configuration
wait_strategy_2 = wait_retry_after(
    fallback_strategy=wait_exponential(multiplier=2, max=120),
    max_wait=600  # Never wait more than 10 minutes
)

```

This wait strategy:
  * Automatically parses `Retry-After` headers from HTTP 429 responses
  * Supports both seconds format (`"30"`) and HTTP date format (`"Wed, 21 Oct 2015 07:28:00 GMT"`)
  * Falls back to your chosen strategy when no header is present
  * Respects the `max_wait` limit to prevent excessive delays


## Transport Classes
### AsyncTenacityTransport
For asynchronous HTTP clients (recommended for most use cases):
async_transport_example.py```
from httpx import AsyncClient
from tenacity import stop_after_attempt

from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig


def validator(response):
    """Treat responses with HTTP status 4xx/5xx as failures that need to be retried.
    Without a response validator, only network errors and timeouts will result in a retry.
    """
    response.raise_for_status()

# Create the transport
transport = AsyncTenacityTransport(
    config=RetryConfig(stop=stop_after_attempt(3), reraise=True),
    validate_response=validator
)

# Create a client using the transport:
client = AsyncClient(transport=transport)

```

### TenacityTransport
For synchronous HTTP clients:
sync_transport_example.py```
from httpx import Client
from tenacity import stop_after_attempt

from pydantic_ai.retries import RetryConfig, TenacityTransport


def validator(response):
    """Treat responses with HTTP status 4xx/5xx as failures that need to be retried.
    Without a response validator, only network errors and timeouts will result in a retry.
    """
    response.raise_for_status()

# Create the transport
transport = TenacityTransport(
    config=RetryConfig(stop=stop_after_attempt(3), reraise=True),
    validate_response=validator
)

# Create a client using the transport
client = Client(transport=transport)

```

## Common Retry Patterns
### Rate Limit Handling with Retry-After Support
rate_limit_handling.py```
from httpx import AsyncClient, HTTPStatusError
from tenacity import retry_if_exception_type, stop_after_attempt, wait_exponential

from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after


def create_rate_limit_client():
    """Create a client that respects Retry-After headers from rate limiting responses."""
    transport = AsyncTenacityTransport(
        config=RetryConfig(
            retry=retry_if_exception_type(HTTPStatusError),
            wait=wait_retry_after(
                fallback_strategy=wait_exponential(multiplier=1, max=60),
                max_wait=300  # Don't wait more than 5 minutes
            ),
            stop=stop_after_attempt(10),
            reraise=True
        ),
        validate_response=lambda r: r.raise_for_status()  # Raises HTTPStatusError for 4xx/5xx
    )
    return AsyncClient(transport=transport)

# Example usage
client = create_rate_limit_client()
# Client is now ready to use with any HTTP requests and will respect Retry-After headers

```

The `wait_retry_after` function automatically detects `Retry-After` headers in 429 (rate limit) responses and waits for the specified time. If no header is present, it falls back to exponential backoff.
### Network Error Handling
network_error_handling.py```
import httpx
from tenacity import retry_if_exception_type, stop_after_attempt, wait_exponential

from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig


def create_network_resilient_client():
    """Create a client that handles network errors with retries."""
    transport = AsyncTenacityTransport(
        config=RetryConfig(
            retry=retry_if_exception_type((
                httpx.TimeoutException,
                httpx.ConnectError,
                httpx.ReadError
            )),
            wait=wait_exponential(multiplier=1, max=10),
            stop=stop_after_attempt(3),
            reraise=True
        )
    )
    return httpx.AsyncClient(transport=transport)

# Example usage
client = create_network_resilient_client()
# Client will now retry on timeout, connection, and read errors

```

### Custom Retry Logic
custom_retry_logic.py```
import httpx
from tenacity import retry_if_exception, stop_after_attempt, wait_exponential

from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after


def create_custom_retry_client():
    """Create a client with custom retry logic."""
    def custom_retry_condition(exception):
        """Custom logic to determine if we should retry."""
        if isinstance(exception, httpx.HTTPStatusError):
            # Retry on server errors but not client errors
            return 500 <= exception.response.status_code < 600
        return isinstance(exception, httpx.TimeoutException | httpx.ConnectError)

    transport = AsyncTenacityTransport(
        config=RetryConfig(
            retry=retry_if_exception(custom_retry_condition),
            # Use wait_retry_after for smart waiting on rate limits,
            # with custom exponential backoff as fallback
            wait=wait_retry_after(
                fallback_strategy=wait_exponential(multiplier=2, max=30),
                max_wait=120
            ),
            stop=stop_after_attempt(5),
            reraise=True
        ),
        validate_response=lambda r: r.raise_for_status()
    )
    return httpx.AsyncClient(transport=transport)

client = create_custom_retry_client()
# Client will retry server errors (5xx) and network errors, but not client errors (4xx)

```

## Using with Different Providers
The retry transports work with any provider that accepts a custom HTTP client:
### OpenAI
openai_with_retries.py```
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from smart_retry_example import create_retrying_client

client = create_retrying_client()
model = OpenAIChatModel('gpt-5.2', provider=OpenAIProvider(http_client=client))
agent = Agent(model)

```

### Anthropic
anthropic_with_retries.py```
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

from smart_retry_example import create_retrying_client

client = create_retrying_client()
model = AnthropicModel('claude-sonnet-4-5-20250929', provider=AnthropicProvider(http_client=client))
agent = Agent(model)

```

### Any OpenAI-Compatible Provider
openai_compatible_with_retries.py```
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from smart_retry_example import create_retrying_client

client = create_retrying_client()
model = OpenAIChatModel(
    'your-model-name',  # Replace with actual model name
    provider=OpenAIProvider(
        base_url='https://api.example.com/v1',  # Replace with actual API URL
        api_key='your-api-key',  # Replace with actual API key
        http_client=client
    )
)
agent = Agent(model)

```

## Best Practices
  1. **Start Conservative** : Begin with a small number of retries (3-5) and reasonable wait times.
  2. **Use Exponential Backoff** : This helps avoid overwhelming servers during outages.
  3. **Set Maximum Wait Times** : Prevent indefinite delays with reasonable maximum wait times.
  4. **Handle Rate Limits Properly** : Respect `Retry-After` headers when possible.
  5. **Log Retry Attempts** : Add logging to monitor retry behavior in production. (This will be picked up by Logfire automatically if you instrument httpx.)
  6. **Consider Circuit Breakers** : For high-traffic applications, consider implementing circuit breaker patterns.


Monitoring Retries in Production
Excessive retries can indicate underlying issues and increase costs. [Logfire](https://ai.pydantic.dev/logfire/) helps you track retry patterns:
  * See which requests triggered retries
  * Understand retry causes (rate limits, server errors, timeouts)
  * Monitor retry frequency over time
  * Identify opportunities to reduce retries


With [HTTPX instrumentation](https://ai.pydantic.dev/logfire/#monitoring-http-requests) enabled, retry attempts are automatically captured in your traces.
## Error Handling
The retry transports will re-raise the last exception if all retry attempts fail. Make sure to handle these appropriately in your application:
error_handling_example.py```
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from smart_retry_example import create_retrying_client

client = create_retrying_client()
model = OpenAIChatModel('gpt-5.2', provider=OpenAIProvider(http_client=client))
agent = Agent(model)

```

## Performance Considerations
  * Retries add latency to requests, especially with exponential backoff
  * Consider the total timeout for your application when configuring retry behavior
  * Monitor retry rates to detect systemic issues
  * Use async transports for better concurrency when handling multiple requests


For more advanced retry configurations, refer to the [tenacity documentation](https://tenacity.readthedocs.io/).
## Provider-Specific Retry Behavior
### AWS Bedrock
The AWS Bedrock provider uses boto3's built-in retry mechanisms instead of httpx. To configure retries for Bedrock, use boto3's `Config`:
```
from botocore.config import Config

config = Config(retries={'max_attempts': 5, 'mode': 'adaptive'})

```

See [Bedrock: Configuring Retries](https://ai.pydantic.dev/models/bedrock/#configuring-retries) for complete examples.
© Pydantic Services Inc. 2024 to present
