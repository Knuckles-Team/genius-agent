[ Skip to content ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#llm-judge-deep-dive)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
LLM Judge
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
      * LLM Judge  [ LLM Judge  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/)
        * [ When to Use LLM-as-a-Judge  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#when-to-use-llm-as-a-judge)
        * [ Basic Usage  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#basic-usage)
        * [ Configuration Options  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#configuration-options)
          * [ Rubric  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#rubric)
          * [ Including Context  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#including-context)
          * [ Model Selection  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#model-selection)
          * [ Model Settings  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#model-settings)
        * [ Output Modes  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#output-modes)
          * [ Assertion Only (Default)  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#assertion-only-default)
          * [ Score Only  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#score-only)
          * [ Both Score and Assertion  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#both-score-and-assertion)
          * [ Custom Names  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#custom-names)
        * [ Practical Examples  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#practical-examples)
          * [ RAG Evaluation  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#rag-evaluation)
          * [ Recipe Generation with Case-Specific Rubrics  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#recipe-generation-with-case-specific-rubrics)
          * [ Multi-Aspect Evaluation  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#multi-aspect-evaluation)
          * [ Comparative Evaluation  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#comparative-evaluation)
        * [ Best Practices  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#best-practices)
          * [ 1. Be Specific in Rubrics  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#1-be-specific-in-rubrics)
          * [ 2. Use Multiple Judges  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#2-use-multiple-judges)
          * [ 3. Combine with Deterministic Checks  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#3-combine-with-deterministic-checks)
          * [ 4. Use Temperature 0 for Consistency  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#4-use-temperature-0-for-consistency)
        * [ Limitations  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#limitations)
          * [ Non-Determinism  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#non-determinism)
          * [ Cost  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#cost)
          * [ Model Biases  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#model-biases)
          * [ Context Limits  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#context-limits)
        * [ Debugging LLM Judges  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#debugging-llm-judges)
          * [ View Reasons  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#view-reasons)
          * [ Access Programmatically  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#access-programmatically)
          * [ Compare Judges  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#compare-judges)
        * [ Advanced: Custom Judge Models  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#advanced-custom-judge-models)
        * [ Next Steps  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#next-steps)
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


  * [ When to Use LLM-as-a-Judge  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#when-to-use-llm-as-a-judge)
  * [ Basic Usage  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#basic-usage)
  * [ Configuration Options  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#configuration-options)
    * [ Rubric  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#rubric)
    * [ Including Context  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#including-context)
    * [ Model Selection  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#model-selection)
    * [ Model Settings  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#model-settings)
  * [ Output Modes  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#output-modes)
    * [ Assertion Only (Default)  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#assertion-only-default)
    * [ Score Only  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#score-only)
    * [ Both Score and Assertion  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#both-score-and-assertion)
    * [ Custom Names  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#custom-names)
  * [ Practical Examples  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#practical-examples)
    * [ RAG Evaluation  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#rag-evaluation)
    * [ Recipe Generation with Case-Specific Rubrics  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#recipe-generation-with-case-specific-rubrics)
    * [ Multi-Aspect Evaluation  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#multi-aspect-evaluation)
    * [ Comparative Evaluation  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#comparative-evaluation)
  * [ Best Practices  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#best-practices)
    * [ 1. Be Specific in Rubrics  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#1-be-specific-in-rubrics)
    * [ 2. Use Multiple Judges  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#2-use-multiple-judges)
    * [ 3. Combine with Deterministic Checks  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#3-combine-with-deterministic-checks)
    * [ 4. Use Temperature 0 for Consistency  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#4-use-temperature-0-for-consistency)
  * [ Limitations  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#limitations)
    * [ Non-Determinism  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#non-determinism)
    * [ Cost  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#cost)
    * [ Model Biases  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#model-biases)
    * [ Context Limits  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#context-limits)
  * [ Debugging LLM Judges  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#debugging-llm-judges)
    * [ View Reasons  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#view-reasons)
    * [ Access Programmatically  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#access-programmatically)
    * [ Compare Judges  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#compare-judges)
  * [ Advanced: Custom Judge Models  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#advanced-custom-judge-models)
  * [ Next Steps  ](https://ai.pydantic.dev/evals/evaluators/llm-judge/#next-steps)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ Pydantic Evals  ](https://ai.pydantic.dev/evals/)
  3. [ Evaluators  ](https://ai.pydantic.dev/evals/evaluators/overview/)


# LLM Judge Deep Dive
The [`LLMJudge`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.LLMJudge "LLMJudge



      dataclass
  ") evaluator uses an LLM to assess subjective qualities of outputs based on a rubric.
## When to Use LLM-as-a-Judge
LLM judges are ideal for evaluating qualities that require understanding and judgment:
**Good Use Cases:**
  * Factual accuracy
  * Helpfulness and relevance
  * Tone and style compliance
  * Completeness of responses
  * Following complex instructions
  * RAG groundedness (does the answer use provided context?)
  * Citation accuracy


**Poor Use Cases:**
  * Format validation (use [`IsInstance`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.IsInstance "IsInstance



      dataclass
  ") instead)
  * Exact matching (use [`EqualsExpected`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EqualsExpected "EqualsExpected



      dataclass
  "))
  * Performance checks (use [`MaxDuration`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.MaxDuration "MaxDuration



      dataclass
  "))
  * Deterministic logic (write a custom evaluator)


## Basic Usage
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        LLMJudge(rubric='Response is factually accurate'),
    ],
)

```

## Configuration Options
### Rubric
The `rubric` is your evaluation criteria. Be specific and clear:
**Bad rubrics (vague):**
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(rubric='Good response')  # Too vague
LLMJudge(rubric='Check quality')  # What aspect of quality?

```

**Good rubrics (specific):**
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(rubric='Response directly answers the user question without hallucination')
LLMJudge(rubric='Response uses formal, professional language appropriate for business communication')
LLMJudge(rubric='All factual claims in the response are supported by the provided context')

```

### Including Context
Control what information the judge sees:
```
from pydantic_evals.evaluators import LLMJudge

# Output only (default)
LLMJudge(rubric='Response is polite')

# Output + Input
LLMJudge(
    rubric='Response accurately answers the input question',
    include_input=True,
)

# Output + Input + Expected Output
LLMJudge(
    rubric='Response is semantically equivalent to the expected output',
    include_input=True,
    include_expected_output=True,
)

```

**Example:**
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge

dataset = Dataset(
    cases=[
        Case(
            inputs='What is 2+2?',
            expected_output='4',
        ),
    ],
    evaluators=[
        # This judge sees: output + inputs + expected_output
        LLMJudge(
            rubric='Response provides the same answer as expected, possibly with explanation',
            include_input=True,
            include_expected_output=True,
        ),
    ],
)

```

### Model Selection
Choose the judge model based on cost/quality tradeoffs:
```
from pydantic_evals.evaluators import LLMJudge

# Default: GPT-4o (good balance)
LLMJudge(rubric='...')

# Anthropic Claude (alternative default)
LLMJudge(
    rubric='...',
    model='anthropic:claude-sonnet-4-6',
)

# Cheaper option for simple checks
LLMJudge(
    rubric='Response contains profanity',
    model='openai:gpt-5-mini',
)

# Premium option for nuanced evaluation
LLMJudge(
    rubric='Response demonstrates deep understanding of quantum mechanics',
    model='anthropic:claude-opus-4-5',
)

```

### Model Settings
Customize model behavior:
```
from pydantic_ai.settings import ModelSettings
from pydantic_evals.evaluators import LLMJudge

LLMJudge(
    rubric='...',
    model_settings=ModelSettings(
        temperature=0.0,  # Deterministic evaluation
        max_tokens=100,  # Shorter responses
    ),
)

```

## Output Modes
### Assertion Only (Default)
Returns pass/fail with reason:
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(rubric='Response is accurate')
# Returns: {'LLMJudge_pass': EvaluationReason(value=True, reason='...')}

```

In reports:
```
┃ Assertions ┃
┃ ✔          ┃

```

### Score Only
Returns a numeric score (0.0 to 1.0):
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(
    rubric='Response quality',
    score={'include_reason': True},
    assertion=False,
)
# Returns: {'LLMJudge_score': EvaluationReason(value=0.85, reason='...')}

```

In reports:
```
┃ Scores             ┃
┃ LLMJudge_score: 0.85 ┃

```

### Both Score and Assertion
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(
    rubric='Response quality',
    score={'include_reason': True},
    assertion={'include_reason': True},
)
# Returns: {
#     'LLMJudge_score': EvaluationReason(value=0.85, reason='...'),
#     'LLMJudge_pass': EvaluationReason(value=True, reason='...'),
# }

```

### Custom Names
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(
    rubric='Response is factually accurate',
    assertion={
        'evaluation_name': 'accuracy',
        'include_reason': True,
    },
)
# Returns: {'accuracy': EvaluationReason(value=True, reason='...')}

```

In reports:
```
┃ Assertions ┃
┃ accuracy: ✔ ┃

```

## Practical Examples
### RAG Evaluation
Evaluate whether a RAG system uses provided context:
```
from dataclasses import dataclass

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge


@dataclass
class RAGInput:
    question: str
    context: str


dataset = Dataset(
    cases=[
        Case(
            inputs=RAGInput(
                question='What is the capital of France?',
                context='France is a country in Europe. Its capital is Paris.',
            ),
        ),
    ],
    evaluators=[
        LLMJudge(
            rubric='Response answers the question using only information from the provided context',
            include_input=True,
            assertion={'evaluation_name': 'grounded', 'include_reason': True},
        ),
        LLMJudge(
            rubric='Response cites specific quotes or facts from the context',
            include_input=True,
            assertion={'evaluation_name': 'uses_citations', 'include_reason': True},
        ),
    ],
)

```

### Recipe Generation with Case-Specific Rubrics
This example shows how to use both dataset-level and case-specific evaluators:
[With Pydantic AI Gateway](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__tabbed_1_1)[Directly to Provider API](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__tabbed_1_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) recipe_evaluation.py```
from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from pydantic_ai import Agent, format_as_xml
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import IsInstance, LLMJudge


class CustomerOrder(BaseModel):
    dish_name: str
    dietary_restriction: str | None = None


class Recipe(BaseModel):
    ingredients: list[str]
    steps: list[str]


recipe_agent = Agent(
    'gateway/openai:gpt-5-mini',
    output_type=Recipe,
    instructions=(
        'Generate a recipe to cook the dish that meets the dietary restrictions.'
    ),
)


async def transform_recipe(customer_order: CustomerOrder) -> Recipe:
    r = await recipe_agent.run(format_as_xml(customer_order))
    return r.output


recipe_dataset = Dataset[CustomerOrder, Recipe, Any](
    cases=[
        Case(
            name='vegetarian_recipe',
            inputs=CustomerOrder(
                dish_name='Spaghetti Bolognese', dietary_restriction='vegetarian'
            ),
            expected_output=None,
            metadata={'focus': 'vegetarian'},
            evaluators=(  [](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__code_15_annotation_1)
                LLMJudge(
                    rubric='Recipe should not contain meat or animal products',
                ),
            ),
        ),
        Case(
            name='gluten_free_recipe',
            inputs=CustomerOrder(
                dish_name='Chocolate Cake', dietary_restriction='gluten-free'
            ),
            expected_output=None,
            metadata={'focus': 'gluten-free'},
            evaluators=(  [](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__code_15_annotation_2)
                LLMJudge(
                    rubric='Recipe should not contain gluten or wheat products',
                ),
            ),
        ),
    ],
    evaluators=[  [](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__code_15_annotation_3)
        IsInstance(type_name='Recipe'),
        LLMJudge(
            rubric='Recipe should have clear steps and relevant ingredients',
            include_input=True,
            model='anthropic:claude-sonnet-4-6',
        ),
    ],
)


report = recipe_dataset.evaluate_sync(transform_recipe)
print(report)
"""
     Evaluation Summary: transform_recipe
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID            ┃ Assertions ┃ Duration ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ vegetarian_recipe  │ ✔✔✔        │    38.1s │
├────────────────────┼────────────┼──────────┤
│ gluten_free_recipe │ ✔✔✔        │    22.4s │
├────────────────────┼────────────┼──────────┤
│ Averages           │ 100.0% ✔   │    30.3s │
└────────────────────┴────────────┴──────────┘
"""

```

recipe_evaluation.py```
from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from pydantic_ai import Agent, format_as_xml
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import IsInstance, LLMJudge


class CustomerOrder(BaseModel):
    dish_name: str
    dietary_restriction: str | None = None


class Recipe(BaseModel):
    ingredients: list[str]
    steps: list[str]


recipe_agent = Agent(
    'openai:gpt-5-mini',
    output_type=Recipe,
    instructions=(
        'Generate a recipe to cook the dish that meets the dietary restrictions.'
    ),
)


async def transform_recipe(customer_order: CustomerOrder) -> Recipe:
    r = await recipe_agent.run(format_as_xml(customer_order))
    return r.output


recipe_dataset = Dataset[CustomerOrder, Recipe, Any](
    cases=[
        Case(
            name='vegetarian_recipe',
            inputs=CustomerOrder(
                dish_name='Spaghetti Bolognese', dietary_restriction='vegetarian'
            ),
            expected_output=None,
            metadata={'focus': 'vegetarian'},
            evaluators=(

[](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__code_16_annotation_1)
                LLMJudge(
                    rubric='Recipe should not contain meat or animal products',
                ),
            ),
        ),
        Case(
            name='gluten_free_recipe',
            inputs=CustomerOrder(
                dish_name='Chocolate Cake', dietary_restriction='gluten-free'
            ),
            expected_output=None,
            metadata={'focus': 'gluten-free'},
            evaluators=(

[](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__code_16_annotation_2)
                LLMJudge(
                    rubric='Recipe should not contain gluten or wheat products',
                ),
            ),
        ),
    ],
    evaluators=[

[](https://ai.pydantic.dev/evals/evaluators/llm-judge/#__code_16_annotation_3)
        IsInstance(type_name='Recipe'),
        LLMJudge(
            rubric='Recipe should have clear steps and relevant ingredients',
            include_input=True,
            model='anthropic:claude-sonnet-4-6',
        ),
    ],
)


report = recipe_dataset.evaluate_sync(transform_recipe)
print(report)
"""
     Evaluation Summary: transform_recipe
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID            ┃ Assertions ┃ Duration ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ vegetarian_recipe  │ ✔✔✔        │    38.1s │
├────────────────────┼────────────┼──────────┤
│ gluten_free_recipe │ ✔✔✔        │    22.4s │
├────────────────────┼────────────┼──────────┤
│ Averages           │ 100.0% ✔   │    30.3s │
└────────────────────┴────────────┴──────────┘
"""

```

  1. Case-specific evaluator - only runs for the vegetarian recipe case
  2. Case-specific evaluator - only runs for the gluten-free recipe case
  3. Dataset-level evaluators - run for all cases


### Multi-Aspect Evaluation
Use multiple judges for different quality dimensions:
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # Accuracy
        LLMJudge(
            rubric='Response is factually accurate',
            include_input=True,
            assertion={'evaluation_name': 'accurate'},
        ),

        # Helpfulness
        LLMJudge(
            rubric='Response is helpful and actionable',
            include_input=True,
            score={'evaluation_name': 'helpfulness'},
            assertion=False,
        ),

        # Tone
        LLMJudge(
            rubric='Response uses professional, respectful language',
            assertion={'evaluation_name': 'professional_tone'},
        ),

        # Safety
        LLMJudge(
            rubric='Response contains no harmful, biased, or inappropriate content',
            assertion={'evaluation_name': 'safe'},
        ),
    ],
)

```

### Comparative Evaluation
Compare output against expected output:
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge

dataset = Dataset(
    cases=[
        Case(
            name='translation',
            inputs='Hello world',
            expected_output='Bonjour le monde',
        ),
    ],
    evaluators=[
        LLMJudge(
            rubric='Response is semantically equivalent to the expected output',
            include_input=True,
            include_expected_output=True,
            score={'evaluation_name': 'semantic_similarity'},
            assertion={'evaluation_name': 'correct_meaning'},
        ),
    ],
)

```

## Best Practices
### 1. Be Specific in Rubrics
**Bad:**
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(rubric='Good answer')

```

**Better:**
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(rubric='Response accurately answers the question without hallucinating facts')

```

**Best:**
```
from pydantic_evals.evaluators import LLMJudge

LLMJudge(
    rubric='''
    Response must:
    1. Directly answer the question asked
    2. Use only information from the provided context
    3. Cite specific passages from the context
    4. Acknowledge if information is insufficient
    ''',
    include_input=True,
)

```

### 2. Use Multiple Judges
Don't always try to evaluate everything with one rubric:
```
from pydantic_evals.evaluators import LLMJudge

# Instead of this:
LLMJudge(rubric='Response is good, accurate, helpful, and safe')

# Do this:
evaluators = [
    LLMJudge(rubric='Response is factually accurate'),
    LLMJudge(rubric='Response is helpful and actionable'),
    LLMJudge(rubric='Response is safe and appropriate'),
]

```

### 3. Combine with Deterministic Checks
Don't use LLM evaluation for checks that can be done deterministically:
```
from pydantic_evals.evaluators import Contains, IsInstance, LLMJudge

evaluators = [
    IsInstance(type_name='str'),
    Contains(value='required_section'),
    LLMJudge(rubric='Response quality is high'),
]

```

### 4. Use Temperature 0 for Consistency
```
from pydantic_ai.settings import ModelSettings
from pydantic_evals.evaluators import LLMJudge

LLMJudge(
    rubric='...',
    model_settings=ModelSettings(temperature=0.0),
)

```

## Limitations
### Non-Determinism
LLM judges are not deterministic. The same output may receive different scores across runs.
**Mitigation:**
  * Use `temperature=0.0` for more consistency
  * Run multiple evaluations and average
  * Use retry strategies for flaky evaluations


### Cost
LLM judges make API calls, which cost money and time.
**Mitigation:**
  * Use cheaper models for simple checks (`gpt-5-mini`)
  * Run deterministic checks first to fail fast
  * Cache results when possible
  * Limit evaluation to changed cases


### Model Biases
LLM judges inherit biases from their training data.
**Mitigation:**
  * Use multiple judge models and compare
  * Review evaluation reasons, not just scores
  * Validate judges against human-labeled test sets
  * Be aware of known biases (length bias, style preferences)


### Context Limits
Judges have token limits for inputs.
**Mitigation:**
  * Truncate long inputs/outputs intelligently
  * Use focused rubrics that don't require full context
  * Consider chunked evaluation for very long content


## Debugging LLM Judges
### View Reasons
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge


def my_task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[LLMJudge(rubric='Response is clear')],
)
report = dataset.evaluate_sync(my_task)
report.print(include_reasons=True)
"""
     Evaluation Summary: my_task
┏━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID  ┃ Assertions  ┃ Duration ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ Case 1   │ LLMJudge: ✔ │     10ms │
│          │   Reason: - │          │
│          │             │          │
│          │             │          │
├──────────┼─────────────┼──────────┤
│ Averages │ 100.0% ✔    │     10ms │
└──────────┴─────────────┴──────────┘
"""

```

Output:
```
┃ Assertions              ┃
┃ accuracy: ✔            ┃
┃   Reason: The response │
┃   correctly states...  │

```

### Access Programmatically
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge


def my_task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[LLMJudge(rubric='Response is clear')],
)
report = dataset.evaluate_sync(my_task)
for case in report.cases:
    for name, result in case.assertions.items():
        print(f'{name}: {result.value}')
        #> LLMJudge: True
        if result.reason:
            print(f'  Reason: {result.reason}')
            #>   Reason: -

```

### Compare Judges
Test the same cases with different judge models:
```
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge


def my_task(inputs: str) -> str:
    return f'Result: {inputs}'


judges = [
    LLMJudge(rubric='Response is clear', model='openai:gpt-5.2'),
    LLMJudge(rubric='Response is clear', model='anthropic:claude-sonnet-4-6'),
    LLMJudge(rubric='Response is clear', model='openai:gpt-5-mini'),
]

for judge in judges:
    dataset = Dataset(cases=[Case(inputs='test')], evaluators=[judge])
    report = dataset.evaluate_sync(my_task)
    # Compare results

```

## Advanced: Custom Judge Models
Set a default judge model for all `LLMJudge` evaluators:
```
from pydantic_evals.evaluators import LLMJudge
from pydantic_evals.evaluators.llm_as_a_judge import set_default_judge_model

# Set default to Claude
set_default_judge_model('anthropic:claude-sonnet-4-6')

# Now all LLMJudge instances use Claude by default
LLMJudge(rubric='...')  # Uses Claude

```

## Next Steps
  * **[Custom Evaluators](https://ai.pydantic.dev/evals/evaluators/custom/)** - Write custom evaluation logic
  * **[Built-in Evaluators](https://ai.pydantic.dev/evals/evaluators/built-in/)** - Complete evaluator reference


© Pydantic Services Inc. 2024 to present
