[ Skip to content ](https://ai.pydantic.dev/api/messages/#pydantic_aimessages)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_ai.messages
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
      * pydantic_ai.messages  [ pydantic_ai.messages  ](https://ai.pydantic.dev/api/messages/)
        * [ messages  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages)
        * [ FinishReason  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinishReason)
        * [ ForceDownloadMode  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ForceDownloadMode)
        * [ ProviderDetailsDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ProviderDetailsDelta)
        * [ SystemPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.content)
          * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.timestamp)
          * [ dynamic_ref  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.dynamic_ref)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.part_kind)
        * [ FileUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl)
          * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.url)
          * [ force_download  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.force_download)
          * [ vendor_metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.vendor_metadata)
          * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.media_type)
          * [ identifier  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.identifier)
          * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.format)
        * [ VideoUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl)
          * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.url)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.kind)
          * [ is_youtube  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.is_youtube)
          * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.format)
        * [ AudioUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl)
          * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.url)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.kind)
          * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.format)
        * [ ImageUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl)
          * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.url)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.kind)
          * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.format)
        * [ DocumentUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl)
          * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.url)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.kind)
          * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.format)
        * [ BinaryContent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent)
          * [ data  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.data)
          * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.media_type)
          * [ vendor_metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.vendor_metadata)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.kind)
          * [ narrow_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.narrow_type)
          * [ from_data_uri  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.from_data_uri)
          * [ from_path  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.from_path)
          * [ identifier  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.identifier)
          * [ data_uri  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.data_uri)
          * [ base64  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.base64)
          * [ is_audio  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_audio)
          * [ is_image  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_image)
          * [ is_video  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_video)
          * [ is_document  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_document)
          * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.format)
        * [ BinaryImage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage)
        * [ CachePoint  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.CachePoint)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.CachePoint.kind)
          * [ ttl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.CachePoint.ttl)
        * [ MULTI_MODAL_CONTENT_TYPES  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.MULTI_MODAL_CONTENT_TYPES)
        * [ MultiModalContent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.MultiModalContent)
        * [ ToolReturn  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn)
          * [ return_value  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn.return_value)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn.content)
          * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn.metadata)
        * [ UserPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.content)
          * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.timestamp)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.part_kind)
        * [ BaseToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart)
          * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.tool_name)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.content)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.tool_call_id)
          * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.metadata)
          * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.timestamp)
          * [ model_response_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.model_response_str)
          * [ model_response_object  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.model_response_object)
          * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.has_content)
        * [ ToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.part_kind)
        * [ BuiltinToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart.provider_details)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart.part_kind)
        * [ RetryPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.content)
          * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_name)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_call_id)
          * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.timestamp)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.part_kind)
          * [ model_response  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.model_response)
        * [ ModelRequestPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart)
        * [ ModelRequest  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest)
          * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.parts)
          * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.timestamp)
          * [ instructions  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.instructions)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.kind)
          * [ run_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.run_id)
          * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.metadata)
          * [ user_text_prompt  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.user_text_prompt)
        * [ TextPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.content)
          * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.id)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.provider_details)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.part_kind)
          * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.has_content)
        * [ ThinkingPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.content)
          * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.id)
          * [ signature  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.signature)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.provider_details)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.part_kind)
          * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.has_content)
        * [ FilePart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.content)
          * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.id)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.provider_details)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.part_kind)
          * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.has_content)
        * [ BaseToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart)
          * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.tool_name)
          * [ args  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.args)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.tool_call_id)
          * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.id)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.provider_details)
          * [ args_as_dict  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.args_as_dict)
          * [ args_as_json_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.args_as_json_str)
          * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.has_content)
        * [ ToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.part_kind)
        * [ BuiltinToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart)
          * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart.part_kind)
        * [ ModelResponsePart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart)
        * [ ModelResponse  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse)
          * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.parts)
          * [ usage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.usage)
          * [ model_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.model_name)
          * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.timestamp)
          * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.kind)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_name)
          * [ provider_url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_url)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_details)
          * [ provider_response_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_response_id)
          * [ finish_reason  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.finish_reason)
          * [ run_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.run_id)
          * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.metadata)
          * [ text  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.text)
          * [ thinking  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.thinking)
          * [ files  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.files)
          * [ images  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.images)
          * [ tool_calls  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.tool_calls)
          * [ builtin_tool_calls  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.builtin_tool_calls)
          * [ price  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.price)
          * [ cost  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.cost)
          * [ otel_events  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.otel_events)
        * [ ModelMessage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage)
        * [ ModelMessagesTypeAdapter  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessagesTypeAdapter)
        * [ TextPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta)
          * [ content_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.content_delta)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.provider_details)
          * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.part_delta_kind)
          * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.apply)
        * [ ThinkingPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta)
          * [ content_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.content_delta)
          * [ signature_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.signature_delta)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.provider_details)
          * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.part_delta_kind)
          * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.apply)
        * [ ToolCallPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta)
          * [ tool_name_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_name_delta)
          * [ args_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.args_delta)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_call_id)
          * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.provider_name)
          * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.provider_details)
          * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.part_delta_kind)
          * [ as_part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.as_part)
          * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.apply)
        * [ ModelResponsePartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta)
        * [ PartStartEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent)
          * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.index)
          * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.part)
          * [ previous_part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.previous_part_kind)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.event_kind)
        * [ PartDeltaEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent)
          * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.index)
          * [ delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.delta)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.event_kind)
        * [ PartEndEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent)
          * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.index)
          * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.part)
          * [ next_part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.next_part_kind)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.event_kind)
        * [ FinalResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent)
          * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_name)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_call_id)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.event_kind)
        * [ ModelResponseStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent)
        * [ FunctionToolCallEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent)
          * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.part)
          * [ args_valid  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.args_valid)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.event_kind)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.tool_call_id)
          * [ call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.call_id)
        * [ FunctionToolResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent)
          * [ result  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.result)
          * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.content)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.event_kind)
          * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.tool_call_id)
        * [ BuiltinToolCallEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent)
          * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent.part)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent.event_kind)
        * [ BuiltinToolResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent)
          * [ result  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent.result)
          * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent.event_kind)
        * [ HandleResponseEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.HandleResponseEvent)
        * [ AgentStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent)
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


  * [ messages  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages)
  * [ FinishReason  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinishReason)
  * [ ForceDownloadMode  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ForceDownloadMode)
  * [ ProviderDetailsDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ProviderDetailsDelta)
  * [ SystemPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.content)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.timestamp)
    * [ dynamic_ref  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.dynamic_ref)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.part_kind)
  * [ FileUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.url)
    * [ force_download  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.force_download)
    * [ vendor_metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.vendor_metadata)
    * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.media_type)
    * [ identifier  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.identifier)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl.format)
  * [ VideoUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.kind)
    * [ is_youtube  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.is_youtube)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl.format)
  * [ AudioUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.kind)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.format)
  * [ ImageUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.kind)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.format)
  * [ DocumentUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.kind)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.format)
  * [ BinaryContent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent)
    * [ data  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.data)
    * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.media_type)
    * [ vendor_metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.vendor_metadata)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.kind)
    * [ narrow_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.narrow_type)
    * [ from_data_uri  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.from_data_uri)
    * [ from_path  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.from_path)
    * [ identifier  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.identifier)
    * [ data_uri  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.data_uri)
    * [ base64  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.base64)
    * [ is_audio  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_audio)
    * [ is_image  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_image)
    * [ is_video  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_video)
    * [ is_document  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_document)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.format)
  * [ BinaryImage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage)
  * [ CachePoint  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.CachePoint)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.CachePoint.kind)
    * [ ttl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.CachePoint.ttl)
  * [ MULTI_MODAL_CONTENT_TYPES  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.MULTI_MODAL_CONTENT_TYPES)
  * [ MultiModalContent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.MultiModalContent)
  * [ ToolReturn  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn)
    * [ return_value  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn.return_value)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn.content)
    * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn.metadata)
  * [ UserPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.content)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.timestamp)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.part_kind)
  * [ BaseToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.tool_name)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.content)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.tool_call_id)
    * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.metadata)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.timestamp)
    * [ model_response_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.model_response_str)
    * [ model_response_object  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.model_response_object)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart.has_content)
  * [ ToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.part_kind)
  * [ BuiltinToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart.provider_details)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart.part_kind)
  * [ RetryPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.content)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_name)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_call_id)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.timestamp)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.part_kind)
    * [ model_response  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.model_response)
  * [ ModelRequestPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart)
  * [ ModelRequest  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest)
    * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.parts)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.timestamp)
    * [ instructions  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.instructions)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.kind)
    * [ run_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.run_id)
    * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.metadata)
    * [ user_text_prompt  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.user_text_prompt)
  * [ TextPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.content)
    * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.id)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.provider_details)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.part_kind)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.has_content)
  * [ ThinkingPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.content)
    * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.id)
    * [ signature  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.signature)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.provider_details)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.part_kind)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart.has_content)
  * [ FilePart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.content)
    * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.id)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.provider_details)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.part_kind)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart.has_content)
  * [ BaseToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.tool_name)
    * [ args  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.args)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.tool_call_id)
    * [ id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.id)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.provider_details)
    * [ args_as_dict  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.args_as_dict)
    * [ args_as_json_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.args_as_json_str)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart.has_content)
  * [ ToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.part_kind)
  * [ BuiltinToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart.part_kind)
  * [ ModelResponsePart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart)
  * [ ModelResponse  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse)
    * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.parts)
    * [ usage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.usage)
    * [ model_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.model_name)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.timestamp)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.kind)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_name)
    * [ provider_url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_url)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_details)
    * [ provider_response_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_response_id)
    * [ finish_reason  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.finish_reason)
    * [ run_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.run_id)
    * [ metadata  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.metadata)
    * [ text  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.text)
    * [ thinking  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.thinking)
    * [ files  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.files)
    * [ images  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.images)
    * [ tool_calls  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.tool_calls)
    * [ builtin_tool_calls  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.builtin_tool_calls)
    * [ price  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.price)
    * [ cost  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.cost)
    * [ otel_events  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.otel_events)
  * [ ModelMessage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage)
  * [ ModelMessagesTypeAdapter  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessagesTypeAdapter)
  * [ TextPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta)
    * [ content_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.content_delta)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.provider_details)
    * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.part_delta_kind)
    * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.apply)
  * [ ThinkingPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta)
    * [ content_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.content_delta)
    * [ signature_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.signature_delta)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.provider_details)
    * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.part_delta_kind)
    * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta.apply)
  * [ ToolCallPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta)
    * [ tool_name_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_name_delta)
    * [ args_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.args_delta)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_call_id)
    * [ provider_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.provider_name)
    * [ provider_details  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.provider_details)
    * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.part_delta_kind)
    * [ as_part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.as_part)
    * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.apply)
  * [ ModelResponsePartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta)
  * [ PartStartEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent)
    * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.index)
    * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.part)
    * [ previous_part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.previous_part_kind)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.event_kind)
  * [ PartDeltaEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent)
    * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.index)
    * [ delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.delta)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.event_kind)
  * [ PartEndEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent)
    * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.index)
    * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.part)
    * [ next_part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.next_part_kind)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent.event_kind)
  * [ FinalResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_name)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_call_id)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.event_kind)
  * [ ModelResponseStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent)
  * [ FunctionToolCallEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent)
    * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.part)
    * [ args_valid  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.args_valid)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.event_kind)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.tool_call_id)
    * [ call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.call_id)
  * [ FunctionToolResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent)
    * [ result  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.result)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.content)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.event_kind)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.tool_call_id)
  * [ BuiltinToolCallEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent)
    * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent.part)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent.event_kind)
  * [ BuiltinToolResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent)
    * [ result  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent.result)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent.event_kind)
  * [ HandleResponseEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.HandleResponseEvent)
  * [ AgentStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_ai  ](https://ai.pydantic.dev/api/ag_ui/)


# `pydantic_ai.messages`
The structure of [`ModelMessage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
  ") can be shown as a graph:
###  FinishReason `module-attribute`
```
FinishReason: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
    "stop", "length", "content_filter", "tool_call", "error"
]

```

Reason the model finished generating the response, normalized to OpenTelemetry values.
###  ForceDownloadMode `module-attribute`
```
ForceDownloadMode: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = bool[](https://docs.python.org/3/library/functions.html#bool) | Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["allow-local"]

```

Type for the force_download parameter on FileUrl subclasses.
  * `False`: The URL is sent directly to providers that support it. For providers that don't, the file is downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * `True`: The file is always downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * `'allow-local'`: The file is always downloaded, allowing private IPs but still blocking cloud metadata.


###  ProviderDetailsDelta `module-attribute`
```
ProviderDetailsDelta: TypeAlias[](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") = (
    dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]
    | Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None], dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]]
    | None
)

