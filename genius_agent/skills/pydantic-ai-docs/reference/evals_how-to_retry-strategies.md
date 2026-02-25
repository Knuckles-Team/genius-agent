[ Skip to content ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#retry-strategies)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
Retry Strategies
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
      * Retry Strategies  [ Retry Strategies  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/)
        * [ Overview  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#overview)
        * [ Basic Retry Configuration  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#basic-retry-configuration)
        * [ Retry Configuration Options  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#retry-configuration-options)
          * [ Common Parameters  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#common-parameters)
        * [ Task Retries  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#task-retries)
          * [ When Task Retries Trigger  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#when-task-retries-trigger)
          * [ Exponential Backoff  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#exponential-backoff)
        * [ Evaluator Retries  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#evaluator-retries)
          * [ When Evaluator Retries Trigger  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#when-evaluator-retries-trigger)
          * [ Evaluator Failures  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#evaluator-failures)
        * [ Combining Task and Evaluator Retries  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#combining-task-and-evaluator-retries)
        * [ Practical Examples  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#practical-examples)
          * [ Rate Limit Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#rate-limit-handling)
          * [ Network Timeout Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#network-timeout-handling)
          * [ Context Length Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#context-length-handling)
        * [ Retry vs Error Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#retry-vs-error-handling)
        * [ Troubleshooting  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#troubleshooting)
          * [ "Still failing after retries"  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#still-failing-after-retries)
          * [ "Evaluations taking too long"  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#evaluations-taking-too-long)
          * [ "Hitting rate limits despite retries"  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#hitting-rate-limits-despite-retries)
        * [ Next Steps  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#next-steps)
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


  * [ Overview  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#overview)
  * [ Basic Retry Configuration  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#basic-retry-configuration)
  * [ Retry Configuration Options  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#retry-configuration-options)
    * [ Common Parameters  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#common-parameters)
  * [ Task Retries  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#task-retries)
    * [ When Task Retries Trigger  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#when-task-retries-trigger)
    * [ Exponential Backoff  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#exponential-backoff)
  * [ Evaluator Retries  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#evaluator-retries)
    * [ When Evaluator Retries Trigger  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#when-evaluator-retries-trigger)
    * [ Evaluator Failures  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#evaluator-failures)
  * [ Combining Task and Evaluator Retries  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#combining-task-and-evaluator-retries)
  * [ Practical Examples  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#practical-examples)
    * [ Rate Limit Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#rate-limit-handling)
    * [ Network Timeout Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#network-timeout-handling)
    * [ Context Length Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#context-length-handling)
  * [ Retry vs Error Handling  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#retry-vs-error-handling)
  * [ Troubleshooting  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#troubleshooting)
    * [ "Still failing after retries"  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#still-failing-after-retries)
    * [ "Evaluations taking too long"  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#evaluations-taking-too-long)
    * [ "Hitting rate limits despite retries"  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#hitting-rate-limits-despite-retries)
  * [ Next Steps  ](https://ai.pydantic.dev/evals/how-to/retry-strategies/#next-steps)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ Pydantic Evals  ](https://ai.pydantic.dev/evals/)
  3. [ How-To Guides  ](https://ai.pydantic.dev/evals/how-to/logfire-integration/)


# Retry Strategies
Handle transient failures in tasks and evaluators with automatic retry logic.
## Overview
LLM-based systems can experience transient failures:
  * Rate limits
  * Network timeouts
  * Temporary API outages
  * Context length errors


Pydantic Evals supports retry configuration for both:
  * **Task execution** - The function being evaluated
  * **Evaluator execution** - The evaluators themselves


## Basic Retry Configuration
Pass a retry configuration to `evaluate()` or `evaluate_sync()` using [Tenacity](https://tenacity.readthedocs.io/) parameters:
```
from tenacity import stop_after_attempt

from pydantic_evals import Case, Dataset


def my_function(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

report = dataset.evaluate_sync(
    task=my_function,
    retry_task={'stop': stop_after_attempt(3)},
    retry_evaluators={'stop': stop_after_attempt(2)},
)

```

## Retry Configuration Options
Retry configurations use [Tenacity](https://tenacity.readthedocs.io/) and support the same options as Pydantic AI's [`RetryConfig`](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig"):
```
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset


def my_function(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

retry_config = {
    'stop': stop_after_attempt(3),  # Stop after 3 attempts
    'wait': wait_exponential(multiplier=1, min=1, max=10),  # Exponential backoff: 1s, 2s, 4s, 8s (capped at 10s)
    'reraise': True,  # Re-raise the original exception after exhausting retries
}

dataset.evaluate_sync(
    task=my_function,
    retry_task=retry_config,
)

```

### Common Parameters
The retry configuration accepts any parameters from the tenacity `retry` decorator. Common ones include:
Parameter | Type | Description
---|---|---
`stop` | `StopBaseT` | Stop strategy (e.g., `stop_after_attempt(3)`, `stop_after_delay(60)`)
`wait` | `WaitBaseT` | Wait strategy (e.g., `wait_exponential()`, `wait_fixed(2)`)
`retry` | `RetryBaseT` | Retry condition (e.g., `retry_if_exception_type(TimeoutError)`)
`reraise` | `bool` | Whether to reraise the original exception (default: `False`)
`before_sleep` | `Callable` | Callback before sleeping between retries
See the [Tenacity documentation](https://tenacity.readthedocs.io/) for all available options.
## Task Retries
Retry the task function when it fails:
```
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset


async def call_llm(inputs: str) -> str:
    return f'LLM response to: {inputs}'


async def flaky_llm_task(inputs: str) -> str:
    """This might hit rate limits or timeout."""
    response = await call_llm(inputs)
    return response


dataset = Dataset(cases=[Case(inputs='test')])

report = dataset.evaluate_sync(
    task=flaky_llm_task,
    retry_task={
        'stop': stop_after_attempt(5),  # Try up to 5 times
        'wait': wait_exponential(multiplier=1, min=1, max=30),  # Exponential backoff, capped at 30s
        'reraise': True,
    },
)

```

### When Task Retries Trigger
Retries trigger when the task raises an exception:
```
class RateLimitError(Exception):
    pass


class ValidationError(Exception):
    pass


async def call_api(inputs: str) -> str:
    return f'API response: {inputs}'


async def my_task(inputs: str) -> str:
    try:
        return await call_api(inputs)
    except RateLimitError:
        # Will trigger retry
        raise
    except ValidationError:
        # Will also trigger retry
        raise

```

### Exponential Backoff
When using `wait_exponential()`, delays increase exponentially:
```
Attempt 1: immediate
Attempt 2: ~1s delay (multiplier * 2^0)
Attempt 3: ~2s delay (multiplier * 2^1)
Attempt 4: ~4s delay (multiplier * 2^2)
Attempt 5: ~8s delay (multiplier * 2^3, capped at max)

```

The actual delay depends on the `multiplier`, `min`, and `max` parameters passed to `wait_exponential()`.
## Evaluator Retries
Retry evaluators when they fail:
```
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge


def my_task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # LLMJudge might hit rate limits
        LLMJudge(rubric='Response is accurate'),
    ],
)

report = dataset.evaluate_sync(
    task=my_task,
    retry_evaluators={
        'stop': stop_after_attempt(3),
        'wait': wait_exponential(multiplier=1, min=0.5, max=10),
        'reraise': True,
    },
)

```

### When Evaluator Retries Trigger
Retries trigger when an evaluator raises an exception:
```
from dataclasses import dataclass

from pydantic_evals.evaluators import Evaluator, EvaluatorContext


async def external_api_call(output: str) -> bool:
    return len(output) > 0


@dataclass
class APIEvaluator(Evaluator):
    async def evaluate(self, ctx: EvaluatorContext) -> bool:
        # If this raises an exception, retry logic will trigger
        result = await external_api_call(ctx.output)
        return result

```

### Evaluator Failures
If an evaluator fails after all retries, it's recorded as an [`EvaluatorFailure`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorFailure "EvaluatorFailure



      dataclass
  "):
```
from tenacity import stop_after_attempt

from pydantic_evals import Case, Dataset


def task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

report = dataset.evaluate_sync(task, retry_evaluators={'stop': stop_after_attempt(3)})

# Check for evaluator failures
for case in report.cases:
    if case.evaluator_failures:
        for failure in case.evaluator_failures:
            print(f'Evaluator {failure.name} failed: {failure.error_message}')
    #> (No output - no evaluator failures in this case)

```

View evaluator failures in reports:
```
from pydantic_evals import Case, Dataset


def task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])
report = dataset.evaluate_sync(task)

report.print(include_evaluator_failures=True)
"""
  Evaluation Summary:
         task
┏━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID  ┃ Duration ┃
┡━━━━━━━━━━╇━━━━━━━━━━┩
│ Case 1   │     10ms │
├──────────┼──────────┤
│ Averages │     10ms │
└──────────┴──────────┘
"""
#>
#> ✅ case_0                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% (0/0)

```

## Combining Task and Evaluator Retries
You can configure both independently:
```
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset


def flaky_task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

report = dataset.evaluate_sync(
    task=flaky_task,
    retry_task={
        'stop': stop_after_attempt(5),  # Retry task up to 5 times
        'wait': wait_exponential(multiplier=1, min=1, max=30),
        'reraise': True,
    },
    retry_evaluators={
        'stop': stop_after_attempt(3),  # Retry evaluators up to 3 times
        'wait': wait_exponential(multiplier=1, min=0.5, max=10),
        'reraise': True,
    },
)

```

## Practical Examples
### Rate Limit Handling
```
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge


async def expensive_llm_call(inputs: str) -> str:
    return f'LLM response: {inputs}'


async def llm_task(inputs: str) -> str:
    """Task that might hit rate limits."""
    return await expensive_llm_call(inputs)


dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        LLMJudge(rubric='Quality check'),  # Also might hit rate limits
    ],
)

# Generous retries for rate limits
report = dataset.evaluate_sync(
    task=llm_task,
    retry_task={
        'stop': stop_after_attempt(10),  # Rate limits can take multiple retries
        'wait': wait_exponential(multiplier=2, min=2, max=60),  # Start at 2s, exponential up to 60s
        'reraise': True,
    },
    retry_evaluators={
        'stop': stop_after_attempt(5),
        'wait': wait_exponential(multiplier=2, min=2, max=30),
        'reraise': True,
    },
)

```

### Network Timeout Handling
```
import httpx
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset


async def api_task(inputs: str) -> str:
    """Task that calls external API which might timeout."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post('https://api.example.com', json={'input': inputs})
        return response.text


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Quick retries for network issues
report = dataset.evaluate_sync(
    task=api_task,
    retry_task={
        'stop': stop_after_attempt(4),  # A few quick retries
        'wait': wait_exponential(multiplier=0.5, min=0.5, max=5),  # Fast retry, capped at 5s
        'reraise': True,
    },
)

```

### Context Length Handling
```
from tenacity import stop_after_attempt

from pydantic_evals import Case, Dataset


class ContextLengthError(Exception):
    pass


async def llm_call(inputs: str, max_tokens: int = 8000) -> str:
    return f'LLM response: {inputs[:100]}'


async def smart_llm_task(inputs: str) -> str:
    """Task that might exceed context length."""
    try:
        return await llm_call(inputs, max_tokens=8000)
    except ContextLengthError:
        # Retry with shorter context
        truncated_inputs = inputs[:4000]
        return await llm_call(truncated_inputs, max_tokens=4000)


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Don't retry context length errors (handle in task)
report = dataset.evaluate_sync(
    task=smart_llm_task,
    retry_task={'stop': stop_after_attempt(1)},  # No retries, we handle it
)

```

## Retry vs Error Handling
**Use retries for:** - Transient failures (rate limits, timeouts) - Network issues - Temporary service outages - Recoverable errors
**Use error handling for:** - Validation errors - Logic errors - Permanent failures - Expected error conditions
```
class RateLimitError(Exception):
    pass


async def llm_call(inputs: str) -> str:
    return f'LLM response: {inputs}'


def is_valid(result: str) -> bool:
    return len(result) > 0


async def smart_task(inputs: str) -> str:
    """Handle expected errors, let retries handle transient failures."""
    try:
        result = await llm_call(inputs)

        # Validate output (don't retry validation errors)
        if not is_valid(result):
            return 'ERROR: Invalid output format'

        return result

    except RateLimitError:
        # Let retry logic handle this
        raise

    except ValueError as e:
        # Don't retry - this is a permanent error
        return f'ERROR: {e}'

```

## Troubleshooting
### "Still failing after retries"
Increase retry attempts or check if error is retriable:
```
import logging

from tenacity import stop_after_attempt

from pydantic_evals import Case, Dataset


def task(inputs: str) -> str:
    return f'Result: {inputs}'


# Add logging to see what's failing
logging.basicConfig(level=logging.DEBUG)

dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Tenacity logs retry attempts
report = dataset.evaluate_sync(task, retry_task={'stop': stop_after_attempt(5)})

```

### "Evaluations taking too long"
Reduce retry attempts or wait times:
```
from tenacity import stop_after_attempt, wait_exponential

# Faster retries
retry_config = {
    'stop': stop_after_attempt(3),  # Fewer attempts
    'wait': wait_exponential(multiplier=0.1, min=0.1, max=2),  # Quick retries, capped at 2s
    'reraise': True,
}

```

### "Hitting rate limits despite retries"
Increase delays or use `max_concurrency`:
```
from tenacity import stop_after_attempt, wait_exponential

from pydantic_evals import Case, Dataset


def task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Longer delays
retry_config = {
    'stop': stop_after_attempt(5),
    'wait': wait_exponential(multiplier=5, min=5, max=60),  # Start at 5s, exponential up to 60s
    'reraise': True,
}

# Also reduce concurrency
report = dataset.evaluate_sync(
    task=task,
    retry_task=retry_config,
    max_concurrency=2,  # Only 2 concurrent tasks
)

```

## Next Steps
  * **[Concurrency& Performance](https://ai.pydantic.dev/evals/how-to/concurrency/)** - Optimize evaluation performance
  * **[Logfire Integration](https://ai.pydantic.dev/evals/how-to/logfire-integration/)** - View retries in Logfire


© Pydantic Services Inc. 2024 to present
