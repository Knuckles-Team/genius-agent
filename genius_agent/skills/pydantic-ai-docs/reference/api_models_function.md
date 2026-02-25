[ Skip to content ](https://ai.pydantic.dev/api/models/function/#pydantic_aimodelsfunction)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_ai.models.function
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
      * pydantic_ai.models.function  [ pydantic_ai.models.function  ](https://ai.pydantic.dev/api/models/function/)
        * [ function  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function)
        * [ FunctionModel  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel)
          * [ __init__  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.__init__)
          * [ model_name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.model_name)
          * [ system  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.system)
          * [ supported_builtin_tools  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.supported_builtin_tools)
        * [ AgentInfo  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo)
          * [ function_tools  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.function_tools)
          * [ allow_text_output  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.allow_text_output)
          * [ output_tools  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.output_tools)
          * [ model_settings  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.model_settings)
          * [ model_request_parameters  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.model_request_parameters)
          * [ instructions  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.instructions)
        * [ DeltaToolCall  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall)
          * [ name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall.name)
          * [ json_args  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall.json_args)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall.tool_call_id)
        * [ DeltaThinkingPart  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart)
          * [ content  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart.content)
          * [ signature  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart.signature)
        * [ DeltaToolCalls  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCalls)
        * [ DeltaThinkingCalls  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingCalls)
        * [ FunctionDef  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionDef)
        * [ StreamFunctionDef  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.StreamFunctionDef)
        * [ FunctionStreamedResponse  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse)
          * [ model_name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.model_name)
          * [ provider_name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.provider_name)
          * [ provider_url  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.provider_url)
          * [ timestamp  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.timestamp)
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


  * [ function  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function)
  * [ FunctionModel  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel)
    * [ __init__  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.__init__)
    * [ model_name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.model_name)
    * [ system  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.system)
    * [ supported_builtin_tools  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel.supported_builtin_tools)
  * [ AgentInfo  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo)
    * [ function_tools  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.function_tools)
    * [ allow_text_output  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.allow_text_output)
    * [ output_tools  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.output_tools)
    * [ model_settings  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.model_settings)
    * [ model_request_parameters  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.model_request_parameters)
    * [ instructions  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo.instructions)
  * [ DeltaToolCall  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall)
    * [ name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall.name)
    * [ json_args  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall.json_args)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall.tool_call_id)
  * [ DeltaThinkingPart  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart)
    * [ content  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart.content)
    * [ signature  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart.signature)
  * [ DeltaToolCalls  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCalls)
  * [ DeltaThinkingCalls  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingCalls)
  * [ FunctionDef  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionDef)
  * [ StreamFunctionDef  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.StreamFunctionDef)
  * [ FunctionStreamedResponse  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse)
    * [ model_name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.model_name)
    * [ provider_name  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.provider_name)
    * [ provider_url  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.provider_url)
    * [ timestamp  ](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionStreamedResponse.timestamp)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_ai  ](https://ai.pydantic.dev/api/ag_ui/)


# `pydantic_ai.models.function`
A model controlled by a local function.
[`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel "FunctionModel



      dataclass
  ") is similar to [`TestModel`](https://ai.pydantic.dev/api/models/test/), but allows greater control over the model's behavior.
Its primary use case is for more advanced unit testing than is possible with `TestModel`.
Here's a minimal example:
[With Pydantic AI Gateway](https://ai.pydantic.dev/api/models/function/#__tabbed_1_1)[Directly to Provider API](https://ai.pydantic.dev/api/models/function/#__tabbed_1_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) function_model_usage.py```
from pydantic_ai import Agent
from pydantic_ai import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import FunctionModel, AgentInfo

my_agent = Agent('gateway/openai:gpt-5.2')


async def model_function(
    messages: list[ModelMessage], info: AgentInfo
) -> ModelResponse:
    print(messages)
    """
    [
        ModelRequest(
            parts=[
                UserPromptPart(
                    content='Testing my agent...',
                    timestamp=datetime.datetime(...),
                )
            ],
            timestamp=datetime.datetime(...),
            run_id='...',
        )
    ]
    """
    print(info)
    """
    AgentInfo(
        function_tools=[],
        allow_text_output=True,
        output_tools=[],
        model_settings=None,
        model_request_parameters=ModelRequestParameters(
            function_tools=[], builtin_tools=[], output_tools=[]
        ),
        instructions=None,
    )
    """
    return ModelResponse(parts=[TextPart('hello world')])


async def test_my_agent():
    """Unit test for my_agent, to be run by pytest."""
    with my_agent.override(model=FunctionModel(model_function)):
        result = await my_agent.run('Testing my agent...')
        assert result.output == 'hello world'

```

function_model_usage.py```
from pydantic_ai import Agent
from pydantic_ai import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import FunctionModel, AgentInfo

my_agent = Agent('openai:gpt-5.2')


async def model_function(
    messages: list[ModelMessage], info: AgentInfo
) -> ModelResponse:
    print(messages)
    """
    [
        ModelRequest(
            parts=[
                UserPromptPart(
                    content='Testing my agent...',
                    timestamp=datetime.datetime(...),
                )
            ],
            timestamp=datetime.datetime(...),
            run_id='...',
        )
    ]
    """
    print(info)
    """
    AgentInfo(
        function_tools=[],
        allow_text_output=True,
        output_tools=[],
        model_settings=None,
        model_request_parameters=ModelRequestParameters(
            function_tools=[], builtin_tools=[], output_tools=[]
        ),
        instructions=None,
    )
    """
    return ModelResponse(parts=[TextPart('hello world')])


async def test_my_agent():
    """Unit test for my_agent, to be run by pytest."""
    with my_agent.override(model=FunctionModel(model_function)):
        result = await my_agent.run('Testing my agent...')
        assert result.output == 'hello world'

```

See [Unit testing with `FunctionModel`](https://ai.pydantic.dev/testing/#unit-testing-with-functionmodel) for detailed documentation.
###  FunctionModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model controlled by a local function.
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
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
115
116
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
```
| ```
@dataclass(init=False)
class FunctionModel(Model):
    """A model controlled by a local function.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    function: FunctionDef | None
    stream_function: StreamFunctionDef | None

    _model_name: str = field(repr=False)
    _system: str = field(default='function', repr=False)

    @overload
    def __init__(
        self,
        function: FunctionDef,
        *,
        model_name: str | None = None,
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        stream_function: StreamFunctionDef,
        model_name: str | None = None,
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        function: FunctionDef,
        *,
        stream_function: StreamFunctionDef,
        model_name: str | None = None,
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ) -> None: ...

    def __init__(
        self,
        function: FunctionDef | None = None,
        *,
        stream_function: StreamFunctionDef | None = None,
        model_name: str | None = None,
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize a `FunctionModel`.

        Either `function` or `stream_function` must be provided, providing both is allowed.

        Args:
            function: The function to call for non-streamed requests.
            stream_function: The function to call for streamed requests.
            model_name: The name of the model. If not provided, a name is generated from the function names.
            profile: The model profile to use.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        if function is None and stream_function is None:
            raise TypeError('Either `function` or `stream_function` must be provided')

        self.function = function
        self.stream_function = stream_function

        function_name = self.function.__name__ if self.function is not None else ''
        stream_function_name = self.stream_function.__name__ if self.stream_function is not None else ''
        self._model_name = model_name or f'function:{function_name}:{stream_function_name}'

        # Use a default profile that supports JSON schema and object output if none provided
        if profile is None:
            profile = ModelProfile(
                supports_json_schema_output=True,
                supports_json_object_output=True,
            )
        super().__init__(settings=settings, profile=profile)

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        agent_info = AgentInfo(
            function_tools=model_request_parameters.function_tools,
            allow_text_output=model_request_parameters.allow_text_output,
            output_tools=model_request_parameters.output_tools,
            model_settings=model_settings,
            model_request_parameters=model_request_parameters,
            instructions=self._get_instructions(messages, model_request_parameters),
        )

        assert self.function is not None, 'FunctionModel must receive a `function` to support non-streamed requests'

        if inspect.iscoroutinefunction(self.function):
            response = await self.function(messages, agent_info)
        else:
            response_ = await _utils.run_in_executor(self.function, messages, agent_info)
            assert isinstance(response_, ModelResponse), response_
            response = response_
        response.model_name = self._model_name
        # Add usage data if not already present
        if not response.usage.has_values():  # pragma: no branch
            response.usage = _estimate_usage(chain(messages, [response]))
        return response

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        agent_info = AgentInfo(
            function_tools=model_request_parameters.function_tools,
            allow_text_output=model_request_parameters.allow_text_output,
            output_tools=model_request_parameters.output_tools,
            model_settings=model_settings,
            model_request_parameters=model_request_parameters,
            instructions=self._get_instructions(messages, model_request_parameters),
        )

        assert self.stream_function is not None, (
            'FunctionModel must receive a `stream_function` to support streamed requests'
        )

        response_stream = PeekableAsyncStream(self.stream_function(messages, agent_info))

        first = await response_stream.peek()
        if isinstance(first, _utils.Unset):
            raise ValueError('Stream function must return at least one item')

        yield FunctionStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=self._model_name,
            _iter=response_stream,
        )

    @property
    def model_name(self) -> str:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The system / model provider."""
        return self._system

    @classmethod
    def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
        """FunctionModel supports all builtin tools for testing flexibility."""
        from ..builtin_tools import SUPPORTED_BUILTIN_TOOLS

        return SUPPORTED_BUILTIN_TOOLS

```

---|---
####  __init__
```
__init__(
    function: FunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionDef "FunctionDef



      module-attribute
   \(pydantic_ai.models.function.FunctionDef\)"),
    *,
    model_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
) -> None

```

```
__init__(
    *,
    stream_function: StreamFunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.StreamFunctionDef "StreamFunctionDef



      module-attribute
   \(pydantic_ai.models.function.StreamFunctionDef\)"),
    model_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
) -> None

```

```
__init__(
    function: FunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionDef "FunctionDef



      module-attribute
   \(pydantic_ai.models.function.FunctionDef\)"),
    *,
    stream_function: StreamFunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.StreamFunctionDef "StreamFunctionDef



      module-attribute
   \(pydantic_ai.models.function.StreamFunctionDef\)"),
    model_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
) -> None

```

```
__init__(
    function: FunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionDef "FunctionDef



      module-attribute
   \(pydantic_ai.models.function.FunctionDef\)") | None = None,
    *,
    stream_function: StreamFunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.StreamFunctionDef "StreamFunctionDef



      module-attribute
   \(pydantic_ai.models.function.StreamFunctionDef\)") | None = None,
    model_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize a `FunctionModel`.
Either `function` or `stream_function` must be provided, providing both is allowed.
Parameters:
Name | Type | Description | Default
---|---|---|---
`function` |  `FunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionDef "FunctionDef



      module-attribute
   \(pydantic_ai.models.function.FunctionDef\)") | None` |  The function to call for non-streamed requests. |  `None`
`stream_function` |  `StreamFunctionDef[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.StreamFunctionDef "StreamFunctionDef



      module-attribute
   \(pydantic_ai.models.function.StreamFunctionDef\)") | None` |  The function to call for streamed requests. |  `None`
`model_name` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  The name of the model. If not provided, a name is generated from the function names. |  `None`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
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
115
116
117
118
119
120
121
122
```
| ```
def __init__(
    self,
    function: FunctionDef | None = None,
    *,
    stream_function: StreamFunctionDef | None = None,
    model_name: str | None = None,
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize a `FunctionModel`.

    Either `function` or `stream_function` must be provided, providing both is allowed.

    Args:
        function: The function to call for non-streamed requests.
        stream_function: The function to call for streamed requests.
        model_name: The name of the model. If not provided, a name is generated from the function names.
        profile: The model profile to use.
        settings: Model-specific settings that will be used as defaults for this model.
    """
    if function is None and stream_function is None:
        raise TypeError('Either `function` or `stream_function` must be provided')

    self.function = function
    self.stream_function = stream_function

    function_name = self.function.__name__ if self.function is not None else ''
    stream_function_name = self.stream_function.__name__ if self.stream_function is not None else ''
    self._model_name = model_name or f'function:{function_name}:{stream_function_name}'

    # Use a default profile that supports JSON schema and object output if none provided
    if profile is None:
        profile = ModelProfile(
            supports_json_schema_output=True,
            supports_json_object_output=True,
        )
    super().__init__(settings=settings, profile=profile)

```

---|---
####  model_name `property`
```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The model name.
####  system `property`
```
system: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The system / model provider.
####  supported_builtin_tools `classmethod`
```
supported_builtin_tools() -> (
    frozenset[](https://docs.python.org/3/library/stdtypes.html#frozenset)[type[](https://docs.python.org/3/library/functions.html#type)[AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")]]
)

```

FunctionModel supports all builtin tools for testing flexibility.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
204
205
206
207
208
209
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """FunctionModel supports all builtin tools for testing flexibility."""
    from ..builtin_tools import SUPPORTED_BUILTIN_TOOLS

    return SUPPORTED_BUILTIN_TOOLS

```

---|---
###  AgentInfo `dataclass`
Information about an agent.
This is passed as the second to functions used within [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel "FunctionModel



      dataclass
  ").
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
212
213
214
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
```
| ```
@dataclass(frozen=True, kw_only=True)
class AgentInfo:
    """Information about an agent.

    This is passed as the second to functions used within [`FunctionModel`][pydantic_ai.models.function.FunctionModel].
    """

    function_tools: list[ToolDefinition]
    """The function tools available on this agent.

    These are the tools registered via the [`tool`][pydantic_ai.agent.Agent.tool] and
    [`tool_plain`][pydantic_ai.agent.Agent.tool_plain] decorators.
    """
    allow_text_output: bool
    """Whether a plain text output is allowed."""
    output_tools: list[ToolDefinition]
    """The tools that can called to produce the final output of the run."""
    model_settings: ModelSettings | None
    """The model settings passed to the run call."""
    model_request_parameters: ModelRequestParameters
    """The model request parameters passed to the run call."""
    instructions: str | None
    """The instructions passed to model."""

```

---|---
####  function_tools `instance-attribute`
```
function_tools: list[](https://docs.python.org/3/library/stdtypes.html#list)[ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
   \(pydantic_ai.tools.ToolDefinition\)")]

```

The function tools available on this agent.
These are the tools registered via the [`tool`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool "tool") and [`tool_plain`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool_plain "tool_plain") decorators.
####  allow_text_output `instance-attribute`
```
allow_text_output: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Whether a plain text output is allowed.
####  output_tools `instance-attribute`
```
output_tools: list[](https://docs.python.org/3/library/stdtypes.html#list)[ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
   \(pydantic_ai.tools.ToolDefinition\)")]

```

The tools that can called to produce the final output of the run.
####  model_settings `instance-attribute`
```
model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None

```

The model settings passed to the run call.
####  model_request_parameters `instance-attribute`
```
model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)")

```

The model request parameters passed to the run call.
####  instructions `instance-attribute`
```
instructions: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

The instructions passed to model.
###  DeltaToolCall `dataclass`
Incremental change to a tool call.
Used to describe a chunk when streaming structured responses.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
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
```
| ```
@dataclass
class DeltaToolCall:
    """Incremental change to a tool call.

    Used to describe a chunk when streaming structured responses.
    """

    name: str | None = None
    """Incremental change to the name of the tool."""

    json_args: str | None = None
    """Incremental change to the arguments as JSON"""

    _: KW_ONLY

    tool_call_id: str | None = None
    """Incremental change to the tool call ID."""

```

---|---
####  name `class-attribute` `instance-attribute`
```
name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental change to the name of the tool.
####  json_args `class-attribute` `instance-attribute`
```
json_args: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental change to the arguments as JSON
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental change to the tool call ID.
###  DeltaThinkingPart `dataclass`
Incremental change to a thinking part.
Used to describe a chunk when streaming thinking responses.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
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
```
| ```
@dataclass(kw_only=True)
class DeltaThinkingPart:
    """Incremental change to a thinking part.

    Used to describe a chunk when streaming thinking responses.
    """

    content: str | None = None
    """Incremental change to the thinking content."""
    signature: str | None = None
    """Incremental change to the thinking signature."""

```

---|---
####  content `class-attribute` `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental change to the thinking content.
####  signature `class-attribute` `instance-attribute`
```
signature: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental change to the thinking signature.
###  DeltaToolCalls `module-attribute`
```
DeltaToolCalls: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = dict[](https://docs.python.org/3/library/stdtypes.html#dict)[int[](https://docs.python.org/3/library/functions.html#int), DeltaToolCall[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCall "DeltaToolCall



      dataclass
   \(pydantic_ai.models.function.DeltaToolCall\)")]

```

A mapping of tool call IDs to incremental changes.
###  DeltaThinkingCalls `module-attribute`
```
DeltaThinkingCalls: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = dict[](https://docs.python.org/3/library/stdtypes.html#dict)[int[](https://docs.python.org/3/library/functions.html#int), DeltaThinkingPart[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingPart "DeltaThinkingPart



      dataclass
   \(pydantic_ai.models.function.DeltaThinkingPart\)")]

```

A mapping of thinking call IDs to incremental changes.
###  FunctionDef `module-attribute`
```
FunctionDef: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
    [list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")], AgentInfo[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo "AgentInfo



      dataclass
   \(pydantic_ai.models.function.AgentInfo\)")],
    ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)") | Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")],
]

```

A function used to generate a non-streamed response.
###  StreamFunctionDef `module-attribute`
```
StreamFunctionDef: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
    [list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")], AgentInfo[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.AgentInfo "AgentInfo



      dataclass
   \(pydantic_ai.models.function.AgentInfo\)")],
    AsyncIterator[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator")[
        str[](https://docs.python.org/3/library/stdtypes.html#str)
        | DeltaToolCalls[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaToolCalls "DeltaToolCalls



      module-attribute
   \(pydantic_ai.models.function.DeltaToolCalls\)")
        | DeltaThinkingCalls[](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.DeltaThinkingCalls "DeltaThinkingCalls



      module-attribute
   \(pydantic_ai.models.function.DeltaThinkingCalls\)")
        | BuiltinToolCallsReturns
    ],
]

```

A function used to generate a streamed response.
While this is defined as having return type of `AsyncIterator[str | DeltaToolCalls | DeltaThinkingCalls | BuiltinTools]`, it should really be considered as `AsyncIterator[str] | AsyncIterator[DeltaToolCalls] | AsyncIterator[DeltaThinkingCalls]`,
E.g. you need to yield all text, all `DeltaToolCalls`, all `DeltaThinkingCalls`, or all `BuiltinToolCallsReturns`, not mix them.
###  FunctionStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for [FunctionModel](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel "FunctionModel



      dataclass
  ").
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
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
310
311
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
```
| ```
@dataclass
class FunctionStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for [FunctionModel][pydantic_ai.models.function.FunctionModel]."""

    _model_name: str
    _iter: AsyncIterator[str | DeltaToolCalls | DeltaThinkingCalls | BuiltinToolCallsReturns]
    _timestamp: datetime = field(default_factory=_utils.now_utc)

    def __post_init__(self):
        self._usage += _estimate_usage([])

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:  # noqa: C901
        async for item in self._iter:
            if isinstance(item, str):
                response_tokens = _estimate_string_tokens(item)
                self._usage += usage.RequestUsage(output_tokens=response_tokens)
                for event in self._parts_manager.handle_text_delta(vendor_part_id='content', content=item):
                    yield event
            elif isinstance(item, dict) and item:
                for dtc_index, delta in item.items():
                    if isinstance(delta, DeltaThinkingPart):
                        if delta.content:  # pragma: no branch
                            response_tokens = _estimate_string_tokens(delta.content)
                            self._usage += usage.RequestUsage(output_tokens=response_tokens)
                        for event in self._parts_manager.handle_thinking_delta(
                            vendor_part_id=dtc_index,
                            content=delta.content,
                            signature=delta.signature,
                            provider_name='function' if delta.signature else None,
                        ):
                            yield event
                    elif isinstance(delta, DeltaToolCall):
                        if delta.json_args:
                            response_tokens = _estimate_string_tokens(delta.json_args)
                            self._usage += usage.RequestUsage(output_tokens=response_tokens)
                        maybe_event = self._parts_manager.handle_tool_call_delta(
                            vendor_part_id=dtc_index,
                            tool_name=delta.name,
                            args=delta.json_args,
                            tool_call_id=delta.tool_call_id,
                        )
                        if maybe_event is not None:  # pragma: no branch
                            yield maybe_event
                    elif isinstance(delta, BuiltinToolCallPart):
                        if content := delta.args_as_json_str():  # pragma: no branch
                            response_tokens = _estimate_string_tokens(content)
                            self._usage += usage.RequestUsage(output_tokens=response_tokens)
                        yield self._parts_manager.handle_part(vendor_part_id=dtc_index, part=delta)
                    elif isinstance(delta, BuiltinToolReturnPart):
                        if content := delta.model_response_str():  # pragma: no branch
                            response_tokens = _estimate_string_tokens(content)
                            self._usage += usage.RequestUsage(output_tokens=response_tokens)
                        yield self._parts_manager.handle_part(vendor_part_id=dtc_index, part=delta)
                    else:
                        assert_never(delta)

    @property
    def model_name(self) -> str:
        """Get the model name of the response."""
        return self._model_name

    @property
    def provider_name(self) -> None:
        """Get the provider name."""
        return None

    @property
    def provider_url(self) -> None:
        """Get the provider base URL."""
        return None

    @property
    def timestamp(self) -> datetime:
        """Get the timestamp of the response."""
        return self._timestamp

```

---|---
####  model_name `property`
```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Get the model name of the response.
####  provider_name `property`
```
provider_name: None

```

Get the provider name.
####  provider_url `property`
```
provider_url: None

```

Get the provider base URL.
####  timestamp `property`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")

```

Get the timestamp of the response.
© Pydantic Services Inc. 2024 to present