```

Type for provider_details input: can be a static dict, a callback to update existing details, or None.
###  SystemPromptPart `dataclass`
A system prompt, generally written by the application developer.
This gives the model context and guidance on how to respond.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass(repr=False)
class SystemPromptPart:
    """A system prompt, generally written by the application developer.

    This gives the model context and guidance on how to respond.
    """

    content: str
    """The content of the prompt."""

    _: KW_ONLY

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp of the prompt."""

    dynamic_ref: str | None = None
    """The ref of the dynamic system prompt function that generated this part.

    Only set if system prompt is dynamic, see [`system_prompt`][pydantic_ai.agent.Agent.system_prompt] for more information.
    """

    part_kind: Literal['system-prompt'] = 'system-prompt'
    """Part type identifier, this is available on all parts as a discriminator."""

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        return LogRecord(
            attributes={'event.name': 'gen_ai.system.message'},
            body={'role': 'system', **({'content': self.content} if settings.include_content else {})},
        )

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        return [_otel_messages.TextPart(type='text', **{'content': self.content} if settings.include_content else {})]

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The content of the prompt.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp of the prompt.
####  dynamic_ref `class-attribute` `instance-attribute`
```
dynamic_ref: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The ref of the dynamic system prompt function that generated this part.
Only set if system prompt is dynamic, see [`system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt "system_prompt") for more information.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['system-prompt'] = 'system-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
###  FileUrl
Bases: `ABC[](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`
Abstract base class for any URL-based file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class FileUrl(ABC):
    """Abstract base class for any URL-based file."""

    url: str
    """The URL of the file."""

    _: KW_ONLY

    force_download: ForceDownloadMode = False
    """Controls whether the file is downloaded and how SSRF protection is applied:

    * If `False`, the URL is sent directly to providers that support it. For providers that don't,
      the file is downloaded with SSRF protection (blocks private IPs and cloud metadata).
    * If `True`, the file is always downloaded with SSRF protection (blocks private IPs and cloud metadata).
    * If `'allow-local'`, the file is always downloaded, allowing private IPs but still blocking cloud metadata.
    """

    vendor_metadata: dict[str, Any] | None = None
    """Vendor-specific metadata for the file.

    Supported by:
    - `GoogleModel`: `VideoUrl.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing
    - `OpenAIChatModel`, `OpenAIResponsesModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images
    - `XaiModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images
    """

    _media_type: Annotated[str | None, pydantic.Field(alias='media_type', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    _identifier: Annotated[str | None, pydantic.Field(alias='identifier', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `media_type` and `identifier` aliases.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    @pydantic.computed_field
    @property
    def media_type(self) -> str:
        """Return the media type of the file, based on the URL or the provided `media_type`."""
        return self._media_type or self._infer_media_type()

    @pydantic.computed_field
    @property
    def identifier(self) -> str:
        """The identifier of the file, such as a unique ID.

        This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument,
        and the tool can look up the file in question by iterating over the message history and finding the matching `FileUrl`.

        This identifier is only automatically passed to the model when the `FileUrl` is returned by a tool.
        If you're passing the `FileUrl` as a user message, it's up to you to include a separate text part with the identifier,
        e.g. "This is file <identifier>:" preceding the `FileUrl`.

        It's also included in inline-text delimiters for providers that require inlining text documents, so the model can
        distinguish multiple files.
        """
        return self._identifier or _multi_modal_content_identifier(self.url)

    @abstractmethod
    def _infer_media_type(self) -> str:
        """Infer the media type of the file based on the URL."""
        raise NotImplementedError

    @property
    @abstractmethod
    def format(self) -> str:
        """The file format."""
        raise NotImplementedError

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the file.
####  force_download `class-attribute` `instance-attribute`
```
force_download: ForceDownloadMode[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ForceDownloadMode "ForceDownloadMode



      module-attribute
   \(pydantic_ai.messages.ForceDownloadMode\)") = False

```

Controls whether the file is downloaded and how SSRF protection is applied:
  * If `False`, the URL is sent directly to providers that support it. For providers that don't, the file is downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * If `True`, the file is always downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * If `'allow-local'`, the file is always downloaded, allowing private IPs but still blocking cloud metadata.


####  vendor_metadata `class-attribute` `instance-attribute`
```
vendor_metadata: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Vendor-specific metadata for the file.
Supported by: - `GoogleModel`: `VideoUrl.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing - `OpenAIChatModel`, `OpenAIResponsesModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images - `XaiModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images
####  media_type `property`
```
media_type: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return the media type of the file, based on the URL or the provided `media_type`.
####  identifier `property`
```
identifier: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The identifier of the file, such as a unique ID.
This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument, and the tool can look up the file in question by iterating over the message history and finding the matching `FileUrl`.
This identifier is only automatically passed to the model when the `FileUrl` is returned by a tool. If you're passing the `FileUrl` as a user message, it's up to you to include a separate text part with the identifier, e.g. "This is file :" preceding the `FileUrl`.
It's also included in inline-text delimiters for providers that require inlining text documents, so the model can distinguish multiple files.
####  format `abstractmethod` `property`
```
format: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The file format.
###  VideoUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
A URL to a video.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
310
311
312
313
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class VideoUrl(FileUrl):
    """A URL to a video."""

    url: str
    """The URL of the video."""

    _: KW_ONLY

    kind: Literal['video-url'] = 'video-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['video-url'] = 'video-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the video, based on the url."""
        # Assume that YouTube videos are mp4 because there would be no extension
        # to infer from. This should not be a problem, as Gemini disregards media
        # type for YouTube URLs.
        if self.is_youtube:
            return 'video/mp4'

        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from video URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def is_youtube(self) -> bool:
        """True if the URL has a YouTube domain."""
        parsed = urlparse(self.url)
        hostname = parsed.hostname
        return hostname in ('youtu.be', 'youtube.com', 'www.youtube.com')

    @property
    def format(self) -> VideoFormat:
        """The file format of the video.

        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
        """
        return _video_format_lookup[self.media_type]

```

---|---
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the video.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['video-url'] = 'video-url'

```

Type identifier, this is available on all parts as a discriminator.
####  is_youtube `property`
```
is_youtube: bool[](https://docs.python.org/3/library/functions.html#bool)

```

True if the URL has a YouTube domain.
####  format `property`
```
format: VideoFormat

```

The file format of the video.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  AudioUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
A URL to an audio file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class AudioUrl(FileUrl):
    """A URL to an audio file."""

    url: str
    """The URL of the audio file."""

    _: KW_ONLY

    kind: Literal['audio-url'] = 'audio-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['audio-url'] = 'audio-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the audio file, based on the url.

        References:
        - Gemini: https://ai.google.dev/gemini-api/docs/audio#supported-formats
        """
        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from audio URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def format(self) -> AudioFormat:
        """The file format of the audio file."""
        return _audio_format_lookup[self.media_type]

```

---|---
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the audio file.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['audio-url'] = 'audio-url'

```

Type identifier, this is available on all parts as a discriminator.
####  format `property`
```
format: AudioFormat

```

The file format of the audio file.
###  ImageUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
A URL to an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class ImageUrl(FileUrl):
    """A URL to an image."""

    url: str
    """The URL of the image."""

    _: KW_ONLY

    kind: Literal['image-url'] = 'image-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['image-url'] = 'image-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the image, based on the url."""
        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from image URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def format(self) -> ImageFormat:
        """The file format of the image.

        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
        """
        return _image_format_lookup[self.media_type]

```

---|---
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the image.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['image-url'] = 'image-url'

```

Type identifier, this is available on all parts as a discriminator.
####  format `property`
```
format: ImageFormat

```

The file format of the image.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  DocumentUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
The URL of the document.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class DocumentUrl(FileUrl):
    """The URL of the document."""

    url: str
    """The URL of the document."""

    _: KW_ONLY

    kind: Literal['document-url'] = 'document-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['document-url'] = 'document-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the document, based on the url."""
        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from document URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def format(self) -> DocumentFormat:
        """The file format of the document.

        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
        """
        media_type = self.media_type
        try:
            return _document_format_lookup[media_type]
        except KeyError as e:
            raise ValueError(f'Unknown document media type: {media_type}') from e

```

---|---
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the document.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['document-url'] = 'document-url'

```

Type identifier, this is available on all parts as a discriminator.
####  format `property`
```
format: DocumentFormat

```

The file format of the document.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  BinaryContent
Binary content, e.g. an audio or image file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
```
| ```
@pydantic_dataclass(
    repr=False,
    config=pydantic.ConfigDict(
        ser_json_bytes='base64',
        val_json_bytes='base64',
    ),
)
class BinaryContent:
    """Binary content, e.g. an audio or image file."""

    data: bytes
    """The binary file data.

    Use `.base64` to get the base64-encoded string.
    """

    _: KW_ONLY

    media_type: AudioMediaType | ImageMediaType | DocumentMediaType | str
    """The media type of the binary data."""

    vendor_metadata: dict[str, Any] | None = None
    """Vendor-specific metadata for the file.

    Supported by:
    - `GoogleModel`: `BinaryContent.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing
    - `OpenAIChatModel`, `OpenAIResponsesModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images
    - `XaiModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images
    """

    _identifier: Annotated[str | None, pydantic.Field(alias='identifier', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    kind: Literal['binary'] = 'binary'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `identifier` alias for the `_identifier` field.
    def __init__(
        self,
        data: bytes,
        *,
        media_type: AudioMediaType | ImageMediaType | DocumentMediaType | str,
        identifier: str | None = None,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['binary'] = 'binary',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    @staticmethod
    def narrow_type(bc: BinaryContent) -> BinaryContent | BinaryImage:
        """Narrow the type of the `BinaryContent` to `BinaryImage` if it's an image."""
        if bc.is_image:
            return BinaryImage(
                data=bc.data,
                media_type=bc.media_type,
                identifier=bc.identifier,
                vendor_metadata=bc.vendor_metadata,
            )
        else:
            return bc

    @classmethod
    def from_data_uri(cls, data_uri: str) -> BinaryContent:
        """Create a `BinaryContent` from a data URI."""
        prefix = 'data:'
        if not data_uri.startswith(prefix):
            raise ValueError('Data URI must start with "data:"')
        media_type, data = data_uri[len(prefix) :].split(';base64,', 1)
        return cls.narrow_type(cls(data=base64.b64decode(data), media_type=media_type))

    @classmethod
    def from_path(cls, path: PathLike[str]) -> BinaryContent:
        """Create a `BinaryContent` from a path.

        Defaults to 'application/octet-stream' if the media type cannot be inferred.

        Raises:
            FileNotFoundError: if the file does not exist.
            PermissionError: if the file cannot be read.
        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f'File not found: {path}')
        media_type, _ = _mime_types.guess_type(path)
        if media_type is None:
            media_type = 'application/octet-stream'

        return cls.narrow_type(cls(data=path.read_bytes(), media_type=media_type))

    @pydantic.computed_field
    @property
    def identifier(self) -> str:
        """Identifier for the binary content, such as a unique ID.

        This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument,
        and the tool can look up the file in question by iterating over the message history and finding the matching `BinaryContent`.

        This identifier is only automatically passed to the model when the `BinaryContent` is returned by a tool.
        If you're passing the `BinaryContent` as a user message, it's up to you to include a separate text part with the identifier,
        e.g. "This is file <identifier>:" preceding the `BinaryContent`.

        It's also included in inline-text delimiters for providers that require inlining text documents, so the model can
        distinguish multiple files.
        """
        return self._identifier or _multi_modal_content_identifier(self.data)

    @property
    def data_uri(self) -> str:
        """Convert the `BinaryContent` to a data URI."""
        return f'data:{self.media_type};base64,{self.base64}'

    @property
    def base64(self) -> str:
        """Return the binary data as a base64-encoded string. Default encoding is UTF-8."""
        return base64.b64encode(self.data).decode()

    @property
    def is_audio(self) -> bool:
        """Return `True` if the media type is an audio type."""
        return self.media_type.startswith('audio/')

    @property
    def is_image(self) -> bool:
        """Return `True` if the media type is an image type."""
        return self.media_type.startswith('image/')

    @property
    def is_video(self) -> bool:
        """Return `True` if the media type is a video type."""
        return self.media_type.startswith('video/')

    @property
    def is_document(self) -> bool:
        """Return `True` if the media type is a document type."""
        return self.media_type in _document_format_lookup

    @property
    def format(self) -> str:
        """The file format of the binary content."""
        try:
            if self.is_audio:
                return _audio_format_lookup[self.media_type]
            elif self.is_image:
                return _image_format_lookup[self.media_type]
            elif self.is_video:
                return _video_format_lookup[self.media_type]
            else:
                return _document_format_lookup[self.media_type]
        except KeyError as e:
            raise ValueError(f'Unknown media type: {self.media_type}') from e

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  data `instance-attribute`
```
data: bytes[](https://docs.python.org/3/library/stdtypes.html#bytes)

```

The binary file data.
Use `.base64` to get the base64-encoded string.
####  media_type `instance-attribute`
```
media_type: (
    AudioMediaType
    | ImageMediaType
    | DocumentMediaType
    | str[](https://docs.python.org/3/library/stdtypes.html#str)
)

```

The media type of the binary data.
####  vendor_metadata `class-attribute` `instance-attribute`
```
vendor_metadata: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Vendor-specific metadata for the file.
Supported by: - `GoogleModel`: `BinaryContent.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing - `OpenAIChatModel`, `OpenAIResponsesModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images - `XaiModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['binary'] = 'binary'

```

Type identifier, this is available on all parts as a discriminator.
####  narrow_type `staticmethod`
```
narrow_type(
    bc: BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"),
) -> BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | BinaryImage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage \(pydantic_ai.messages.BinaryImage\)")

```

Narrow the type of the `BinaryContent` to `BinaryImage` if it's an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
510
511
512
513
514
515
516
517
518
519
520
521
```
| ```
@staticmethod
def narrow_type(bc: BinaryContent) -> BinaryContent | BinaryImage:
    """Narrow the type of the `BinaryContent` to `BinaryImage` if it's an image."""
    if bc.is_image:
        return BinaryImage(
            data=bc.data,
            media_type=bc.media_type,
            identifier=bc.identifier,
            vendor_metadata=bc.vendor_metadata,
        )
    else:
        return bc

```

---|---
####  from_data_uri `classmethod`
```
from_data_uri(data_uri: str[](https://docs.python.org/3/library/stdtypes.html#str)) -> BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")

```

Create a `BinaryContent` from a data URI.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
523
524
525
526
527
528
529
530
```
| ```
@classmethod
def from_data_uri(cls, data_uri: str) -> BinaryContent:
    """Create a `BinaryContent` from a data URI."""
    prefix = 'data:'
    if not data_uri.startswith(prefix):
        raise ValueError('Data URI must start with "data:"')
    media_type, data = data_uri[len(prefix) :].split(';base64,', 1)
    return cls.narrow_type(cls(data=base64.b64decode(data), media_type=media_type))

```

---|---
####  from_path `classmethod`
```
from_path(path: PathLike[](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")[str[](https://docs.python.org/3/library/stdtypes.html#str)]) -> BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")

```

Create a `BinaryContent` from a path.
Defaults to 'application/octet-stream' if the media type cannot be inferred.
Raises:
Type | Description
---|---
`FileNotFoundError[](https://docs.python.org/3/library/exceptions.html#FileNotFoundError)` |  if the file does not exist.
`PermissionError[](https://docs.python.org/3/library/exceptions.html#PermissionError)` |  if the file cannot be read.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
```
| ```
@classmethod
def from_path(cls, path: PathLike[str]) -> BinaryContent:
    """Create a `BinaryContent` from a path.

    Defaults to 'application/octet-stream' if the media type cannot be inferred.

    Raises:
        FileNotFoundError: if the file does not exist.
        PermissionError: if the file cannot be read.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f'File not found: {path}')
    media_type, _ = _mime_types.guess_type(path)
    if media_type is None:
        media_type = 'application/octet-stream'

    return cls.narrow_type(cls(data=path.read_bytes(), media_type=media_type))

```

---|---
####  identifier `property`
```
identifier: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Identifier for the binary content, such as a unique ID.
This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument, and the tool can look up the file in question by iterating over the message history and finding the matching `BinaryContent`.
This identifier is only automatically passed to the model when the `BinaryContent` is returned by a tool. If you're passing the `BinaryContent` as a user message, it's up to you to include a separate text part with the identifier, e.g. "This is file :" preceding the `BinaryContent`.
It's also included in inline-text delimiters for providers that require inlining text documents, so the model can distinguish multiple files.
####  data_uri `property`
```
data_uri: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Convert the `BinaryContent` to a data URI.
####  base64 `property`
```
base64: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return the binary data as a base64-encoded string. Default encoding is UTF-8.
####  is_audio `property`
```
is_audio: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is an audio type.
####  is_image `property`
```
is_image: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is an image type.
####  is_video `property`
```
is_video: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is a video type.
####  is_document `property`
```
is_document: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is a document type.
####  format `property`
```
format: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The file format of the binary content.
###  BinaryImage
Bases: `BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")`
Binary content that's guaranteed to be an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
```
| ```
@pydantic_dataclass(
    repr=False,
    config=pydantic.ConfigDict(
        ser_json_bytes='base64',
        val_json_bytes='base64',
    ),
)
class BinaryImage(BinaryContent):
    """Binary content that's guaranteed to be an image."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `identifier` alias for the `_identifier` field.
    def __init__(
        self,
        data: bytes,
        *,
        media_type: ImageMediaType | str,
        identifier: str | None = None,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['binary'] = 'binary',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def __post_init__(self):
        if not self.is_image:
            raise ValueError('`BinaryImage` must have a media type that starts with "image/"')

```

---|---
###  CachePoint `dataclass`
A cache point marker for prompt caching.
Can be inserted into UserPromptPart.content to mark cache boundaries. Models that don't support caching will filter these out.
Supported by:
  * Anthropic
  * Amazon Bedrock (Converse API)

Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
```
| ```
@dataclass
class CachePoint:
    """A cache point marker for prompt caching.

    Can be inserted into UserPromptPart.content to mark cache boundaries.
    Models that don't support caching will filter these out.

    Supported by:

    - Anthropic
    - Amazon Bedrock (Converse API)
    """

    kind: Literal['cache-point'] = 'cache-point'
    """Type identifier, this is available on all parts as a discriminator."""

    ttl: Literal['5m', '1h'] = '5m'
    """The cache time-to-live, either "5m" (5 minutes) or "1h" (1 hour).

    Supported by:

    * Anthropic (automatically omitted for Bedrock, as it does not support explicit TTL). See https://docs.claude.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration for more information."""

```

---|---
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['cache-point'] = 'cache-point'

```

Type identifier, this is available on all parts as a discriminator.
####  ttl `class-attribute` `instance-attribute`
```
ttl: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['5m', '1h'] = '5m'

```

The cache time-to-live, either "5m" (5 minutes) or "1h" (1 hour).
Supported by:
  * Anthropic (automatically omitted for Bedrock, as it does not support explicit TTL). See https://docs.claude.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration for more information.


###  MULTI_MODAL_CONTENT_TYPES `module-attribute`
```
MULTI_MODAL_CONTENT_TYPES = (
    ImageUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl "ImageUrl \(pydantic_ai.messages.ImageUrl\)"),
    AudioUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl "AudioUrl \(pydantic_ai.messages.AudioUrl\)"),
    DocumentUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl "DocumentUrl \(pydantic_ai.messages.DocumentUrl\)"),
    VideoUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl "VideoUrl \(pydantic_ai.messages.VideoUrl\)"),
    BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"),
)

```

Tuple of multi-modal content types for use with isinstance() checks.
###  MultiModalContent `module-attribute`
```
MultiModalContent = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    ImageUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl "ImageUrl \(pydantic_ai.messages.ImageUrl\)")
    | AudioUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl "AudioUrl \(pydantic_ai.messages.AudioUrl\)")
    | DocumentUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl "DocumentUrl \(pydantic_ai.messages.DocumentUrl\)")
    | VideoUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl "VideoUrl \(pydantic_ai.messages.VideoUrl\)")
    | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("kind"),
]

