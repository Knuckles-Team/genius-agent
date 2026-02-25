[ Skip to content ](https://ai.pydantic.dev/api/models/cohere/#pydantic_aimodelscohere)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_ai.models.cohere
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
      * pydantic_ai.models.cohere  [ pydantic_ai.models.cohere  ](https://ai.pydantic.dev/api/models/cohere/)
        * [ Setup  ](https://ai.pydantic.dev/api/models/cohere/#setup)
          * [ cohere  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere)
          * [ LatestCohereModelNames  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.LatestCohereModelNames)
          * [ CohereModelName  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelName)
          * [ CohereModelSettings  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelSettings)
          * [ CohereModel  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel)
            * [ __init__  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel.__init__)
            * [ model_name  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel.model_name)
            * [ system  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel.system)
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


  * [ Setup  ](https://ai.pydantic.dev/api/models/cohere/#setup)
    * [ cohere  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere)
    * [ LatestCohereModelNames  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.LatestCohereModelNames)
    * [ CohereModelName  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelName)
    * [ CohereModelSettings  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelSettings)
    * [ CohereModel  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel)
      * [ __init__  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel.__init__)
      * [ model_name  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel.model_name)
      * [ system  ](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModel.system)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_ai  ](https://ai.pydantic.dev/api/ag_ui/)


# `pydantic_ai.models.cohere`
## Setup
For details on how to set up authentication with this model, see [model configuration for Cohere](https://ai.pydantic.dev/models/cohere/).
###  LatestCohereModelNames `module-attribute`
```
LatestCohereModelNames = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
    "c4ai-aya-expanse-32b",
    "c4ai-aya-expanse-8b",
    "command-nightly",
    "command-r-08-2024",
    "command-r-plus-08-2024",
    "command-r7b-12-2024",
]

```

Latest Cohere models.
###  CohereModelName `module-attribute`
```
CohereModelName = str[](https://docs.python.org/3/library/stdtypes.html#str) | LatestCohereModelNames[](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.LatestCohereModelNames "LatestCohereModelNames



      module-attribute
   \(pydantic_ai.models.cohere.LatestCohereModelNames\)")

```

Possible Cohere model names.
Since Cohere supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See [Cohere's docs](https://docs.cohere.com/v2/docs/models) for a list of all available models.
###  CohereModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings used for a Cohere model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/cohere.py`
```
88
89
```
| ```
class CohereModelSettings(ModelSettings, total=False):
    """Settings used for a Cohere model request."""

```

---|---
###  CohereModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses the Cohere API.
Internally, this uses the [Cohere Python client](https://github.com/cohere-ai/cohere-python) to interact with the API.
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/cohere.py`
```
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
```
| ```
@dataclass(init=False)
class CohereModel(Model):
    """A model that uses the Cohere API.

    Internally, this uses the [Cohere Python client](
    https://github.com/cohere-ai/cohere-python) to interact with the API.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: AsyncClientV2 = field(repr=False)

    _model_name: CohereModelName = field(repr=False)
    _provider: Provider[AsyncClientV2] = field(repr=False)

    def __init__(
        self,
        model_name: CohereModelName,
        *,
        provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize an Cohere model.

        Args:
            model_name: The name of the Cohere model to use. List of model names
                available [here](https://docs.cohere.com/docs/models#command).
            provider: The provider to use for authentication and API access. Can be either the string
                'cohere' or an instance of `Provider[AsyncClientV2]`. If not provided, a new provider will be
                created using the other parameters.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    def base_url(self) -> str:
        client_wrapper = self.client._client_wrapper  # type: ignore
        return str(client_wrapper.get_base_url())

    @property
    def model_name(self) -> CohereModelName:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The model provider."""
        return self._provider.name

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._chat(messages, cast(CohereModelSettings, model_settings or {}), model_request_parameters)
        model_response = self._process_response(response)
        return model_response

    async def _chat(
        self,
        messages: list[ModelMessage],
        model_settings: CohereModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> V2ChatResponse:
        tools = self._get_tools(model_request_parameters)

        cohere_messages = self._map_messages(messages, model_request_parameters)
        try:
            return await self.client.chat(
                model=self._model_name,
                messages=cohere_messages,
                tools=tools or OMIT,
                max_tokens=model_settings.get('max_tokens', OMIT),
                stop_sequences=model_settings.get('stop_sequences', OMIT),
                temperature=model_settings.get('temperature', OMIT),
                p=model_settings.get('top_p', OMIT),
                seed=model_settings.get('seed', OMIT),
                presence_penalty=model_settings.get('presence_penalty', OMIT),
                frequency_penalty=model_settings.get('frequency_penalty', OMIT),
            )
        except ApiError as e:
            if (status_code := e.status_code) and status_code >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e

    def _process_response(self, response: V2ChatResponse) -> ModelResponse:
        """Process a non-streamed response, and prepare a message to return."""
        parts: list[ModelResponsePart] = []
        if response.message.content is not None:
            for content in response.message.content:
                if content.type == 'text':
                    parts.append(TextPart(content=content.text))
                elif content.type == 'thinking':  # pragma: no branch
                    parts.append(ThinkingPart(content=content.thinking))
        for c in response.message.tool_calls or []:
            if c.function and c.function.name and c.function.arguments:  # pragma: no branch
                parts.append(
                    ToolCallPart(
                        tool_name=c.function.name,
                        args=c.function.arguments,
                        tool_call_id=c.id or _generate_tool_call_id(),
                    )
                )

        raw_finish_reason = response.finish_reason
        provider_details = {'finish_reason': raw_finish_reason}
        finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

        return ModelResponse(
            parts=parts,
            usage=_map_usage(response),
            model_name=self._model_name,
            provider_name=self._provider.name,
            provider_url=self.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details,
        )

    def _map_messages(
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> list[ChatMessageV2]:
        """Just maps a `pydantic_ai.Message` to a `cohere.ChatMessageV2`."""
        cohere_messages: list[ChatMessageV2] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                cohere_messages.extend(self._map_user_message(message))
            elif isinstance(message, ModelResponse):
                texts: list[str] = []
                thinking: list[str] = []
                tool_calls: list[ToolCallV2] = []
                for item in message.parts:
                    if isinstance(item, TextPart):
                        texts.append(item.content)
                    elif isinstance(item, ThinkingPart):
                        thinking.append(item.content)
                    elif isinstance(item, ToolCallPart):
                        tool_calls.append(self._map_tool_call(item))
                    elif isinstance(item, BuiltinToolCallPart | BuiltinToolReturnPart):  # pragma: no cover
                        # This is currently never returned from cohere
                        pass
                    elif isinstance(item, FilePart):  # pragma: no cover
                        # Files generated by models are not sent back to models that don't themselves generate files.
                        pass
                    else:
                        assert_never(item)

                message_param = AssistantChatMessageV2(role='assistant')
                if texts or thinking:
                    contents: list[TextAssistantMessageV2ContentOneItem | ThinkingAssistantMessageV2ContentOneItem] = []
                    if thinking:
                        contents.append(ThinkingAssistantMessageV2ContentOneItem(thinking='\n\n'.join(thinking)))
                    if texts:  # pragma: no branch
                        contents.append(TextAssistantMessageV2ContentOneItem(text='\n\n'.join(texts)))
                    message_param.content = contents
                if tool_calls:
                    message_param.tool_calls = tool_calls
                cohere_messages.append(message_param)
            else:
                assert_never(message)
        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt_count = sum(1 for m in cohere_messages if isinstance(m, SystemChatMessageV2))
            cohere_messages.insert(system_prompt_count, SystemChatMessageV2(role='system', content=instructions))
        return cohere_messages

    def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[ToolV2]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    @staticmethod
    def _map_tool_call(t: ToolCallPart) -> ToolCallV2:
        return ToolCallV2(
            id=_guard_tool_call_id(t=t),
            type='function',
            function=ToolCallV2Function(
                name=t.tool_name,
                arguments=t.args_as_json_str(),
            ),
        )

    @staticmethod
    def _map_tool_definition(f: ToolDefinition) -> ToolV2:
        return ToolV2(
            type='function',
            function=ToolV2Function(
                name=f.name,
                description=f.description,
                parameters=f.parameters_json_schema,
            ),
        )

    @classmethod
    def _map_user_message(cls, message: ModelRequest) -> Iterable[ChatMessageV2]:
        for part in message.parts:
            if isinstance(part, SystemPromptPart):
                yield SystemChatMessageV2(role='system', content=part.content)
            elif isinstance(part, UserPromptPart):
                if isinstance(part.content, str):
                    yield UserChatMessageV2(role='user', content=part.content)
                else:
                    raise RuntimeError('Cohere does not yet support multi-modal inputs.')
            elif isinstance(part, ToolReturnPart):
                yield ToolChatMessageV2(
                    role='tool',
                    tool_call_id=_guard_tool_call_id(t=part),
                    content=part.model_response_str(),
                )
            elif isinstance(part, RetryPromptPart):
                if part.tool_name is None:
                    yield UserChatMessageV2(role='user', content=part.model_response())  # pragma: no cover
                else:
                    yield ToolChatMessageV2(
                        role='tool',
                        tool_call_id=_guard_tool_call_id(t=part),
                        content=part.model_response(),
                    )
            else:
                assert_never(part)

```

---|---
####  __init__
```
__init__(
    model_name: CohereModelName[](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelName "CohereModelName



      module-attribute
   \(pydantic_ai.models.cohere.CohereModelName\)"),
    *,
    provider: (
        Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["cohere"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClientV2]
    ) = "cohere",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize an Cohere model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `CohereModelName[](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelName "CohereModelName



      module-attribute
   \(pydantic_ai.models.cohere.CohereModelName\)")` |  The name of the Cohere model to use. List of model names available [here](https://docs.cohere.com/docs/models#command). |  _required_
`provider` |  `Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['cohere'] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncClientV2]` |  The provider to use for authentication and API access. Can be either the string 'cohere' or an instance of `Provider[AsyncClientV2]`. If not provided, a new provider will be created using the other parameters. |  `'cohere'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/cohere.py`
```
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
```
| ```
def __init__(
    self,
    model_name: CohereModelName,
    *,
    provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize an Cohere model.

    Args:
        model_name: The name of the Cohere model to use. List of model names
            available [here](https://docs.cohere.com/docs/models#command).
        provider: The provider to use for authentication and API access. Can be either the string
            'cohere' or an instance of `Provider[AsyncClientV2]`. If not provided, a new provider will be
            created using the other parameters.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
        settings: Model-specific settings that will be used as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self.client = provider.client

    super().__init__(settings=settings, profile=profile or provider.model_profile)

```

---|---
####  model_name `property`
```
model_name: CohereModelName[](https://ai.pydantic.dev/api/models/cohere/#pydantic_ai.models.cohere.CohereModelName "CohereModelName



      module-attribute
   \(pydantic_ai.models.cohere.CohereModelName\)")

```

The model name.
####  system `property`
```
system: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The model provider.
© Pydantic Services Inc. 2024 to present
