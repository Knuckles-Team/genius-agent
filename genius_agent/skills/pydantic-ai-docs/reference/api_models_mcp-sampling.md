[ Skip to content ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_aimodelsmcp_sampling)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_ai.models.mcp_sampling
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
      * pydantic_ai.models.mcp_sampling  [ pydantic_ai.models.mcp_sampling  ](https://ai.pydantic.dev/api/models/mcp-sampling/)
        * [ mcp_sampling  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling)
        * [ MCPSamplingModelSettings  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModelSettings)
          * [ mcp_model_preferences  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModelSettings.mcp_model_preferences)
        * [ MCPSamplingModel  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel)
          * [ session  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.session)
          * [ default_max_tokens  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.default_max_tokens)
          * [ model_name  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.model_name)
          * [ system  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.system)
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


  * [ mcp_sampling  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling)
  * [ MCPSamplingModelSettings  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModelSettings)
    * [ mcp_model_preferences  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModelSettings.mcp_model_preferences)
  * [ MCPSamplingModel  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel)
    * [ session  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.session)
    * [ default_max_tokens  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.default_max_tokens)
    * [ model_name  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.model_name)
    * [ system  ](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel.system)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_ai  ](https://ai.pydantic.dev/api/ag_ui/)


# pydantic_ai.models.mcp_sampling
###  MCPSamplingModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings used for an MCP Sampling model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/mcp_sampling.py`
```
19
20
21
22
23
24
25
```
| ```
class MCPSamplingModelSettings(ModelSettings, total=False):
    """Settings used for an MCP Sampling model request."""

    # ALL FIELDS MUST BE `mcp_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    mcp_model_preferences: ModelPreferences
    """Model preferences to use for MCP Sampling."""

```

---|---
####  mcp_model_preferences `instance-attribute`
```
mcp_model_preferences: ModelPreferences

```

Model preferences to use for MCP Sampling.
###  MCPSamplingModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses MCP Sampling.
[MCP Sampling](https://modelcontextprotocol.io/docs/concepts/sampling) allows an MCP server to make requests to a model by calling back to the MCP client that connected to it.
Source code in `pydantic_ai_slim/pydantic_ai/models/mcp_sampling.py`
```
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
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
```
| ```
@dataclass
class MCPSamplingModel(Model):
    """A model that uses MCP Sampling.

    [MCP Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
    allows an MCP server to make requests to a model by calling back to the MCP client that connected to it.
    """

    session: ServerSession
    """The MCP server session to use for sampling."""

    _: KW_ONLY

    default_max_tokens: int = 16_384
    """Default max tokens to use if not set in [`ModelSettings`][pydantic_ai.settings.ModelSettings.max_tokens].

    Max tokens is a required parameter for MCP Sampling, but optional on
    [`ModelSettings`][pydantic_ai.settings.ModelSettings], so this value is used as fallback.
    """

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        system_prompt, sampling_messages = _mcp.map_from_pai_messages(messages)

        model_settings, _ = self.prepare_request(model_settings, model_request_parameters)
        model_settings = cast(MCPSamplingModelSettings, model_settings or {})

        result = await self.session.create_message(
            sampling_messages,
            max_tokens=model_settings.get('max_tokens', self.default_max_tokens),
            system_prompt=system_prompt,
            temperature=model_settings.get('temperature'),
            model_preferences=model_settings.get('mcp_model_preferences'),
            stop_sequences=model_settings.get('stop_sequences'),
        )
        if result.role == 'assistant':
            return ModelResponse(
                parts=[_mcp.map_from_sampling_content(result.content)],
                model_name=result.model,
            )
        else:
            raise exceptions.UnexpectedModelBehavior(
                f'Unexpected result from MCP sampling, expected "assistant" role, got {result.role}.'
            )

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        raise NotImplementedError('MCP Sampling does not support streaming')
        yield

    @property
    def model_name(self) -> str:
        """The model name.

        Since the model name isn't known until the request is made, this property always returns `'mcp-sampling'`.
        """
        return 'mcp-sampling'

    @property
    def system(self) -> str:
        """The system / model provider, returns `'MCP'`."""
        return 'MCP'

```

---|---
####  session `instance-attribute`
```
session: ServerSession[](https://modelcontextprotocol.github.io/python-sdk/api/#mcp.ServerSession "mcp.ServerSession")

```

The MCP server session to use for sampling.
####  default_max_tokens `class-attribute` `instance-attribute`
```
default_max_tokens: int[](https://docs.python.org/3/library/functions.html#int) = 16384

```

Default max tokens to use if not set in [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings.max_tokens "max_tokens



      instance-attribute
  ").
Max tokens is a required parameter for MCP Sampling, but optional on [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings"), so this value is used as fallback.
####  model_name `property`
```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The model name.
Since the model name isn't known until the request is made, this property always returns `'mcp-sampling'`.
####  system `property`
```
system: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The system / model provider, returns `'MCP'`.
© Pydantic Services Inc. 2024 to present