```

Union of all multi-modal content types with a discriminator for Pydantic validation.
###  ToolReturn `dataclass`
A structured return value for tools that need to provide both a return value and custom content to the model.
This class allows tools to return complex responses that include: - A return value for actual tool return - Custom content (including multi-modal content) to be sent to the model as a UserPromptPart - Optional metadata for application use
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
```
| ```
@dataclass(repr=False)
class ToolReturn:
    """A structured return value for tools that need to provide both a return value and custom content to the model.

    This class allows tools to return complex responses that include:
    - A return value for actual tool return
    - Custom content (including multi-modal content) to be sent to the model as a UserPromptPart
    - Optional metadata for application use
    """

    return_value: ToolReturnContent
    """The return value to be used in the tool response."""

    _: KW_ONLY

    content: str | Sequence[UserContent] | None = None
    """The content to be sent to the model as a UserPromptPart."""

    metadata: Any = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    kind: Literal['tool-return'] = 'tool-return'

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  return_value `instance-attribute`
```
return_value: ToolReturnContent

```

The return value to be used in the tool response.
####  content `class-attribute` `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[UserContent] | None = None

```

The content to be sent to the model as a UserPromptPart.
####  metadata `class-attribute` `instance-attribute`
```
metadata: Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
###  UserPromptPart `dataclass`
A user prompt, generally written by the end user.
Content comes from the `user_prompt` parameter of [`Agent.run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  "), [`Agent.run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_sync "run_sync"), and [`Agent.run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
```
| ```
@dataclass(repr=False)
class UserPromptPart:
    """A user prompt, generally written by the end user.

    Content comes from the `user_prompt` parameter of [`Agent.run`][pydantic_ai.agent.AbstractAgent.run],
    [`Agent.run_sync`][pydantic_ai.agent.AbstractAgent.run_sync], and [`Agent.run_stream`][pydantic_ai.agent.AbstractAgent.run_stream].
    """

    content: str | Sequence[UserContent]
    """The content of the prompt."""

    _: KW_ONLY

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp of the prompt."""

    part_kind: Literal['user-prompt'] = 'user-prompt'
    """Part type identifier, this is available on all parts as a discriminator."""

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        content: Any = [{'kind': part.pop('type'), **part} for part in self.otel_message_parts(settings)]
        for part in content:
            if part['kind'] == 'binary' and 'content' in part:
                part['binary_content'] = part.pop('content')
        content = [
            part['content'] if part == {'kind': 'text', 'content': part.get('content')} else part for part in content
        ]
        if content in ([{'kind': 'text'}], [self.content]):
            content = content[0]
        return LogRecord(attributes={'event.name': 'gen_ai.user.message'}, body={'content': content, 'role': 'user'})

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        parts: list[_otel_messages.MessagePart] = []
        content: Sequence[UserContent] = [self.content] if isinstance(self.content, str) else self.content
        for part in content:
            if isinstance(part, str):
                parts.append(
                    _otel_messages.TextPart(type='text', **({'content': part} if settings.include_content else {}))
                )
            elif isinstance(part, ImageUrl | AudioUrl | DocumentUrl | VideoUrl):
                if settings.version >= 4:
                    uri_part = _otel_messages.UriPart(type='uri')
                    modality = _kind_to_modality_lookup.get(part.kind)
                    if modality is not None:
                        uri_part['modality'] = modality
                    try:  # don't fail the whole message if media type can't be inferred for some reason, just omit it
                        uri_part['mime_type'] = part.media_type
                    except ValueError:
                        pass
                    if settings.include_content:
                        uri_part['uri'] = part.url
                    parts.append(uri_part)
                else:
                    parts.append(
                        _otel_messages.MediaUrlPart(
                            type=part.kind,
                            **{'url': part.url} if settings.include_content else {},
                        )
                    )
            elif isinstance(part, BinaryContent):
                parts.append(_convert_binary_to_otel_part(part.media_type, lambda p=part: p.base64, settings))
            elif isinstance(part, CachePoint):
                # CachePoint is a marker, not actual content - skip it for otel
                pass
            else:
                parts.append({'type': part.kind})  # pragma: no cover
        return parts

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[UserContent]

```

The content of the prompt.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp of the prompt.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['user-prompt'] = 'user-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
###  BaseToolReturnPart `dataclass`
Base class for tool return parts.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
```
| ```
@dataclass(repr=False)
class BaseToolReturnPart:
    """Base class for tool return parts."""

    tool_name: str
    """The name of the "tool" was called."""

    content: ToolReturnContent
    """The return value."""

    tool_call_id: str = field(default_factory=_generate_tool_call_id)
    """The tool call identifier, this is used by some models including OpenAI.

    In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
    """

    _: KW_ONLY

    metadata: Any = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp, when the tool returned."""

    def model_response_str(self) -> str:
        """Return a string representation of the content for the model."""
        if isinstance(self.content, str):
            return self.content
        else:
            return tool_return_ta.dump_json(self.content).decode()

    def model_response_object(self) -> dict[str, Any]:
        """Return a dictionary representation of the content, wrapping non-dict types appropriately."""
        # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
        json_content = tool_return_ta.dump_python(self.content, mode='json')
        if isinstance(json_content, dict):
            return json_content  # type: ignore[reportUnknownReturn]
        else:
            return {'return_value': json_content}

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        body: AnyValue = {
            'role': 'tool',
            'id': self.tool_call_id,
            'name': self.tool_name,
        }
        if settings.include_content:
            body['content'] = self.content  # pyright: ignore[reportArgumentType]

        return LogRecord(
            body=body,
            attributes={'event.name': 'gen_ai.tool.message'},
        )

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        from .models.instrumented import InstrumentedModel

        part = _otel_messages.ToolCallResponsePart(
            type='tool_call_response',
            id=self.tool_call_id,
            name=self.tool_name,
        )

        if settings.include_content and self.content is not None:
            part['result'] = InstrumentedModel.serialize_any(self.content)

        return [part]

    def has_content(self) -> bool:
        """Return `True` if the tool return has content."""
        return self.content is not None  # pragma: no cover

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The name of the "tool" was called.
####  content `instance-attribute`
```
content: ToolReturnContent

```

The return value.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(
    default_factory=generate_tool_call_id
)

```

The tool call identifier, this is used by some models including OpenAI.
In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
####  metadata `class-attribute` `instance-attribute`
```
metadata: Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp, when the tool returned.
####  model_response_str
```
model_response_str() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return a string representation of the content for the model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
890
891
892
893
894
895
```
| ```
def model_response_str(self) -> str:
    """Return a string representation of the content for the model."""
    if isinstance(self.content, str):
        return self.content
    else:
        return tool_return_ta.dump_json(self.content).decode()

```

---|---
####  model_response_object
```
model_response_object() -> dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

Return a dictionary representation of the content, wrapping non-dict types appropriately.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
897
898
899
900
901
902
903
904
```
| ```
def model_response_object(self) -> dict[str, Any]:
    """Return a dictionary representation of the content, wrapping non-dict types appropriately."""
    # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
    json_content = tool_return_ta.dump_python(self.content, mode='json')
    if isinstance(json_content, dict):
        return json_content  # type: ignore[reportUnknownReturn]
    else:
        return {'return_value': json_content}

```

---|---
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the tool return has content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
934
935
936
```
| ```
def has_content(self) -> bool:
    """Return `True` if the tool return has content."""
    return self.content is not None  # pragma: no cover

```

---|---
###  ToolReturnPart `dataclass`
Bases: `BaseToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart "BaseToolReturnPart



      dataclass
   \(pydantic_ai.messages.BaseToolReturnPart\)")`
A tool return message, this encodes the result of running a tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
941
942
943
944
945
946
947
948
```
| ```
@dataclass(repr=False)
class ToolReturnPart(BaseToolReturnPart):
    """A tool return message, this encodes the result of running a tool."""

    _: KW_ONLY

    part_kind: Literal['tool-return'] = 'tool-return'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['tool-return'] = 'tool-return'

```

Part type identifier, this is available on all parts as a discriminator.
###  BuiltinToolReturnPart `dataclass`
Bases: `BaseToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart "BaseToolReturnPart



      dataclass
   \(pydantic_ai.messages.BaseToolReturnPart\)")`
A tool return message from a built-in tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
```
| ```
@dataclass(repr=False)
class BuiltinToolReturnPart(BaseToolReturnPart):
    """A tool return message from a built-in tool."""

    _: KW_ONLY

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Required to be set when `provider_details` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data."""

    part_kind: Literal['builtin-tool-return'] = 'builtin-tool-return'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
Required to be set when `provider_details` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["builtin-tool-return"] = (
    "builtin-tool-return"
)

```

Part type identifier, this is available on all parts as a discriminator.
###  RetryPromptPart `dataclass`
A message back to a model asking it to try again.
This can be sent for a number of reasons:
  * Pydantic validation of tool arguments failed, here content is derived from a Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
  * a tool raised a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") exception
  * no tool was found for the tool name
  * the model returned plain text when a structured response was expected
  * Pydantic validation of a structured response failed, here content is derived from a Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
  * an output validator raised a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") exception

Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
```
| ```
@dataclass(repr=False)
class RetryPromptPart:
    """A message back to a model asking it to try again.

    This can be sent for a number of reasons:

    * Pydantic validation of tool arguments failed, here content is derived from a Pydantic
      [`ValidationError`][pydantic_core.ValidationError]
    * a tool raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
    * no tool was found for the tool name
    * the model returned plain text when a structured response was expected
    * Pydantic validation of a structured response failed, here content is derived from a Pydantic
      [`ValidationError`][pydantic_core.ValidationError]
    * an output validator raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
    """

    content: list[pydantic_core.ErrorDetails] | str
    """Details of why and how the model should retry.

    If the retry was triggered by a [`ValidationError`][pydantic_core.ValidationError], this will be a list of
    error details.
    """

    _: KW_ONLY

    tool_name: str | None = None
    """The name of the tool that was called, if any."""

    tool_call_id: str = field(default_factory=_generate_tool_call_id)
    """The tool call identifier, this is used by some models including OpenAI.

    In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
    """

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp, when the retry was triggered."""

    part_kind: Literal['retry-prompt'] = 'retry-prompt'
    """Part type identifier, this is available on all parts as a discriminator."""

    def model_response(self) -> str:
        """Return a string message describing why the retry is requested."""
        if isinstance(self.content, str):
            if self.tool_name is None:
                description = f'Validation feedback:\n{self.content}'
            else:
                description = self.content
        else:
            json_errors = error_details_ta.dump_json(self.content, exclude={'__all__': {'ctx'}}, indent=2)
            plural = isinstance(self.content, list) and len(self.content) != 1
            description = (
                f'{len(self.content)} validation error{"s" if plural else ""}:\n```json\n{json_errors.decode()}\n```'
            )
        return f'{description}\n\nFix the errors and try again.'

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        if self.tool_name is None:
            return LogRecord(
                attributes={'event.name': 'gen_ai.user.message'},
                body={'content': self.model_response(), 'role': 'user'},
            )
        else:
            return LogRecord(
                attributes={'event.name': 'gen_ai.tool.message'},
                body={
                    **({'content': self.model_response()} if settings.include_content else {}),
                    'role': 'tool',
                    'id': self.tool_call_id,
                    'name': self.tool_name,
                },
            )

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        if self.tool_name is None:
            return [_otel_messages.TextPart(type='text', content=self.model_response())]
        else:
            part = _otel_messages.ToolCallResponsePart(
                type='tool_call_response',
                id=self.tool_call_id,
                name=self.tool_name,
            )

            if settings.include_content:
                part['result'] = self.model_response()

            return [part]

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: list[](https://docs.python.org/3/library/stdtypes.html#list)[ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails "pydantic_core.ErrorDetails")] | str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Details of why and how the model should retry.
If the retry was triggered by a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError), this will be a list of error details.
####  tool_name `class-attribute` `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the tool that was called, if any.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(
    default_factory=generate_tool_call_id
)

```

The tool call identifier, this is used by some models including OpenAI.
In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp, when the retry was triggered.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['retry-prompt'] = 'retry-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
####  model_response
```
model_response() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return a string message describing why the retry is requested.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
```
| ```
def model_response(self) -> str:
    """Return a string message describing why the retry is requested."""
    if isinstance(self.content, str):
        if self.tool_name is None:
            description = f'Validation feedback:\n{self.content}'
        else:
            description = self.content
    else:
        json_errors = error_details_ta.dump_json(self.content, exclude={'__all__': {'ctx'}}, indent=2)
        plural = isinstance(self.content, list) and len(self.content) != 1
        description = (
            f'{len(self.content)} validation error{"s" if plural else ""}:\n```json\n{json_errors.decode()}\n```'
        )
    return f'{description}\n\nFix the errors and try again.'

```

---|---
###  ModelRequestPart `module-attribute`
```
ModelRequestPart = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    SystemPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart "SystemPromptPart



      dataclass
   \(pydantic_ai.messages.SystemPromptPart\)")
    | UserPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart "UserPromptPart



      dataclass
   \(pydantic_ai.messages.UserPromptPart\)")
    | ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "ToolReturnPart



      dataclass
   \(pydantic_ai.messages.ToolReturnPart\)")
    | RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "RetryPromptPart



      dataclass
   \(pydantic_ai.messages.RetryPromptPart\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_kind"),
]

```

A message part sent by Pydantic AI to a model.
###  ModelRequest `dataclass`
A request generated by Pydantic AI and sent to a model, e.g. a message from the Pydantic AI app to the model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
```
| ```
@dataclass(repr=False)
class ModelRequest:
    """A request generated by Pydantic AI and sent to a model, e.g. a message from the Pydantic AI app to the model."""

    parts: Sequence[ModelRequestPart]
    """The parts of the user message."""

    _: KW_ONLY

    # Default is None for backwards compatibility with old serialized messages that don't have this field.
    # Using a default_factory would incorrectly fill in the current time for deserialized historical messages.
    timestamp: datetime | None = None
    """The timestamp when the request was sent to the model."""

    instructions: str | None = None
    """The instructions for the model."""

    kind: Literal['request'] = 'request'
    """Message type identifier, this is available on all parts as a discriminator."""

    run_id: str | None = None
    """The unique identifier of the agent run in which this message originated."""

    metadata: dict[str, Any] | None = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    @classmethod
    def user_text_prompt(cls, user_prompt: str, *, instructions: str | None = None) -> ModelRequest:
        """Create a `ModelRequest` with a single user prompt as text."""
        return cls(parts=[UserPromptPart(user_prompt)], instructions=instructions)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  parts `instance-attribute`
```
parts: Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[ModelRequestPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart "ModelRequestPart



      module-attribute
   \(pydantic_ai.messages.ModelRequestPart\)")]

```

The parts of the user message.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") | None = None

```

The timestamp when the request was sent to the model.
####  instructions `class-attribute` `instance-attribute`
```
instructions: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The instructions for the model.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['request'] = 'request'

```

Message type identifier, this is available on all parts as a discriminator.
####  run_id `class-attribute` `instance-attribute`
```
run_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The unique identifier of the agent run in which this message originated.
####  metadata `class-attribute` `instance-attribute`
```
metadata: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
####  user_text_prompt `classmethod`
```
user_text_prompt(
    user_prompt: str[](https://docs.python.org/3/library/stdtypes.html#str), *, instructions: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest



      dataclass
   \(pydantic_ai.messages.ModelRequest\)")

```

Create a `ModelRequest` with a single user prompt as text.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1098
1099
1100
1101
```
| ```
@classmethod
def user_text_prompt(cls, user_prompt: str, *, instructions: str | None = None) -> ModelRequest:
    """Create a `ModelRequest` with a single user prompt as text."""
    return cls(parts=[UserPromptPart(user_prompt)], instructions=instructions)

```

---|---
###  TextPart `dataclass`
A plain text response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
```
| ```
@dataclass(repr=False)
class TextPart:
    """A plain text response from a model."""

    content: str
    """The text content of the response."""

    _: KW_ONLY

    id: str | None = None
    """An optional identifier of the text part.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Required to be set when `provider_details` or `id` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_kind: Literal['text'] = 'text'
    """Part type identifier, this is available on all parts as a discriminator."""

    def has_content(self) -> bool:
        """Return `True` if the text content is non-empty."""
        return bool(self.content)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The text content of the response.
####  id `class-attribute` `instance-attribute`
```
id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

An optional identifier of the text part.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
Required to be set when `provider_details` or `id` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['text'] = 'text'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the text content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1137
1138
1139
```
| ```
def has_content(self) -> bool:
    """Return `True` if the text content is non-empty."""
    return bool(self.content)

```

---|---
###  ThinkingPart `dataclass`
A thinking response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
```
| ```
@dataclass(repr=False)
class ThinkingPart:
    """A thinking response from a model."""

    content: str
    """The thinking content of the response."""

    _: KW_ONLY

    id: str | None = None
    """The identifier of the thinking part.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    signature: str | None = None
    """The signature of the thinking.

    Supported by:

    * Anthropic (corresponds to the `signature` field)
    * Bedrock (corresponds to the `signature` field)
    * Google (corresponds to the `thought_signature` field)
    * OpenAI (corresponds to the `encrypted_content` field)

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Signatures are only sent back to the same provider.
    Required to be set when `provider_details`, `id` or `signature` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_kind: Literal['thinking'] = 'thinking'
    """Part type identifier, this is available on all parts as a discriminator."""

    def has_content(self) -> bool:
        """Return `True` if the thinking content is non-empty."""
        return bool(self.content)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The thinking content of the response.
####  id `class-attribute` `instance-attribute`
```
id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The identifier of the thinking part.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  signature `class-attribute` `instance-attribute`
```
signature: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The signature of the thinking.
Supported by:
  * Anthropic (corresponds to the `signature` field)
  * Bedrock (corresponds to the `signature` field)
  * Google (corresponds to the `thought_signature` field)
  * OpenAI (corresponds to the `encrypted_content` field)


When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
Signatures are only sent back to the same provider. Required to be set when `provider_details`, `id` or `signature` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['thinking'] = 'thinking'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the thinking content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1189
1190
1191
```
| ```
def has_content(self) -> bool:
    """Return `True` if the thinking content is non-empty."""
    return bool(self.content)

```

---|---
###  FilePart `dataclass`
A file response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
```
| ```
@dataclass(repr=False)
class FilePart:
    """A file response from a model."""

    content: Annotated[BinaryContent, pydantic.AfterValidator(BinaryImage.narrow_type)]
    """The file content of the response."""

    _: KW_ONLY

    id: str | None = None
    """The identifier of the file part.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Required to be set when `provider_details` or `id` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_kind: Literal['file'] = 'file'
    """Part type identifier, this is available on all parts as a discriminator."""

    def has_content(self) -> bool:
        """Return `True` if the file content is non-empty."""
        return bool(self.content.data)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"), AfterValidator[](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.AfterValidator "pydantic.AfterValidator")(narrow_type[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.narrow_type "narrow_type



      staticmethod
   \(pydantic_ai.messages.BinaryImage.narrow_type\)"))
]

```

The file content of the response.
####  id `class-attribute` `instance-attribute`
```
id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The identifier of the file part.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
Required to be set when `provider_details` or `id` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['file'] = 'file'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the file content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1227
1228
1229
```
| ```
def has_content(self) -> bool:
    """Return `True` if the file content is non-empty."""
    return bool(self.content.data)

```

---|---
###  BaseToolCallPart `dataclass`
A tool call from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
```
| ```
@dataclass(repr=False)
class BaseToolCallPart:
    """A tool call from a model."""

    tool_name: str
    """The name of the tool to call."""

    args: str | dict[str, Any] | None = None
    """The arguments to pass to the tool.

    This is stored either as a JSON string or a Python dictionary depending on how data was received.
    """

    tool_call_id: str = field(default_factory=_generate_tool_call_id)
    """The tool call identifier, this is used by some models including OpenAI.

    In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
    """

    _: KW_ONLY

    id: str | None = None
    """An optional identifier of the tool call part, separate from the tool call ID.

    This is used by some APIs like OpenAI Responses.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Builtin tool calls are only sent back to the same provider.
    Required to be set when `provider_details` or `id` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    def args_as_dict(self) -> dict[str, Any]:
        """Return the arguments as a Python dictionary.

        This is just for convenience with models that require dicts as input.
        """
        if not self.args:
            return {}
        if isinstance(self.args, dict):
            return self.args
        args = pydantic_core.from_json(self.args)
        assert isinstance(args, dict), 'args should be a dict'
        return cast(dict[str, Any], args)

    def args_as_json_str(self) -> str:
        """Return the arguments as a JSON string.

        This is just for convenience with models that require JSON strings as input.
        """
        if not self.args:
            return '{}'
        if isinstance(self.args, str):
            return self.args
        return pydantic_core.to_json(self.args).decode()

    def has_content(self) -> bool:
        """Return `True` if the arguments contain any data."""
        if isinstance(self.args, dict):
            # TODO: This should probably return True if you have the value False, or 0, etc.
            #   It makes sense to me to ignore empty strings, but not sure about empty lists or dicts
            return any(self.args.values())
        else:
            return bool(self.args)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The name of the tool to call.
####  args `class-attribute` `instance-attribute`
```
args: str[](https://docs.python.org/3/library/stdtypes.html#str) | dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

The arguments to pass to the tool.
This is stored either as a JSON string or a Python dictionary depending on how data was received.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(
    default_factory=generate_tool_call_id
)

```

The tool call identifier, this is used by some models including OpenAI.
In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
####  id `class-attribute` `instance-attribute`
```
id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

An optional identifier of the tool call part, separate from the tool call ID.
This is used by some APIs like OpenAI Responses. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
Builtin tool calls are only sent back to the same provider. Required to be set when `provider_details` or `id` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  args_as_dict
```
args_as_dict() -> dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

Return the arguments as a Python dictionary.
This is just for convenience with models that require dicts as input.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
```
| ```
def args_as_dict(self) -> dict[str, Any]:
    """Return the arguments as a Python dictionary.

    This is just for convenience with models that require dicts as input.
    """
    if not self.args:
        return {}
    if isinstance(self.args, dict):
        return self.args
    args = pydantic_core.from_json(self.args)
    assert isinstance(args, dict), 'args should be a dict'
    return cast(dict[str, Any], args)

```

---|---
####  args_as_json_str
```
args_as_json_str() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return the arguments as a JSON string.
This is just for convenience with models that require JSON strings as input.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
```
| ```
def args_as_json_str(self) -> str:
    """Return the arguments as a JSON string.

    This is just for convenience with models that require JSON strings as input.
    """
    if not self.args:
        return '{}'
    if isinstance(self.args, str):
        return self.args
    return pydantic_core.to_json(self.args).decode()

```

---|---
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the arguments contain any data.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1300
1301
1302
1303
1304
1305
1306
1307
```
| ```
def has_content(self) -> bool:
    """Return `True` if the arguments contain any data."""
    if isinstance(self.args, dict):
        # TODO: This should probably return True if you have the value False, or 0, etc.
        #   It makes sense to me to ignore empty strings, but not sure about empty lists or dicts
        return any(self.args.values())
    else:
        return bool(self.args)

```

---|---
###  ToolCallPart `dataclass`
Bases: `BaseToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart "BaseToolCallPart



      dataclass
   \(pydantic_ai.messages.BaseToolCallPart\)")`
A tool call from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1312
1313
1314
1315
1316
1317
1318
1319
```
| ```
@dataclass(repr=False)
class ToolCallPart(BaseToolCallPart):
    """A tool call from a model."""

    _: KW_ONLY

    part_kind: Literal['tool-call'] = 'tool-call'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['tool-call'] = 'tool-call'

```

Part type identifier, this is available on all parts as a discriminator.
###  BuiltinToolCallPart `dataclass`
Bases: `BaseToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart "BaseToolCallPart



      dataclass
   \(pydantic_ai.messages.BaseToolCallPart\)")`
A tool call to a built-in tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1322
1323
1324
1325
1326
1327
1328
1329
```
| ```
@dataclass(repr=False)
class BuiltinToolCallPart(BaseToolCallPart):
    """A tool call to a built-in tool."""

    _: KW_ONLY

    part_kind: Literal['builtin-tool-call'] = 'builtin-tool-call'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["builtin-tool-call"] = (
    "builtin-tool-call"
)

```

Part type identifier, this is available on all parts as a discriminator.
###  ModelResponsePart `module-attribute`
```
ModelResponsePart = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")
    | ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")
    | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")
    | BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")
    | ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)")
    | FilePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart "FilePart



      dataclass
   \(pydantic_ai.messages.FilePart\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_kind"),
]

```

A message part returned by a model.
###  ModelResponse `dataclass`
A response from a model, e.g. a message from the model to the Pydantic AI app.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
```
| ```
@dataclass(repr=False)
class ModelResponse:
    """A response from a model, e.g. a message from the model to the Pydantic AI app."""

    parts: Sequence[ModelResponsePart]
    """The parts of the model message."""

    _: KW_ONLY

    usage: RequestUsage = field(default_factory=RequestUsage)
    """Usage information for the request.

    This has a default to make tests easier, and to support loading old messages where usage will be missing.
    """

    model_name: str | None = None
    """The name of the model that generated the response."""

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp when the response was received locally.

    This is always a high-precision local datetime. Provider-specific timestamps
    (if available) are stored in `provider_details['timestamp']`.
    """

    kind: Literal['response'] = 'response'
    """Message type identifier, this is available on all parts as a discriminator."""

    provider_name: str | None = None
    """The name of the LLM provider that generated the response."""

    provider_url: str | None = None
    """The base URL of the LLM provider that generated the response."""

    provider_details: Annotated[
        dict[str, Any] | None,
        # `vendor_details` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        pydantic.Field(validation_alias=pydantic.AliasChoices('provider_details', 'vendor_details')),
    ] = None
    """Additional data returned by the provider that can't be mapped to standard fields."""

    provider_response_id: Annotated[
        str | None,
        # `vendor_id` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        pydantic.Field(validation_alias=pydantic.AliasChoices('provider_response_id', 'vendor_id')),
    ] = None
    """request ID as specified by the model provider. This can be used to track the specific request to the model."""

    finish_reason: FinishReason | None = None
    """Reason the model finished generating the response, normalized to OpenTelemetry values."""

    run_id: str | None = None
    """The unique identifier of the agent run in which this message originated."""

    metadata: dict[str, Any] | None = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    @property
    def text(self) -> str | None:
        """Get the text in the response."""
        texts: list[str] = []
        last_part: ModelResponsePart | None = None
        for part in self.parts:
            if isinstance(part, TextPart):
                # Adjacent text parts should be joined together, but if there are parts in between
                # (like built-in tool calls) they should have newlines between them
                if isinstance(last_part, TextPart):
                    texts[-1] += part.content
                else:
                    texts.append(part.content)
            last_part = part
        if not texts:
            return None

        return '\n\n'.join(texts)

    @property
    def thinking(self) -> str | None:
        """Get the thinking in the response."""
        thinking_parts = [part.content for part in self.parts if isinstance(part, ThinkingPart)]
        if not thinking_parts:
            return None
        return '\n\n'.join(thinking_parts)

    @property
    def files(self) -> list[BinaryContent]:
        """Get the files in the response."""
        return [part.content for part in self.parts if isinstance(part, FilePart)]

    @property
    def images(self) -> list[BinaryImage]:
        """Get the images in the response."""
        return [file for file in self.files if isinstance(file, BinaryImage)]

    @property
    def tool_calls(self) -> list[ToolCallPart]:
        """Get the tool calls in the response."""
        return [part for part in self.parts if isinstance(part, ToolCallPart)]

    @property
    def builtin_tool_calls(self) -> list[tuple[BuiltinToolCallPart, BuiltinToolReturnPart]]:
        """Get the builtin tool calls and results in the response."""
        calls = [part for part in self.parts if isinstance(part, BuiltinToolCallPart)]
        if not calls:
            return []
        returns_by_id = {part.tool_call_id: part for part in self.parts if isinstance(part, BuiltinToolReturnPart)}
        return [
            (call_part, returns_by_id[call_part.tool_call_id])
            for call_part in calls
            if call_part.tool_call_id in returns_by_id
        ]

    @deprecated('`price` is deprecated, use `cost` instead')
    def price(self) -> genai_types.PriceCalculation:  # pragma: no cover
        return self.cost()

    def cost(self) -> genai_types.PriceCalculation:
        """Calculate the cost of the usage.

        Uses [`genai-prices`](https://github.com/pydantic/genai-prices).
        """
        assert self.model_name, 'Model name is required to calculate price'
        # Try matching on provider_api_url first as this is more specific, then fall back to provider_id.
        if self.provider_url:
            try:
                return calc_price(
                    self.usage,
                    self.model_name,
                    provider_api_url=self.provider_url,
                    genai_request_timestamp=self.timestamp,
                )
            except LookupError:
                pass
        return calc_price(
            self.usage,
            self.model_name,
            provider_id=self.provider_name,
            genai_request_timestamp=self.timestamp,
        )

    def otel_events(self, settings: InstrumentationSettings) -> list[LogRecord]:
        """Return OpenTelemetry events for the response."""
        result: list[LogRecord] = []

        def new_event_body():
            new_body: dict[str, Any] = {'role': 'assistant'}
            ev = LogRecord(attributes={'event.name': 'gen_ai.assistant.message'}, body=new_body)
            result.append(ev)
            return new_body

        body = new_event_body()
        for part in self.parts:
            if isinstance(part, ToolCallPart):
                body.setdefault('tool_calls', []).append(
                    {
                        'id': part.tool_call_id,
                        'type': 'function',
                        'function': {
                            'name': part.tool_name,
                            **({'arguments': part.args} if settings.include_content else {}),
                        },
                    }
                )
            elif isinstance(part, TextPart | ThinkingPart):
                kind = part.part_kind
                body.setdefault('content', []).append(
                    {'kind': kind, **({'text': part.content} if settings.include_content else {})}
                )
            elif isinstance(part, FilePart):
                body.setdefault('content', []).append(
                    {
                        'kind': 'binary',
                        'media_type': part.content.media_type,
                        **(
                            {'binary_content': part.content.base64}
                            if settings.include_content and settings.include_binary_content
                            else {}
                        ),
                    }
                )

        if content := body.get('content'):
            text_content = content[0].get('text')
            if content == [{'kind': 'text', 'text': text_content}]:
                body['content'] = text_content

        return result

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        parts: list[_otel_messages.MessagePart] = []
        for part in self.parts:
            if isinstance(part, TextPart):
                parts.append(
                    _otel_messages.TextPart(
                        type='text',
                        **({'content': part.content} if settings.include_content else {}),
                    )
                )
            elif isinstance(part, ThinkingPart):
                parts.append(
                    _otel_messages.ThinkingPart(
                        type='thinking',
                        **({'content': part.content} if settings.include_content else {}),
                    )
                )
            elif isinstance(part, FilePart):
                parts.append(
                    _convert_binary_to_otel_part(part.content.media_type, lambda p=part: p.content.base64, settings)
                )
            elif isinstance(part, BaseToolCallPart):
                call_part = _otel_messages.ToolCallPart(type='tool_call', id=part.tool_call_id, name=part.tool_name)
                if isinstance(part, BuiltinToolCallPart):
                    call_part['builtin'] = True
                if settings.include_content and part.args is not None:
                    from .models.instrumented import InstrumentedModel

                    if isinstance(part.args, str):
                        call_part['arguments'] = part.args
                    else:
                        call_part['arguments'] = {k: InstrumentedModel.serialize_any(v) for k, v in part.args.items()}

                parts.append(call_part)
            elif isinstance(part, BuiltinToolReturnPart):
                return_part = _otel_messages.ToolCallResponsePart(
                    type='tool_call_response',
                    id=part.tool_call_id,
                    name=part.tool_name,
                    builtin=True,
                )
                if settings.include_content and part.content is not None:  # pragma: no branch
                    from .models.instrumented import InstrumentedModel

                    return_part['result'] = InstrumentedModel.serialize_any(part.content)

                parts.append(return_part)
        return parts

    @property
    @deprecated('`vendor_details` is deprecated, use `provider_details` instead')
    def vendor_details(self) -> dict[str, Any] | None:
        return self.provider_details

    @property
    @deprecated('`vendor_id` is deprecated, use `provider_response_id` instead')
    def vendor_id(self) -> str | None:
        return self.provider_response_id

    @property
    @deprecated('`provider_request_id` is deprecated, use `provider_response_id` instead')
    def provider_request_id(self) -> str | None:
        return self.provider_response_id

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  parts `instance-attribute`
```
parts: Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")]

```

The parts of the model message.
####  usage `class-attribute` `instance-attribute`
```
usage: RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)"))

