[ Skip to content ](https://ai.pydantic.dev/api/retries/#pydantic_airetries)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_ai.retries
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
      * [ HTTP Request Retries  ](https://ai.pydantic.dev/retries/)
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
      * pydantic_ai.retries  [ pydantic_ai.retries  ](https://ai.pydantic.dev/api/retries/)
        * [ retries  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries)
        * [ RetryConfig  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig)
          * [ sleep  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.sleep)
          * [ stop  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.stop)
          * [ wait  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.wait)
          * [ retry  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.retry)
          * [ before  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.before)
          * [ after  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.after)
          * [ before_sleep  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.before_sleep)
          * [ reraise  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.reraise)
          * [ retry_error_cls  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.retry_error_cls)
          * [ retry_error_callback  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.retry_error_callback)
        * [ TenacityTransport  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.TenacityTransport)
          * [ handle_request  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.TenacityTransport.handle_request)
        * [ AsyncTenacityTransport  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.AsyncTenacityTransport)
          * [ handle_async_request  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.AsyncTenacityTransport.handle_async_request)
        * [ wait_retry_after  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.wait_retry_after)
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


  * [ retries  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries)
  * [ RetryConfig  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig)
    * [ sleep  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.sleep)
    * [ stop  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.stop)
    * [ wait  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.wait)
    * [ retry  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.retry)
    * [ before  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.before)
    * [ after  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.after)
    * [ before_sleep  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.before_sleep)
    * [ reraise  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.reraise)
    * [ retry_error_cls  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.retry_error_cls)
    * [ retry_error_callback  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig.retry_error_callback)
  * [ TenacityTransport  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.TenacityTransport)
    * [ handle_request  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.TenacityTransport.handle_request)
  * [ AsyncTenacityTransport  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.AsyncTenacityTransport)
    * [ handle_async_request  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.AsyncTenacityTransport.handle_async_request)
  * [ wait_retry_after  ](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.wait_retry_after)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_ai  ](https://ai.pydantic.dev/api/ag_ui/)


# `pydantic_ai.retries`
Retries utilities based on tenacity, especially for HTTP requests.
This module provides HTTP transport wrappers and wait strategies that integrate with the tenacity library to add retry capabilities to HTTP requests. The transports can be used with HTTP clients that support custom transports (such as httpx), while the wait strategies can be used with any tenacity retry decorator.
The module includes: - TenacityTransport: Synchronous HTTP transport with retry capabilities - AsyncTenacityTransport: Asynchronous HTTP transport with retry capabilities - wait_retry_after: Wait strategy that respects HTTP Retry-After headers
###  RetryConfig
Bases: `TypedDict[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "typing_extensions.TypedDict")`
The configuration for tenacity-based retrying.
These are precisely the arguments to the tenacity `retry` decorator, and they are generally used internally by passing them to that decorator via `@retry(**config)` or similar.
All fields are optional, and if not provided, the default values from the `tenacity.retry` decorator will be used.
Source code in `pydantic_ai_slim/pydantic_ai/retries.py`
```
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
```
| ```
class RetryConfig(TypedDict, total=False):
    """The configuration for tenacity-based retrying.

    These are precisely the arguments to the tenacity `retry` decorator, and they are generally
    used internally by passing them to that decorator via `@retry(**config)` or similar.

    All fields are optional, and if not provided, the default values from the `tenacity.retry` decorator will be used.
    """

    sleep: Callable[[int | float], None | Awaitable[None]]
    """A sleep strategy to use for sleeping between retries.

    Tenacity's default for this argument is `tenacity.nap.sleep`."""

    stop: StopBaseT
    """
    A stop strategy to determine when to stop retrying.

    Tenacity's default for this argument is `tenacity.stop.stop_never`."""

    wait: WaitBaseT
    """
    A wait strategy to determine how long to wait between retries.

    Tenacity's default for this argument is `tenacity.wait.wait_none`."""

    retry: SyncRetryBaseT | RetryBaseT
    """A retry strategy to determine which exceptions should trigger a retry.

    Tenacity's default for this argument is `tenacity.retry.retry_if_exception_type()`."""

    before: Callable[[RetryCallState], None | Awaitable[None]]
    """
    A callable that is called before each retry attempt.

    Tenacity's default for this argument is `tenacity.before.before_nothing`."""

    after: Callable[[RetryCallState], None | Awaitable[None]]
    """
    A callable that is called after each retry attempt.

    Tenacity's default for this argument is `tenacity.after.after_nothing`."""

    before_sleep: Callable[[RetryCallState], None | Awaitable[None]] | None
    """
    An optional callable that is called before sleeping between retries.

    Tenacity's default for this argument is `None`."""

    reraise: bool
    """Whether to reraise the last exception if the retry attempts are exhausted, or raise a RetryError instead.

    Tenacity's default for this argument is `False`."""

    retry_error_cls: type[RetryError]
    """The exception class to raise when the retry attempts are exhausted and `reraise` is False.

    Tenacity's default for this argument is `tenacity.RetryError`."""

    retry_error_callback: Callable[[RetryCallState], Any | Awaitable[Any]] | None
    """An optional callable that is called when the retry attempts are exhausted and `reraise` is False.

    Tenacity's default for this argument is `None`."""

```

---|---
####  sleep `instance-attribute`
```
sleep: Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[int[](https://docs.python.org/3/library/functions.html#int) | float[](https://docs.python.org/3/library/functions.html#float)], None | Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[None]]

```

A sleep strategy to use for sleeping between retries.
Tenacity's default for this argument is `tenacity.nap.sleep`.
####  stop `instance-attribute`
```
stop: StopBaseT

```

A stop strategy to determine when to stop retrying.
Tenacity's default for this argument is `tenacity.stop.stop_never`.
####  wait `instance-attribute`
```
wait: WaitBaseT

```

A wait strategy to determine how long to wait between retries.
Tenacity's default for this argument is `tenacity.wait.wait_none`.
####  retry `instance-attribute`
```
retry: RetryBaseT | RetryBaseT

```

A retry strategy to determine which exceptions should trigger a retry.
Tenacity's default for this argument is `tenacity.retry.retry_if_exception_type()`.
####  before `instance-attribute`
```
before: Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], None | Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[None]]

```

A callable that is called before each retry attempt.
Tenacity's default for this argument is `tenacity.before.before_nothing`.
####  after `instance-attribute`
```
after: Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], None | Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[None]]

```

A callable that is called after each retry attempt.
Tenacity's default for this argument is `tenacity.after.after_nothing`.
####  before_sleep `instance-attribute`
```
before_sleep: (
    Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], None | Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[None]]
    | None
)

```

An optional callable that is called before sleeping between retries.
Tenacity's default for this argument is `None`.
####  reraise `instance-attribute`
```
reraise: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Whether to reraise the last exception if the retry attempts are exhausted, or raise a RetryError instead.
Tenacity's default for this argument is `False`.
####  retry_error_cls `instance-attribute`
```
retry_error_cls: type[](https://docs.python.org/3/library/functions.html#type)[RetryError]

```

The exception class to raise when the retry attempts are exhausted and `reraise` is False.
Tenacity's default for this argument is `tenacity.RetryError`.
####  retry_error_callback `instance-attribute`
```
retry_error_callback: (
    Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") | Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]] | None
)

```

An optional callable that is called when the retry attempts are exhausted and `reraise` is False.
Tenacity's default for this argument is `None`.
###  TenacityTransport
Bases: `BaseTransport`
Synchronous HTTP transport with tenacity-based retry functionality.
This transport wraps another BaseTransport and adds retry capabilities using the tenacity library. It can be configured to retry requests based on various conditions such as specific exception types, response status codes, or custom validation logic.
The transport works by intercepting HTTP requests and responses, allowing the tenacity controller to determine when and how to retry failed requests. The validate_response function can be used to convert HTTP responses into exceptions that trigger retries.
Parameters:
Name | Type | Description | Default
---|---|---|---
`wrapped` |  `BaseTransport | None` |  The underlying transport to wrap and add retry functionality to. |  `None`
`config` |  `RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)")` |  The arguments to use for the tenacity `retry` decorator, including retry conditions, wait strategy, stop conditions, etc. See the tenacity docs for more info. |  _required_
`validate_response` |  `Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[Response], Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None` |  Optional callable that takes a Response and can raise an exception to be handled by the controller if the response should trigger a retry. Common use case is to raise exceptions for certain HTTP status codes. If None, no response validation is performed. |  `None`
Example
```
from httpx import Client, HTTPStatusError, HTTPTransport
from tenacity import retry_if_exception_type, stop_after_attempt

from pydantic_ai.retries import RetryConfig, TenacityTransport, wait_retry_after

transport = TenacityTransport(
    RetryConfig(
        retry=retry_if_exception_type(HTTPStatusError),
        wait=wait_retry_after(max_wait=300),
        stop=stop_after_attempt(5),
        reraise=True
    ),
    HTTPTransport(),
    validate_response=lambda r: r.raise_for_status()
)
client = Client(transport=transport)

```

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`
```
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
```
| ```
class TenacityTransport(BaseTransport):
    """Synchronous HTTP transport with tenacity-based retry functionality.

    This transport wraps another BaseTransport and adds retry capabilities using the tenacity library.
    It can be configured to retry requests based on various conditions such as specific exception types,
    response status codes, or custom validation logic.

    The transport works by intercepting HTTP requests and responses, allowing the tenacity controller
    to determine when and how to retry failed requests. The validate_response function can be used
    to convert HTTP responses into exceptions that trigger retries.

    Args:
        wrapped: The underlying transport to wrap and add retry functionality to.
        config: The arguments to use for the tenacity `retry` decorator, including retry conditions,
            wait strategy, stop conditions, etc. See the tenacity docs for more info.
        validate_response: Optional callable that takes a Response and can raise an exception
            to be handled by the controller if the response should trigger a retry.
            Common use case is to raise exceptions for certain HTTP status codes.
            If None, no response validation is performed.

    Example:
    ```python
        from httpx import Client, HTTPStatusError, HTTPTransport
        from tenacity import retry_if_exception_type, stop_after_attempt

        from pydantic_ai.retries import RetryConfig, TenacityTransport, wait_retry_after

        transport = TenacityTransport(
            RetryConfig(
                retry=retry_if_exception_type(HTTPStatusError),
                wait=wait_retry_after(max_wait=300),
                stop=stop_after_attempt(5),
                reraise=True
            ),
            HTTPTransport(),
            validate_response=lambda r: r.raise_for_status()
        )
        client = Client(transport=transport)
    ```
    """

    def __init__(
        self,
        config: RetryConfig,
        wrapped: BaseTransport | None = None,
        validate_response: Callable[[Response], Any] | None = None,
    ):
        self.config = config
        self.wrapped = wrapped or HTTPTransport()
        self.validate_response = validate_response

    def handle_request(self, request: Request) -> Response:
        """Handle an HTTP request with retry logic.

        Args:
            request: The HTTP request to handle.

        Returns:
            The HTTP response.

        Raises:
            RuntimeError: If the retry controller did not make any attempts.
            Exception: Any exception raised by the wrapped transport or validation function.
        """

        @retry(**self.config)
        def handle_request(req: Request) -> Response:
            response = self.wrapped.handle_request(req)

            # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
            response.request = req

            if self.validate_response:
                try:
                    self.validate_response(response)
                except Exception:
                    response.close()
                    raise
            return response

        return handle_request(request)

    def __enter__(self) -> TenacityTransport:
        self.wrapped.__enter__()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None:
        self.wrapped.__exit__(exc_type, exc_value, traceback)

    def close(self) -> None:
        self.wrapped.close()  # pragma: no cover

```

---|---
####  handle_request
```
handle_request(request: Request) -> Response

```

Handle an HTTP request with retry logic.
Parameters:
Name | Type | Description | Default
---|---|---|---
`request` |  `Request` |  The HTTP request to handle. |  _required_
Returns:
Type | Description
---|---
`Response` |  The HTTP response.
Raises:
Type | Description
---|---
`RuntimeError[](https://docs.python.org/3/library/exceptions.html#RuntimeError)` |  If the retry controller did not make any attempts.
`Exception[](https://docs.python.org/3/library/exceptions.html#Exception)` |  Any exception raised by the wrapped transport or validation function.
Source code in `pydantic_ai_slim/pydantic_ai/retries.py`
```
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
```
| ```
def handle_request(self, request: Request) -> Response:
    """Handle an HTTP request with retry logic.

    Args:
        request: The HTTP request to handle.

    Returns:
        The HTTP response.

    Raises:
        RuntimeError: If the retry controller did not make any attempts.
        Exception: Any exception raised by the wrapped transport or validation function.
    """

    @retry(**self.config)
    def handle_request(req: Request) -> Response:
        response = self.wrapped.handle_request(req)

        # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
        response.request = req

        if self.validate_response:
            try:
                self.validate_response(response)
            except Exception:
                response.close()
                raise
        return response

    return handle_request(request)

```

---|---
###  AsyncTenacityTransport
Bases: `AsyncBaseTransport`
Asynchronous HTTP transport with tenacity-based retry functionality.
This transport wraps another AsyncBaseTransport and adds retry capabilities using the tenacity library. It can be configured to retry requests based on various conditions such as specific exception types, response status codes, or custom validation logic.
The transport works by intercepting HTTP requests and responses, allowing the tenacity controller to determine when and how to retry failed requests. The validate_response function can be used to convert HTTP responses into exceptions that trigger retries.
Parameters:
Name | Type | Description | Default
---|---|---|---
`wrapped` |  `AsyncBaseTransport | None` |  The underlying async transport to wrap and add retry functionality to. |  `None`
`config` |  `RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)")` |  The arguments to use for the tenacity `retry` decorator, including retry conditions, wait strategy, stop conditions, etc. See the tenacity docs for more info. |  _required_
`validate_response` |  `Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[Response], Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None` |  Optional callable that takes a Response and can raise an exception to be handled by the controller if the response should trigger a retry. Common use case is to raise exceptions for certain HTTP status codes. If None, no response validation is performed. |  `None`
Example
```
from httpx import AsyncClient, HTTPStatusError
from tenacity import retry_if_exception_type, stop_after_attempt

from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after

transport = AsyncTenacityTransport(
    RetryConfig(
        retry=retry_if_exception_type(HTTPStatusError),
        wait=wait_retry_after(max_wait=300),
        stop=stop_after_attempt(5),
        reraise=True
    ),
    validate_response=lambda r: r.raise_for_status()
)
client = AsyncClient(transport=transport)

```

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`
```
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
```
| ```
class AsyncTenacityTransport(AsyncBaseTransport):
    """Asynchronous HTTP transport with tenacity-based retry functionality.

    This transport wraps another AsyncBaseTransport and adds retry capabilities using the tenacity library.
    It can be configured to retry requests based on various conditions such as specific exception types,
    response status codes, or custom validation logic.

    The transport works by intercepting HTTP requests and responses, allowing the tenacity controller
    to determine when and how to retry failed requests. The validate_response function can be used
    to convert HTTP responses into exceptions that trigger retries.

    Args:
        wrapped: The underlying async transport to wrap and add retry functionality to.
        config: The arguments to use for the tenacity `retry` decorator, including retry conditions,
            wait strategy, stop conditions, etc. See the tenacity docs for more info.
        validate_response: Optional callable that takes a Response and can raise an exception
            to be handled by the controller if the response should trigger a retry.
            Common use case is to raise exceptions for certain HTTP status codes.
            If None, no response validation is performed.

    Example:
    ```python
        from httpx import AsyncClient, HTTPStatusError
        from tenacity import retry_if_exception_type, stop_after_attempt

        from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after

        transport = AsyncTenacityTransport(
            RetryConfig(
                retry=retry_if_exception_type(HTTPStatusError),
                wait=wait_retry_after(max_wait=300),
                stop=stop_after_attempt(5),
                reraise=True
            ),
            validate_response=lambda r: r.raise_for_status()
        )
        client = AsyncClient(transport=transport)
    ```
    """

    def __init__(
        self,
        config: RetryConfig,
        wrapped: AsyncBaseTransport | None = None,
        validate_response: Callable[[Response], Any] | None = None,
    ):
        self.config = config
        self.wrapped = wrapped or AsyncHTTPTransport()
        self.validate_response = validate_response

    async def handle_async_request(self, request: Request) -> Response:
        """Handle an async HTTP request with retry logic.

        Args:
            request: The HTTP request to handle.

        Returns:
            The HTTP response.

        Raises:
            RuntimeError: If the retry controller did not make any attempts.
            Exception: Any exception raised by the wrapped transport or validation function.
        """

        @retry(**self.config)
        async def handle_async_request(req: Request) -> Response:
            response = await self.wrapped.handle_async_request(req)

            # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
            response.request = req

            if self.validate_response:
                try:
                    self.validate_response(response)
                except Exception:
                    await response.aclose()
                    raise
            return response

        return await handle_async_request(request)

    async def __aenter__(self) -> AsyncTenacityTransport:
        await self.wrapped.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None:
        await self.wrapped.__aexit__(exc_type, exc_value, traceback)

    async def aclose(self) -> None:
        await self.wrapped.aclose()

```

---|---
####  handle_async_request `async`
```
handle_async_request(request: Request) -> Response

```

Handle an async HTTP request with retry logic.
Parameters:
Name | Type | Description | Default
---|---|---|---
`request` |  `Request` |  The HTTP request to handle. |  _required_
Returns:
Type | Description
---|---
`Response` |  The HTTP response.
Raises:
Type | Description
---|---
`RuntimeError[](https://docs.python.org/3/library/exceptions.html#RuntimeError)` |  If the retry controller did not make any attempts.
`Exception[](https://docs.python.org/3/library/exceptions.html#Exception)` |  Any exception raised by the wrapped transport or validation function.
Source code in `pydantic_ai_slim/pydantic_ai/retries.py`
```
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
```
| ```
async def handle_async_request(self, request: Request) -> Response:
    """Handle an async HTTP request with retry logic.

    Args:
        request: The HTTP request to handle.

    Returns:
        The HTTP response.

    Raises:
        RuntimeError: If the retry controller did not make any attempts.
        Exception: Any exception raised by the wrapped transport or validation function.
    """

    @retry(**self.config)
    async def handle_async_request(req: Request) -> Response:
        response = await self.wrapped.handle_async_request(req)

        # this is normally set by httpx _after_ calling this function, but we want the request in the validator:
        response.request = req

        if self.validate_response:
            try:
                self.validate_response(response)
            except Exception:
                await response.aclose()
                raise
        return response

    return await handle_async_request(request)

```

---|---
###  wait_retry_after
```
wait_retry_after(
    fallback_strategy: (
        Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], float[](https://docs.python.org/3/library/functions.html#float)] | None
    ) = None,
    max_wait: float[](https://docs.python.org/3/library/functions.html#float) = 300,
) -> Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], float[](https://docs.python.org/3/library/functions.html#float)]

```

Create a tenacity-compatible wait strategy that respects HTTP Retry-After headers.
This wait strategy checks if the exception contains an HTTPStatusError with a Retry-After header, and if so, waits for the time specified in the header. If no header is present or parsing fails, it falls back to the provided strategy.
The Retry-After header can be in two formats: - An integer representing seconds to wait - An HTTP date string representing when to retry
Parameters:
Name | Type | Description | Default
---|---|---|---
`fallback_strategy` |  `Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], float[](https://docs.python.org/3/library/functions.html#float)] | None` |  Wait strategy to use when no Retry-After header is present or parsing fails. Defaults to exponential backoff with max 60s. |  `None`
`max_wait` |  `float[](https://docs.python.org/3/library/functions.html#float)` |  Maximum time to wait in seconds, regardless of header value. Defaults to 300 (5 minutes). |  `300`
Returns:
Type | Description
---|---
`Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[RetryCallState], float[](https://docs.python.org/3/library/functions.html#float)]` |  A wait function that can be used with tenacity retry decorators.
Example
```
from httpx import AsyncClient, HTTPStatusError
from tenacity import retry_if_exception_type, stop_after_attempt

from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after

transport = AsyncTenacityTransport(
    RetryConfig(
        retry=retry_if_exception_type(HTTPStatusError),
        wait=wait_retry_after(max_wait=120),
        stop=stop_after_attempt(5),
        reraise=True
    ),
    validate_response=lambda r: r.raise_for_status()
)
client = AsyncClient(transport=transport)

```

Source code in `pydantic_ai_slim/pydantic_ai/retries.py`
```
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
```
| ```
def wait_retry_after(
    fallback_strategy: Callable[[RetryCallState], float] | None = None, max_wait: float = 300
) -> Callable[[RetryCallState], float]:
    """Create a tenacity-compatible wait strategy that respects HTTP Retry-After headers.

    This wait strategy checks if the exception contains an HTTPStatusError with a
    Retry-After header, and if so, waits for the time specified in the header.
    If no header is present or parsing fails, it falls back to the provided strategy.

    The Retry-After header can be in two formats:
    - An integer representing seconds to wait
    - An HTTP date string representing when to retry

    Args:
        fallback_strategy: Wait strategy to use when no Retry-After header is present
                          or parsing fails. Defaults to exponential backoff with max 60s.
        max_wait: Maximum time to wait in seconds, regardless of header value.
                 Defaults to 300 (5 minutes).

    Returns:
        A wait function that can be used with tenacity retry decorators.

    Example:
    ```python
        from httpx import AsyncClient, HTTPStatusError
        from tenacity import retry_if_exception_type, stop_after_attempt

        from pydantic_ai.retries import AsyncTenacityTransport, RetryConfig, wait_retry_after

        transport = AsyncTenacityTransport(
            RetryConfig(
                retry=retry_if_exception_type(HTTPStatusError),
                wait=wait_retry_after(max_wait=120),
                stop=stop_after_attempt(5),
                reraise=True
            ),
            validate_response=lambda r: r.raise_for_status()
        )
        client = AsyncClient(transport=transport)
    ```
    """
    if fallback_strategy is None:
        fallback_strategy = wait_exponential(multiplier=1, max=60)

    def wait_func(state: RetryCallState) -> float:
        exc = state.outcome.exception() if state.outcome else None
        if isinstance(exc, HTTPStatusError):
            retry_after = exc.response.headers.get('retry-after')
            if retry_after:
                try:
                    # Try parsing as seconds first
                    wait_seconds = int(retry_after)
                    return min(float(wait_seconds), max_wait)
                except ValueError:
                    # Try parsing as HTTP date
                    try:
                        retry_time = cast(datetime, parsedate_to_datetime(retry_after))
                        assert isinstance(retry_time, datetime)
                        now = datetime.now(timezone.utc)
                        wait_seconds = (retry_time - now).total_seconds()

                        if wait_seconds > 0:
                            return min(wait_seconds, max_wait)
                    except (ValueError, TypeError, AssertionError):
                        # If date parsing fails, fall back to fallback strategy
                        pass

        # Use fallback strategy
        return fallback_strategy(state)

    return wait_func

```

---|---
© Pydantic Services Inc. 2024 to present