```

Usage information for the request.
This has a default to make tests easier, and to support loading old messages where usage will be missing.
####  model_name `class-attribute` `instance-attribute`
```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the model that generated the response.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp when the response was received locally.
This is always a high-precision local datetime. Provider-specific timestamps (if available) are stored in `provider_details['timestamp']`.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['response'] = 'response'

```

Message type identifier, this is available on all parts as a discriminator.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the LLM provider that generated the response.
####  provider_url `class-attribute` `instance-attribute`
```
provider_url: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The base URL of the LLM provider that generated the response.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None,
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(
        validation_alias=AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices "pydantic.AliasChoices")(
            provider_details[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_details "provider_details



      class-attribute
      instance-attribute
   \(pydantic_ai.messages.ModelResponse.provider_details\)"), vendor_details
        )
    ),
] = None

```

Additional data returned by the provider that can't be mapped to standard fields.
####  provider_response_id `class-attribute` `instance-attribute`
```
provider_response_id: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    str[](https://docs.python.org/3/library/stdtypes.html#str) | None,
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(
        validation_alias=AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices "pydantic.AliasChoices")(
            provider_response_id[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_response_id "provider_response_id



      class-attribute
      instance-attribute
   \(pydantic_ai.messages.ModelResponse.provider_response_id\)"), vendor_id
        )
    ),
] = None

```

request ID as specified by the model provider. This can be used to track the specific request to the model.
####  finish_reason `class-attribute` `instance-attribute`
```
finish_reason: FinishReason[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinishReason "FinishReason



      module-attribute
   \(pydantic_ai.messages.FinishReason\)") | None = None

```

Reason the model finished generating the response, normalized to OpenTelemetry values.
####  run_id `class-attribute` `instance-attribute`
```
run_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The unique identifier of the agent run in which this message originated.
####  metadata `class-attribute` `instance-attribute`
```
metadata: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
####  text `property`
```
text: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

Get the text in the response.
####  thinking `property`
```
thinking: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

Get the thinking in the response.
####  files `property`
```
files: list[](https://docs.python.org/3/library/stdtypes.html#list)[BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]

```

Get the files in the response.
####  images `property`
```
images: list[](https://docs.python.org/3/library/stdtypes.html#list)[BinaryImage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage \(pydantic_ai.messages.BinaryImage\)")]

```

Get the images in the response.
####  tool_calls `property`
```
tool_calls: list[](https://docs.python.org/3/library/stdtypes.html#list)[ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")]

```

Get the tool calls in the response.
####  builtin_tool_calls `property`
```
builtin_tool_calls: list[](https://docs.python.org/3/library/stdtypes.html#list)[
    tuple[](https://docs.python.org/3/library/stdtypes.html#tuple)[BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)"), BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")]
]

```

Get the builtin tool calls and results in the response.
####  price `deprecated`
```
price() -> PriceCalculation

```

Deprecated
`price` is deprecated, use `cost` instead
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1451
1452
1453
```
| ```
@deprecated('`price` is deprecated, use `cost` instead')
def price(self) -> genai_types.PriceCalculation:  # pragma: no cover
    return self.cost()

```

---|---
####  cost
```
cost() -> PriceCalculation

```

Calculate the cost of the usage.
Uses [`genai-prices`](https://github.com/pydantic/genai-prices).
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
```
| ```
def cost(self) -> genai_types.PriceCalculation:
    """Calculate the cost of the usage.

    Uses [`genai-prices`](https://github.com/pydantic/genai-prices).
    """
    assert self.model_name, 'Model name is required to calculate price'
    # Try matching on provider_api_url first as this is more specific, then fall back to provider_id.
    if self.provider_url:
        try:
            return calc_price(
                self.usage,
                self.model_name,
                provider_api_url=self.provider_url,
                genai_request_timestamp=self.timestamp,
            )
        except LookupError:
            pass
    return calc_price(
        self.usage,
        self.model_name,
        provider_id=self.provider_name,
        genai_request_timestamp=self.timestamp,
    )

```

---|---
####  otel_events
```
otel_events(
    settings: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)"),
) -> list[](https://docs.python.org/3/library/stdtypes.html#list)[LogRecord]

```

Return OpenTelemetry events for the response.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
```
| ```
def otel_events(self, settings: InstrumentationSettings) -> list[LogRecord]:
    """Return OpenTelemetry events for the response."""
    result: list[LogRecord] = []

    def new_event_body():
        new_body: dict[str, Any] = {'role': 'assistant'}
        ev = LogRecord(attributes={'event.name': 'gen_ai.assistant.message'}, body=new_body)
        result.append(ev)
        return new_body

    body = new_event_body()
    for part in self.parts:
        if isinstance(part, ToolCallPart):
            body.setdefault('tool_calls', []).append(
                {
                    'id': part.tool_call_id,
                    'type': 'function',
                    'function': {
                        'name': part.tool_name,
                        **({'arguments': part.args} if settings.include_content else {}),
                    },
                }
            )
        elif isinstance(part, TextPart | ThinkingPart):
            kind = part.part_kind
            body.setdefault('content', []).append(
                {'kind': kind, **({'text': part.content} if settings.include_content else {})}
            )
        elif isinstance(part, FilePart):
            body.setdefault('content', []).append(
                {
                    'kind': 'binary',
                    'media_type': part.content.media_type,
                    **(
                        {'binary_content': part.content.base64}
                        if settings.include_content and settings.include_binary_content
                        else {}
                    ),
                }
            )

    if content := body.get('content'):
        text_content = content[0].get('text')
        if content == [{'kind': 'text', 'text': text_content}]:
            body['content'] = text_content

    return result

```

---|---
###  ModelMessage `module-attribute`
```
ModelMessage = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest



      dataclass
   \(pydantic_ai.messages.ModelRequest\)") | ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("kind")
]

```

Any message sent to or returned by a model.
###  ModelMessagesTypeAdapter `module-attribute`
```
ModelMessagesTypeAdapter = TypeAdapter[](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter "pydantic.TypeAdapter")(
    list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    config=ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict "pydantic.ConfigDict")(
        defer_build=True,
        ser_json_bytes="base64",
        val_json_bytes="base64",
    ),
)

```

Pydantic [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) for (de)serializing messages.
###  TextPartDelta `dataclass`
A partial update (delta) for a `TextPart` to append new text content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
```
| ```
@dataclass(repr=False)
class TextPartDelta:
    """A partial update (delta) for a `TextPart` to append new text content."""

    content_delta: str
    """The incremental text content to add to the existing `TextPart` content."""

    _: KW_ONLY

    provider_name: str | None = None
    """The name of the provider that generated the response.

    This is required to be set when `provider_details` is set and the initial TextPart does not have a `provider_name` or it has changed.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_delta_kind: Literal['text'] = 'text'
    """Part delta type identifier, used as a discriminator."""

    def apply(self, part: ModelResponsePart) -> TextPart:
        """Apply this text delta to an existing `TextPart`.

        Args:
            part: The existing model response part, which must be a `TextPart`.

        Returns:
            A new `TextPart` with updated text content.

        Raises:
            ValueError: If `part` is not a `TextPart`.
        """
        if not isinstance(part, TextPart):
            raise ValueError('Cannot apply TextPartDeltas to non-TextParts')  # pragma: no cover
        return replace(
            part,
            content=part.content + self.content_delta,
            provider_name=self.provider_name or part.provider_name,
            provider_details={**(part.provider_details or {}), **(self.provider_details or {})} or None,
        )

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content_delta `instance-attribute`
```
content_delta: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The incremental text content to add to the existing `TextPart` content.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
This is required to be set when `provider_details` is set and the initial TextPart does not have a `provider_name` or it has changed.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['text'] = 'text'

```

Part delta type identifier, used as a discriminator.
####  apply
```
apply(part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")) -> TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")

```

Apply this text delta to an existing `TextPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")` |  The existing model response part, which must be a `TextPart`. |  _required_
Returns:
Type | Description
---|---
`TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")` |  A new `TextPart` with updated text content.
Raises:
Type | Description
---|---
`ValueError[](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `part` is not a `TextPart`.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
```
| ```
def apply(self, part: ModelResponsePart) -> TextPart:
    """Apply this text delta to an existing `TextPart`.

    Args:
        part: The existing model response part, which must be a `TextPart`.

    Returns:
        A new `TextPart` with updated text content.

    Raises:
        ValueError: If `part` is not a `TextPart`.
    """
    if not isinstance(part, TextPart):
        raise ValueError('Cannot apply TextPartDeltas to non-TextParts')  # pragma: no cover
    return replace(
        part,
        content=part.content + self.content_delta,
        provider_name=self.provider_name or part.provider_name,
        provider_details={**(part.provider_details or {}), **(self.provider_details or {})} or None,
    )

```

---|---
###  ThinkingPartDelta `dataclass`
A partial update (delta) for a `ThinkingPart` to append new thinking content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
```
| ```
@dataclass(repr=False, kw_only=True)
class ThinkingPartDelta:
    """A partial update (delta) for a `ThinkingPart` to append new thinking content."""

    content_delta: str | None = None
    """The incremental thinking content to add to the existing `ThinkingPart` content."""

    signature_delta: str | None = None
    """Optional signature delta.

    Note this is never treated as a delta — it can replace None.
    """

    provider_name: str | None = None
    """Optional provider name for the thinking part.

    Signatures are only sent back to the same provider.
    Required to be set when `provider_details` is set and the initial ThinkingPart does not have a `provider_name` or it has changed.
    """

    provider_details: ProviderDetailsDelta = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    Can be a dict to merge with existing details, or a callable that takes
    the existing details and returns updated details.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.

    When this field is set, `provider_name` is required to identify the provider that generated this data."""

    part_delta_kind: Literal['thinking'] = 'thinking'
    """Part delta type identifier, used as a discriminator."""

    @overload
    def apply(self, part: ModelResponsePart) -> ThinkingPart: ...

    @overload
    def apply(self, part: ModelResponsePart | ThinkingPartDelta) -> ThinkingPart | ThinkingPartDelta: ...

    def apply(self, part: ModelResponsePart | ThinkingPartDelta) -> ThinkingPart | ThinkingPartDelta:
        """Apply this thinking delta to an existing `ThinkingPart`.

        Args:
            part: The existing model response part, which must be a `ThinkingPart`.

        Returns:
            A new `ThinkingPart` with updated thinking content.

        Raises:
            ValueError: If `part` is not a `ThinkingPart`.
        """
        if isinstance(part, ThinkingPart):
            new_content = part.content + self.content_delta if self.content_delta else part.content
            new_signature = self.signature_delta if self.signature_delta is not None else part.signature
            new_provider_name = self.provider_name if self.provider_name is not None else part.provider_name
            # Resolve callable provider_details if needed
            resolved_details = (
                self.provider_details(part.provider_details)
                if callable(self.provider_details)
                else self.provider_details
            )
            new_provider_details = {**(part.provider_details or {}), **(resolved_details or {})} or None
            return replace(
                part,
                content=new_content,
                signature=new_signature,
                provider_name=new_provider_name,
                provider_details=new_provider_details,
            )
        elif isinstance(part, ThinkingPartDelta):
            if self.content_delta is None and self.signature_delta is None:
                raise ValueError('Cannot apply ThinkingPartDelta with no content or signature')
            if self.content_delta is not None:
                part = replace(part, content_delta=(part.content_delta or '') + self.content_delta)
            if self.signature_delta is not None:
                part = replace(part, signature_delta=self.signature_delta)
            if self.provider_name is not None:
                part = replace(part, provider_name=self.provider_name)
            if self.provider_details is not None:
                if callable(self.provider_details):
                    if callable(part.provider_details):
                        existing_fn = part.provider_details
                        new_fn = self.provider_details

                        def chained_both(d: dict[str, Any] | None) -> dict[str, Any]:
                            return new_fn(existing_fn(d))

                        part = replace(part, provider_details=chained_both)
                    else:
                        part = replace(part, provider_details=self.provider_details)  # pragma: no cover
                elif callable(part.provider_details):
                    existing_fn = part.provider_details
                    new_dict = self.provider_details

                    def chained_dict(d: dict[str, Any] | None) -> dict[str, Any]:
                        return {**existing_fn(d), **new_dict}

                    part = replace(part, provider_details=chained_dict)
                else:
                    existing = part.provider_details if isinstance(part.provider_details, dict) else {}
                    part = replace(part, provider_details={**existing, **self.provider_details})
            return part
        raise ValueError(  # pragma: no cover
            f'Cannot apply ThinkingPartDeltas to non-ThinkingParts or non-ThinkingPartDeltas ({part=}, {self=})'
        )

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content_delta `class-attribute` `instance-attribute`
```
content_delta: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The incremental thinking content to add to the existing `ThinkingPart` content.
####  signature_delta `class-attribute` `instance-attribute`
```
signature_delta: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional signature delta.
Note this is never treated as a delta — it can replace None.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional provider name for the thinking part.
Signatures are only sent back to the same provider. Required to be set when `provider_details` is set and the initial ThinkingPart does not have a `provider_name` or it has changed.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: ProviderDetailsDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ProviderDetailsDelta "ProviderDetailsDelta



      module-attribute
   \(pydantic_ai.messages.ProviderDetailsDelta\)") = None

```

Additional data returned by the provider that can't be mapped to standard fields.
Can be a dict to merge with existing details, or a callable that takes the existing details and returns updated details.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['thinking'] = 'thinking'

```

Part delta type identifier, used as a discriminator.
####  apply
```
apply(part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")) -> ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)"),
) -> ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)"),
) -> ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")

```

Apply this thinking delta to an existing `ThinkingPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")` |  The existing model response part, which must be a `ThinkingPart`. |  _required_
Returns:
Type | Description
---|---
`ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")` |  A new `ThinkingPart` with updated thinking content.
Raises:
Type | Description
---|---
`ValueError[](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `part` is not a `ThinkingPart`.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
```
| ```
def apply(self, part: ModelResponsePart | ThinkingPartDelta) -> ThinkingPart | ThinkingPartDelta:
    """Apply this thinking delta to an existing `ThinkingPart`.

    Args:
        part: The existing model response part, which must be a `ThinkingPart`.

    Returns:
        A new `ThinkingPart` with updated thinking content.

    Raises:
        ValueError: If `part` is not a `ThinkingPart`.
    """
    if isinstance(part, ThinkingPart):
        new_content = part.content + self.content_delta if self.content_delta else part.content
        new_signature = self.signature_delta if self.signature_delta is not None else part.signature
        new_provider_name = self.provider_name if self.provider_name is not None else part.provider_name
        # Resolve callable provider_details if needed
        resolved_details = (
            self.provider_details(part.provider_details)
            if callable(self.provider_details)
            else self.provider_details
        )
        new_provider_details = {**(part.provider_details or {}), **(resolved_details or {})} or None
        return replace(
            part,
            content=new_content,
            signature=new_signature,
            provider_name=new_provider_name,
            provider_details=new_provider_details,
        )
    elif isinstance(part, ThinkingPartDelta):
        if self.content_delta is None and self.signature_delta is None:
            raise ValueError('Cannot apply ThinkingPartDelta with no content or signature')
        if self.content_delta is not None:
            part = replace(part, content_delta=(part.content_delta or '') + self.content_delta)
        if self.signature_delta is not None:
            part = replace(part, signature_delta=self.signature_delta)
        if self.provider_name is not None:
            part = replace(part, provider_name=self.provider_name)
        if self.provider_details is not None:
            if callable(self.provider_details):
                if callable(part.provider_details):
                    existing_fn = part.provider_details
                    new_fn = self.provider_details

                    def chained_both(d: dict[str, Any] | None) -> dict[str, Any]:
                        return new_fn(existing_fn(d))

                    part = replace(part, provider_details=chained_both)
                else:
                    part = replace(part, provider_details=self.provider_details)  # pragma: no cover
            elif callable(part.provider_details):
                existing_fn = part.provider_details
                new_dict = self.provider_details

                def chained_dict(d: dict[str, Any] | None) -> dict[str, Any]:
                    return {**existing_fn(d), **new_dict}

                part = replace(part, provider_details=chained_dict)
            else:
                existing = part.provider_details if isinstance(part.provider_details, dict) else {}
                part = replace(part, provider_details={**existing, **self.provider_details})
        return part
    raise ValueError(  # pragma: no cover
        f'Cannot apply ThinkingPartDeltas to non-ThinkingParts or non-ThinkingPartDeltas ({part=}, {self=})'
    )

```

---|---
###  ToolCallPartDelta `dataclass`
A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
1868
1869
1870
1871
1872
1873
1874
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
```
| ```
@dataclass(repr=False, kw_only=True)
class ToolCallPartDelta:
    """A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID."""

    tool_name_delta: str | None = None
    """Incremental text to add to the existing tool name, if any."""

    args_delta: str | dict[str, Any] | None = None
    """Incremental data to add to the tool arguments.

    If this is a string, it will be appended to existing JSON arguments.
    If this is a dict, it will be merged with existing dict arguments.
    """

    tool_call_id: str | None = None
    """Optional tool call identifier, this is used by some models including OpenAI.

    Note this is never treated as a delta — it can replace None, but otherwise if a
    non-matching value is provided an error will be raised."""

    provider_name: str | None = None
    """The name of the provider that generated the response.

    This is required to be set when `provider_details` is set and the initial ToolCallPart does not have a `provider_name` or it has changed.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_delta_kind: Literal['tool_call'] = 'tool_call'
    """Part delta type identifier, used as a discriminator."""

    def as_part(self) -> ToolCallPart | None:
        """Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.

        Returns:
            A `ToolCallPart` if `tool_name_delta` is set, otherwise `None`.
        """
        if self.tool_name_delta is None:
            return None

        return ToolCallPart(
            self.tool_name_delta,
            self.args_delta,
            self.tool_call_id or _generate_tool_call_id(),
            provider_name=self.provider_name,
            provider_details=self.provider_details,
        )

    @overload
    def apply(self, part: ModelResponsePart) -> ToolCallPart | BuiltinToolCallPart: ...

    @overload
    def apply(
        self, part: ModelResponsePart | ToolCallPartDelta
    ) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta: ...

    def apply(
        self, part: ModelResponsePart | ToolCallPartDelta
    ) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta:
        """Apply this delta to a part or delta, returning a new part or delta with the changes applied.

        Args:
            part: The existing model response part or delta to update.

        Returns:
            Either a new `ToolCallPart` or `BuiltinToolCallPart`, or an updated `ToolCallPartDelta`.

        Raises:
            ValueError: If `part` is neither a `ToolCallPart`, `BuiltinToolCallPart`, nor a `ToolCallPartDelta`.
            UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.
        """
        if isinstance(part, ToolCallPart | BuiltinToolCallPart):
            return self._apply_to_part(part)

        if isinstance(part, ToolCallPartDelta):
            return self._apply_to_delta(part)

        raise ValueError(  # pragma: no cover
            f'Can only apply ToolCallPartDeltas to ToolCallParts, BuiltinToolCallParts, or ToolCallPartDeltas, not {part}'
        )

    def _apply_to_delta(self, delta: ToolCallPartDelta) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta:
        """Internal helper to apply this delta to another delta."""
        if self.tool_name_delta:
            # Append incremental text to the existing tool_name_delta
            updated_tool_name_delta = (delta.tool_name_delta or '') + self.tool_name_delta
            delta = replace(delta, tool_name_delta=updated_tool_name_delta)

        if isinstance(self.args_delta, str):
            if isinstance(delta.args_delta, dict):
                raise UnexpectedModelBehavior(
                    f'Cannot apply JSON deltas to non-JSON tool arguments ({delta=}, {self=})'
                )
            updated_args_delta = (delta.args_delta or '') + self.args_delta
            delta = replace(delta, args_delta=updated_args_delta)
        elif isinstance(self.args_delta, dict):
            if isinstance(delta.args_delta, str):
                raise UnexpectedModelBehavior(
                    f'Cannot apply dict deltas to non-dict tool arguments ({delta=}, {self=})'
                )
            updated_args_delta = {**(delta.args_delta or {}), **self.args_delta}
            delta = replace(delta, args_delta=updated_args_delta)

        if self.tool_call_id:
            delta = replace(delta, tool_call_id=self.tool_call_id)

        if self.provider_name:
            delta = replace(delta, provider_name=self.provider_name)

        if self.provider_details:
            merged_provider_details = {**(delta.provider_details or {}), **self.provider_details}
            delta = replace(delta, provider_details=merged_provider_details)

        # If we now have enough data to create a full ToolCallPart, do so
        if delta.tool_name_delta is not None:
            return ToolCallPart(
                delta.tool_name_delta,
                delta.args_delta,
                delta.tool_call_id or _generate_tool_call_id(),
                provider_name=delta.provider_name,
                provider_details=delta.provider_details,
            )

        return delta

    def _apply_to_part(self, part: ToolCallPart | BuiltinToolCallPart) -> ToolCallPart | BuiltinToolCallPart:
        """Internal helper to apply this delta directly to a `ToolCallPart` or `BuiltinToolCallPart`."""
        if self.tool_name_delta:
            # Append incremental text to the existing tool_name
            tool_name = part.tool_name + self.tool_name_delta
            part = replace(part, tool_name=tool_name)

        if isinstance(self.args_delta, str):
            if isinstance(part.args, dict):
                raise UnexpectedModelBehavior(f'Cannot apply JSON deltas to non-JSON tool arguments ({part=}, {self=})')
            updated_json = (part.args or '') + self.args_delta
            part = replace(part, args=updated_json)
        elif isinstance(self.args_delta, dict):
            if isinstance(part.args, str):
                raise UnexpectedModelBehavior(f'Cannot apply dict deltas to non-dict tool arguments ({part=}, {self=})')
            updated_dict = {**(part.args or {}), **self.args_delta}
            part = replace(part, args=updated_dict)

        if self.tool_call_id:
            part = replace(part, tool_call_id=self.tool_call_id)

        if self.provider_name:
            part = replace(part, provider_name=self.provider_name)

        if self.provider_details:
            merged_provider_details = {**(part.provider_details or {}), **self.provider_details}
            part = replace(part, provider_details=merged_provider_details)

        return part

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name_delta `class-attribute` `instance-attribute`
```
tool_name_delta: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental text to add to the existing tool name, if any.
####  args_delta `class-attribute` `instance-attribute`
```
args_delta: str[](https://docs.python.org/3/library/stdtypes.html#str) | dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Incremental data to add to the tool arguments.
If this is a string, it will be appended to existing JSON arguments. If this is a dict, it will be merged with existing dict arguments.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional tool call identifier, this is used by some models including OpenAI.
Note this is never treated as a delta — it can replace None, but otherwise if a non-matching value is provided an error will be raised.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the provider that generated the response.
This is required to be set when `provider_details` is set and the initial ToolCallPart does not have a `provider_name` or it has changed.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['tool_call'] = 'tool_call'

```

Part delta type identifier, used as a discriminator.
####  as_part
```
as_part() -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | None

```

Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.
Returns:
Type | Description
---|---
`ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | None` |  A `ToolCallPart` if `tool_name_delta` is set, otherwise `None`.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
```
| ```
def as_part(self) -> ToolCallPart | None:
    """Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.

    Returns:
        A `ToolCallPart` if `tool_name_delta` is set, otherwise `None`.
    """
    if self.tool_name_delta is None:
        return None

    return ToolCallPart(
        self.tool_name_delta,
        self.args_delta,
        self.tool_call_id or _generate_tool_call_id(),
        provider_name=self.provider_name,
        provider_details=self.provider_details,
    )

```

---|---
####  apply
```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")

```

Apply this delta to a part or delta, returning a new part or delta with the changes applied.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")` |  The existing model response part or delta to update. |  _required_
Returns:
Type | Description
---|---
`ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")` |  Either a new `ToolCallPart` or `BuiltinToolCallPart`, or an updated `ToolCallPartDelta`.
Raises:
Type | Description
---|---
`ValueError[](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `part` is neither a `ToolCallPart`, `BuiltinToolCallPart`, nor a `ToolCallPartDelta`.
`UnexpectedModelBehavior[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior "UnexpectedModelBehavior \(pydantic_ai.exceptions.UnexpectedModelBehavior\)")` |  If applying JSON deltas to dict arguments or vice versa.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
```
| ```
def apply(
    self, part: ModelResponsePart | ToolCallPartDelta
) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta:
    """Apply this delta to a part or delta, returning a new part or delta with the changes applied.

    Args:
        part: The existing model response part or delta to update.

    Returns:
        Either a new `ToolCallPart` or `BuiltinToolCallPart`, or an updated `ToolCallPartDelta`.

    Raises:
        ValueError: If `part` is neither a `ToolCallPart`, `BuiltinToolCallPart`, nor a `ToolCallPartDelta`.
        UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.
    """
    if isinstance(part, ToolCallPart | BuiltinToolCallPart):
        return self._apply_to_part(part)

    if isinstance(part, ToolCallPartDelta):
        return self._apply_to_delta(part)

    raise ValueError(  # pragma: no cover
        f'Can only apply ToolCallPartDeltas to ToolCallParts, BuiltinToolCallParts, or ToolCallPartDeltas, not {part}'
    )

```

---|---
###  ModelResponsePartDelta `module-attribute`
```
ModelResponsePartDelta = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    TextPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta "TextPartDelta



      dataclass
   \(pydantic_ai.messages.TextPartDelta\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_delta_kind"),
]

```

A partial update (delta) for any model response part.
###  PartStartEvent `dataclass`
An event indicating that a new part has started.
If multiple `PartStartEvent`s are received with the same index, the new one should fully replace the old one.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
```
| ```
@dataclass(repr=False, kw_only=True)
class PartStartEvent:
    """An event indicating that a new part has started.

    If multiple `PartStartEvent`s are received with the same index,
    the new one should fully replace the old one.
    """

    index: int
    """The index of the part within the overall response parts list."""

    part: ModelResponsePart
    """The newly started `ModelResponsePart`."""

    previous_part_kind: (
        Literal['text', 'thinking', 'tool-call', 'builtin-tool-call', 'builtin-tool-return', 'file'] | None
    ) = None
    """The kind of the previous part, if any.

    This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
    """

    event_kind: Literal['part_start'] = 'part_start'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  index `instance-attribute`
```
index: int[](https://docs.python.org/3/library/functions.html#int)

```

The index of the part within the overall response parts list.
####  part `instance-attribute`
```
part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")

```

The newly started `ModelResponsePart`.
####  previous_part_kind `class-attribute` `instance-attribute`
```
previous_part_kind: (
    Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
        "text",
        "thinking",
        "tool-call",
        "builtin-tool-call",
        "builtin-tool-return",
        "file",
    ]
    | None
) = None

```

The kind of the previous part, if any.
This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['part_start'] = 'part_start'

```

Event type identifier, used as a discriminator.
###  PartDeltaEvent `dataclass`
An event indicating a delta update for an existing part.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
```
| ```
@dataclass(repr=False, kw_only=True)
class PartDeltaEvent:
    """An event indicating a delta update for an existing part."""

    index: int
    """The index of the part within the overall response parts list."""

    delta: ModelResponsePartDelta
    """The delta to apply to the specified part."""

    event_kind: Literal['part_delta'] = 'part_delta'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  index `instance-attribute`
```
index: int[](https://docs.python.org/3/library/functions.html#int)

```

The index of the part within the overall response parts list.
####  delta `instance-attribute`
```
delta: ModelResponsePartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta "ModelResponsePartDelta



      module-attribute
   \(pydantic_ai.messages.ModelResponsePartDelta\)")

```

The delta to apply to the specified part.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['part_delta'] = 'part_delta'

```

Event type identifier, used as a discriminator.
###  PartEndEvent `dataclass`
An event indicating that a part is complete.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
```
| ```
@dataclass(repr=False, kw_only=True)
class PartEndEvent:
    """An event indicating that a part is complete."""

    index: int
    """The index of the part within the overall response parts list."""

    part: ModelResponsePart
    """The complete `ModelResponsePart`."""

    next_part_kind: (
        Literal['text', 'thinking', 'tool-call', 'builtin-tool-call', 'builtin-tool-return', 'file'] | None
    ) = None
    """The kind of the next part, if any.

    This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
    """

    event_kind: Literal['part_end'] = 'part_end'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  index `instance-attribute`
```
index: int[](https://docs.python.org/3/library/functions.html#int)

```

The index of the part within the overall response parts list.
####  part `instance-attribute`
```
part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")

```

The complete `ModelResponsePart`.
####  next_part_kind `class-attribute` `instance-attribute`
```
next_part_kind: (
    Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
        "text",
        "thinking",
        "tool-call",
        "builtin-tool-call",
        "builtin-tool-return",
        "file",
    ]
    | None
) = None

```

The kind of the next part, if any.
This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['part_end'] = 'part_end'

```

Event type identifier, used as a discriminator.
###  FinalResultEvent `dataclass`
An event indicating the response to the current model request matches the output schema and will produce a result.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
```
| ```
@dataclass(repr=False, kw_only=True)
class FinalResultEvent:
    """An event indicating the response to the current model request matches the output schema and will produce a result."""

    tool_name: str | None
    """The name of the output tool that was called. `None` if the result is from text content and not from a tool."""
    tool_call_id: str | None
    """The tool call ID, if any, that this result is associated with."""
    event_kind: Literal['final_result'] = 'final_result'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

The name of the output tool that was called. `None` if the result is from text content and not from a tool.
####  tool_call_id `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

The tool call ID, if any, that this result is associated with.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['final_result'] = 'final_result'

```

Event type identifier, used as a discriminator.
###  ModelResponseStreamEvent `module-attribute`
```
ModelResponseStreamEvent = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    PartStartEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "PartStartEvent



      dataclass
   \(pydantic_ai.messages.PartStartEvent\)")
    | PartDeltaEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "PartDeltaEvent



      dataclass
   \(pydantic_ai.messages.PartDeltaEvent\)")
    | PartEndEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent "PartEndEvent



      dataclass
   \(pydantic_ai.messages.PartEndEvent\)")
    | FinalResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "FinalResultEvent



      dataclass
   \(pydantic_ai.messages.FinalResultEvent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event in the model response stream, starting a new part, applying a delta to an existing one, indicating a part is complete, or indicating the final result.
###  FunctionToolCallEvent `dataclass`
An event indicating the start to a call to a function tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
2030
2031
2032
2033
2034
2035
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
```
| ```
@dataclass(repr=False)
class FunctionToolCallEvent:
    """An event indicating the start to a call to a function tool."""

    part: ToolCallPart
    """The (function) tool call to make."""

    _: KW_ONLY

    args_valid: bool | None = None
    """Whether the tool arguments passed validation.
    See the [custom validation docs](https://ai.pydantic.dev/tools-advanced/#args-validator) for more info.

    - `True`: Schema validation and custom validation (if configured) both passed; args are guaranteed valid.
    - `False`: Validation was performed and failed.
    - `None`: Validation was not performed.
    """

    event_kind: Literal['function_tool_call'] = 'function_tool_call'
    """Event type identifier, used as a discriminator."""

    @property
    def tool_call_id(self) -> str:
        """An ID used for matching details about the call to its result."""
        return self.part.tool_call_id

    @property
    @deprecated('`call_id` is deprecated, use `tool_call_id` instead.')
    def call_id(self) -> str:
        """An ID used for matching details about the call to its result."""
        return self.part.tool_call_id  # pragma: no cover

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  part `instance-attribute`
```
part: ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")

```

The (function) tool call to make.
####  args_valid `class-attribute` `instance-attribute`
```
args_valid: bool[](https://docs.python.org/3/library/functions.html#bool) | None = None

```

Whether the tool arguments passed validation. See the [custom validation docs](https://ai.pydantic.dev/tools-advanced/#args-validator) for more info.
  * `True`: Schema validation and custom validation (if configured) both passed; args are guaranteed valid.
  * `False`: Validation was performed and failed.
  * `None`: Validation was not performed.


####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["function_tool_call"] = (
    "function_tool_call"
)

```

Event type identifier, used as a discriminator.
####  tool_call_id `property`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

An ID used for matching details about the call to its result.
####  call_id `property`
```
call_id: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

An ID used for matching details about the call to its result.
###  FunctionToolResultEvent `dataclass`
An event indicating the result of a function tool call.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
```
| ```
@dataclass(repr=False)
class FunctionToolResultEvent:
    """An event indicating the result of a function tool call."""

    result: ToolReturnPart | RetryPromptPart
    """The result of the call to the function tool."""

    _: KW_ONLY

    content: str | Sequence[UserContent] | None = None
    """The content that will be sent to the model as a UserPromptPart following the result."""

    event_kind: Literal['function_tool_result'] = 'function_tool_result'
    """Event type identifier, used as a discriminator."""

    @property
    def tool_call_id(self) -> str:
        """An ID used to match the result to its original call."""
        return self.result.tool_call_id

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  result `instance-attribute`
```
result: ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "ToolReturnPart



      dataclass
   \(pydantic_ai.messages.ToolReturnPart\)") | RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "RetryPromptPart



      dataclass
   \(pydantic_ai.messages.RetryPromptPart\)")

```

The result of the call to the function tool.
####  content `class-attribute` `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[UserContent] | None = None

```

The content that will be sent to the model as a UserPromptPart following the result.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["function_tool_result"] = (
    "function_tool_result"
)

```

Event type identifier, used as a discriminator.
####  tool_call_id `property`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

An ID used to match the result to its original call.
###  BuiltinToolCallEvent `dataclass` `deprecated`
Deprecated
`BuiltinToolCallEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolCallPart` instead.
An event indicating the start to a call to a built-in tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
```
| ```
@deprecated(
    '`BuiltinToolCallEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolCallPart` instead.'
)
@dataclass(repr=False)
class BuiltinToolCallEvent:
    """An event indicating the start to a call to a built-in tool."""

    part: BuiltinToolCallPart
    """The built-in tool call to make."""

    _: KW_ONLY

    event_kind: Literal['builtin_tool_call'] = 'builtin_tool_call'
    """Event type identifier, used as a discriminator."""

```

---|---
####  part `instance-attribute`
```
part: BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")

```

The built-in tool call to make.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["builtin_tool_call"] = (
    "builtin_tool_call"
)

```

Event type identifier, used as a discriminator.
###  BuiltinToolResultEvent `dataclass` `deprecated`
Deprecated
`BuiltinToolResultEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolReturnPart` instead.
An event indicating the result of a built-in tool call.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
```
| ```
@deprecated(
    '`BuiltinToolResultEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolReturnPart` instead.'
)
@dataclass(repr=False)
class BuiltinToolResultEvent:
    """An event indicating the result of a built-in tool call."""

    result: BuiltinToolReturnPart
    """The result of the call to the built-in tool."""

    _: KW_ONLY

    event_kind: Literal['builtin_tool_result'] = 'builtin_tool_result'
    """Event type identifier, used as a discriminator."""

```

---|---
####  result `instance-attribute`
```
result: BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")

```

The result of the call to the built-in tool.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["builtin_tool_result"] = (
    "builtin_tool_result"
)

```

Event type identifier, used as a discriminator.
###  HandleResponseEvent `module-attribute`
```
HandleResponseEvent = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    FunctionToolCallEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent "FunctionToolCallEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolCallEvent\)")
    | FunctionToolResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent "FunctionToolResultEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolResultEvent\)")
    | BuiltinToolCallEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent "BuiltinToolCallEvent



      dataclass
      deprecated
   \(pydantic_ai.messages.BuiltinToolCallEvent\)")
    | BuiltinToolResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent "BuiltinToolResultEvent



      dataclass
      deprecated
   \(pydantic_ai.messages.BuiltinToolResultEvent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event yielded when handling a model response, indicating tool calls and results.
###  AgentStreamEvent `module-attribute`
```
AgentStreamEvent = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
    ModelResponseStreamEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent "ModelResponseStreamEvent



      module-attribute
   \(pydantic_ai.messages.ModelResponseStreamEvent\)") | HandleResponseEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.HandleResponseEvent "HandleResponseEvent



      module-attribute
   \(pydantic_ai.messages.HandleResponseEvent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event in the agent stream: model response stream events and response-handling events.
© Pydantic Services Inc. 2024 to present
