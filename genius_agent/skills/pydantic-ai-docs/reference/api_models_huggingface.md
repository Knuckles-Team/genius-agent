[ Skip to content ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_aimodelshuggingface)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_ai.models.huggingface
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
      * pydantic_ai.models.huggingface  [ pydantic_ai.models.huggingface  ](https://ai.pydantic.dev/api/models/huggingface/)
        * [ Setup  ](https://ai.pydantic.dev/api/models/huggingface/#setup)
          * [ huggingface  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface)
          * [ LatestHuggingFaceModelNames  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.LatestHuggingFaceModelNames)
          * [ HuggingFaceModelName  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModelName)
          * [ HuggingFaceModelSettings  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModelSettings)
          * [ HuggingFaceModel  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel)
            * [ __init__  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.__init__)
            * [ base_url  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.base_url)
            * [ model_name  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.model_name)
            * [ system  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.system)
          * [ HuggingFaceStreamedResponse  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse)
            * [ model_name  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.model_name)
            * [ provider_name  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.provider_name)
            * [ provider_url  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.provider_url)
            * [ timestamp  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.timestamp)
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


  * [ Setup  ](https://ai.pydantic.dev/api/models/huggingface/#setup)
    * [ huggingface  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface)
    * [ LatestHuggingFaceModelNames  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.LatestHuggingFaceModelNames "LatestHuggingFaceModelNames")
    * [ HuggingFaceModelName  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModelName)
    * [ HuggingFaceModelSettings  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModelSettings)
    * [ HuggingFaceModel  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel)
      * [ __init__  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.__init__)
      * [ base_url  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.base_url)
      * [ model_name  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.model_name)
      * [ system  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModel.system)
    * [ HuggingFaceStreamedResponse  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse "HuggingFaceStreamedResponse")
      * [ model_name  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.model_name)
      * [ provider_name  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.provider_name)
      * [ provider_url  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.provider_url)
      * [ timestamp  ](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceStreamedResponse.timestamp)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_ai  ](https://ai.pydantic.dev/api/ag_ui/)


# `pydantic_ai.models.huggingface`
## Setup
For details on how to set up authentication with this model, see [model configuration for Hugging Face](https://ai.pydantic.dev/models/huggingface/).
###  LatestHuggingFaceModelNames `module-attribute`
```
LatestHuggingFaceModelNames = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/Llama-3.3-70B-Instruct",
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct",
    "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    "Qwen/QwQ-32B",
    "Qwen/Qwen2.5-72B-Instruct",
    "Qwen/Qwen3-235B-A22B",
    "Qwen/Qwen3-32B",
]

```

Latest Hugging Face models.
###  HuggingFaceModelName `module-attribute`
```
HuggingFaceModelName = str[](https://docs.python.org/3/library/stdtypes.html#str) | LatestHuggingFaceModelNames[](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.LatestHuggingFaceModelNames "LatestHuggingFaceModelNames



      module-attribute
   \(pydantic_ai.models.huggingface.LatestHuggingFaceModelNames\)")

```

Possible Hugging Face model names.
You can browse available models [here](https://huggingface.co/models?pipeline_tag=text-generation&inference_provider=all&sort=trending).
###  HuggingFaceModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings used for a Hugging Face model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/huggingface.py`
```
109
110
```
| ```
class HuggingFaceModelSettings(ModelSettings, total=False):
    """Settings used for a Hugging Face model request."""

```

---|---
###  HuggingFaceModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses Hugging Face Inference Providers.
Internally, this uses the [HF Python client](https://github.com/huggingface/huggingface_hub) to interact with the API.
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/huggingface.py`
```
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
407
408
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
```
| ```
@dataclass(init=False)
class HuggingFaceModel(Model):
    """A model that uses Hugging Face Inference Providers.

    Internally, this uses the [HF Python client](https://github.com/huggingface/huggingface_hub) to interact with the API.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: AsyncInferenceClient = field(repr=False)

    _model_name: str = field(repr=False)
    _provider: Provider[AsyncInferenceClient] = field(repr=False)

    def __init__(
        self,
        model_name: str,
        *,
        provider: Literal['huggingface'] | Provider[AsyncInferenceClient] = 'huggingface',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize a Hugging Face model.

        Args:
            model_name: The name of the Model to use. You can browse available models [here](https://huggingface.co/models?pipeline_tag=text-generation&inference_provider=all&sort=trending).
            provider: The provider to use for Hugging Face Inference Providers. Can be either the string 'huggingface' or an
                instance of `Provider[AsyncInferenceClient]`. If not provided, the other parameters will be used.
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
        """The base URL of the provider."""
        return self._provider.base_url

    @property
    def model_name(self) -> HuggingFaceModelName:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The system / model provider."""
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
        response = await self._completions_create(
            messages, False, cast(HuggingFaceModelSettings, model_settings or {}), model_request_parameters
        )
        model_response = self._process_response(response)
        return model_response

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._completions_create(
            messages, True, cast(HuggingFaceModelSettings, model_settings or {}), model_request_parameters
        )
        yield await self._process_streamed_response(response, model_request_parameters)

    @overload
    async def _completions_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[True],
        model_settings: HuggingFaceModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncIterable[ChatCompletionStreamOutput]: ...

    @overload
    async def _completions_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[False],
        model_settings: HuggingFaceModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> ChatCompletionOutput: ...

    async def _completions_create(
        self,
        messages: list[ModelMessage],
        stream: bool,
        model_settings: HuggingFaceModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> ChatCompletionOutput | AsyncIterable[ChatCompletionStreamOutput]:
        tools = self._get_tools(model_request_parameters)

        if not tools:
            tool_choice: Literal['none', 'required', 'auto'] | None = None
        elif not model_request_parameters.allow_text_output:
            tool_choice = 'required'
        else:
            tool_choice = 'auto'

        hf_messages = await self._map_messages(messages, model_request_parameters)

        try:
            return await self.client.chat.completions.create(  # type: ignore
                model=self._model_name,
                messages=hf_messages,  # type: ignore
                tools=tools,
                tool_choice=tool_choice or None,
                stream=stream,
                max_tokens=model_settings.get('max_tokens', None),
                stop=model_settings.get('stop_sequences', None),
                temperature=model_settings.get('temperature', None),
                top_p=model_settings.get('top_p', None),
                seed=model_settings.get('seed', None),
                presence_penalty=model_settings.get('presence_penalty', None),
                frequency_penalty=model_settings.get('frequency_penalty', None),
                logit_bias=model_settings.get('logit_bias', None),  # type: ignore
                logprobs=model_settings.get('logprobs', None),
                top_logprobs=model_settings.get('top_logprobs', None),
                extra_body=model_settings.get('extra_body'),  # type: ignore
            )
        except HfHubHTTPError as e:
            raise ModelHTTPError(
                status_code=e.response.status_code,
                model_name=self.model_name,
                body=e.response.content,
            ) from e

    def _process_response(self, response: ChatCompletionOutput) -> ModelResponse:
        """Process a non-streamed response, and prepare a message to return."""
        choice = response.choices[0]
        content = choice.message.content
        tool_calls = choice.message.tool_calls

        items: list[ModelResponsePart] = []

        if content:
            items.extend(split_content_into_text_and_thinking(content, self.profile.thinking_tags))
        if tool_calls is not None:
            for c in tool_calls:
                items.append(ToolCallPart(c.function.name, c.function.arguments, tool_call_id=c.id))

        raw_finish_reason = choice.finish_reason
        provider_details: dict[str, Any] = {'finish_reason': raw_finish_reason}
        if response.created:  # pragma: no branch
            provider_details['timestamp'] = datetime.fromtimestamp(response.created, tz=timezone.utc)
        finish_reason = _FINISH_REASON_MAP.get(cast(HuggingFaceFinishReason, raw_finish_reason), None)

        return ModelResponse(
            parts=items,
            usage=_map_usage(response),
            model_name=response.model,
            provider_response_id=response.id,
            provider_name=self._provider.name,
            provider_url=self.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details,
        )

    async def _process_streamed_response(
        self, response: AsyncIterable[ChatCompletionStreamOutput], model_request_parameters: ModelRequestParameters
    ) -> StreamedResponse:
        """Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):
            raise UnexpectedModelBehavior(  # pragma: no cover
                'Streamed response ended without content or tool calls'
            )

        return HuggingFaceStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=first_chunk.model,
            _model_profile=self.profile,
            _response=peekable_response,
            _provider_name=self._provider.name,
            _provider_url=self.base_url,
            _provider_timestamp=datetime.fromtimestamp(first_chunk.created, tz=timezone.utc),
        )

    def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[ChatCompletionInputTool]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    async def _map_messages(
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> list[ChatCompletionInputMessage | ChatCompletionOutputMessage]:
        """Just maps a `pydantic_ai.Message` to a `huggingface_hub.ChatCompletionInputMessage`."""
        hf_messages: list[ChatCompletionInputMessage | ChatCompletionOutputMessage] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                async for item in self._map_user_message(message):
                    hf_messages.append(item)
            elif isinstance(message, ModelResponse):
                texts: list[str] = []
                tool_calls: list[ChatCompletionInputToolCall] = []
                for item in message.parts:
                    if isinstance(item, TextPart):
                        texts.append(item.content)
                    elif isinstance(item, ToolCallPart):
                        tool_calls.append(self._map_tool_call(item))
                    elif isinstance(item, ThinkingPart):
                        start_tag, end_tag = self.profile.thinking_tags
                        texts.append('\n'.join([start_tag, item.content, end_tag]))
                    elif isinstance(item, BuiltinToolCallPart | BuiltinToolReturnPart):  # pragma: no cover
                        # This is currently never returned from huggingface
                        pass
                    elif isinstance(item, FilePart):  # pragma: no cover
                        # Files generated by models are not sent back to models that don't themselves generate files.
                        pass
                    else:
                        assert_never(item)
                message_param = ChatCompletionInputMessage(role='assistant')
                if texts:
                    # Note: model responses from this model should only have one text item, so the following
                    # shouldn't merge multiple texts into one unless you switch models between runs:
                    message_param['content'] = '\n\n'.join(texts)
                if tool_calls:
                    message_param['tool_calls'] = tool_calls
                hf_messages.append(message_param)
            else:
                assert_never(message)
        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt_count = sum(1 for m in hf_messages if getattr(m, 'role', None) == 'system')
            hf_messages.insert(system_prompt_count, ChatCompletionInputMessage(content=instructions, role='system'))
        return hf_messages

    @staticmethod
    def _map_tool_call(t: ToolCallPart) -> ChatCompletionInputToolCall:
        return ChatCompletionInputToolCall.parse_obj_as_instance(  # type: ignore
            {
                'id': _guard_tool_call_id(t=t),
                'type': 'function',
                'function': {
                    'name': t.tool_name,
                    'arguments': t.args_as_json_str(),
                },
            }
        )

    @staticmethod
    def _map_tool_definition(f: ToolDefinition) -> ChatCompletionInputTool:
        tool_param: ChatCompletionInputTool = ChatCompletionInputTool.parse_obj_as_instance(  # type: ignore
            {
                'type': 'function',
                'function': {
                    'name': f.name,
                    'description': f.description,
                    'parameters': f.parameters_json_schema,
                },
            }
        )
        return tool_param

    async def _map_user_message(
        self, message: ModelRequest
    ) -> AsyncIterable[ChatCompletionInputMessage | ChatCompletionOutputMessage]:
        for part in message.parts:
            if isinstance(part, SystemPromptPart):
                yield ChatCompletionInputMessage.parse_obj_as_instance({'role': 'system', 'content': part.content})  # type: ignore
            elif isinstance(part, UserPromptPart):
                yield await self._map_user_prompt(part)
            elif isinstance(part, ToolReturnPart):
                yield ChatCompletionOutputMessage.parse_obj_as_instance(  # type: ignore
                    {
                        'role': 'tool',
                        'tool_call_id': _guard_tool_call_id(t=part),
                        'content': part.model_response_str(),
                    }
                )
            elif isinstance(part, RetryPromptPart):
                if part.tool_name is None:
                    yield ChatCompletionInputMessage.parse_obj_as_instance(  # type: ignore
                        {'role': 'user', 'content': part.model_response()}
                    )
                else:
                    yield ChatCompletionInputMessage.parse_obj_as_instance(  # type: ignore
                        {
                            'role': 'tool',
                            'tool_call_id': _guard_tool_call_id(t=part),
                            'content': part.model_response(),
                        }
                    )
            else:
                assert_never(part)

    @staticmethod
    async def _map_user_prompt(part: UserPromptPart) -> ChatCompletionInputMessage:
        content: str | list[ChatCompletionInputMessage]
        if isinstance(part.content, str):
            content = part.content
        else:
            content = []
            for item in part.content:
                if isinstance(item, str):
                    content.append(ChatCompletionInputMessageChunk(type='text', text=item))  # type: ignore
                elif isinstance(item, ImageUrl):
                    url = ChatCompletionInputURL(url=item.url)
                    content.append(ChatCompletionInputMessageChunk(type='image_url', image_url=url))  # type: ignore
                elif isinstance(item, BinaryContent):
                    if item.is_image:
                        url = ChatCompletionInputURL(url=item.data_uri)
                        content.append(ChatCompletionInputMessageChunk(type='image_url', image_url=url))  # type: ignore
                    else:  # pragma: no cover
                        raise RuntimeError(f'Unsupported binary content type: {item.media_type}')
                elif isinstance(item, AudioUrl):
                    raise NotImplementedError('AudioUrl is not supported for Hugging Face')
                elif isinstance(item, DocumentUrl):
                    raise NotImplementedError('DocumentUrl is not supported for Hugging Face')
                elif isinstance(item, VideoUrl):
                    raise NotImplementedError('VideoUrl is not supported for Hugging Face')
                elif isinstance(item, CachePoint):
                    # Hugging Face doesn't support prompt caching via CachePoint
                    pass
                else:
                    assert_never(item)
        return ChatCompletionInputMessage(role='user', content=content)  # type: ignore

```

---|---
####  __init__
```
__init__(
    model_name: str[](https://docs.python.org/3/library/stdtypes.html#str),
    *,
    provider: (
        Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["huggingface"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncInferenceClient]
    ) = "huggingface",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize a Hugging Face model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  The name of the Model to use. You can browse available models [here](https://huggingface.co/models?pipeline_tag=text-generation&inference_provider=all&sort=trending). |  _required_
`provider` |  `Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['huggingface'] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncInferenceClient]` |  The provider to use for Hugging Face Inference Providers. Can be either the string 'huggingface' or an instance of `Provider[AsyncInferenceClient]`. If not provided, the other parameters will be used. |  `'huggingface'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/huggingface.py`
```
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
```
| ```
def __init__(
    self,
    model_name: str,
    *,
    provider: Literal['huggingface'] | Provider[AsyncInferenceClient] = 'huggingface',
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize a Hugging Face model.

    Args:
        model_name: The name of the Model to use. You can browse available models [here](https://huggingface.co/models?pipeline_tag=text-generation&inference_provider=all&sort=trending).
        provider: The provider to use for Hugging Face Inference Providers. Can be either the string 'huggingface' or an
            instance of `Provider[AsyncInferenceClient]`. If not provided, the other parameters will be used.
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
####  base_url `property`
```
base_url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The base URL of the provider.
####  model_name `property`
```
model_name: HuggingFaceModelName[](https://ai.pydantic.dev/api/models/huggingface/#pydantic_ai.models.huggingface.HuggingFaceModelName "HuggingFaceModelName



      module-attribute
   \(pydantic_ai.models.huggingface.HuggingFaceModelName\)")

```

The model name.
####  system `property`
```
system: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The system / model provider.
###  HuggingFaceStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for Hugging Face models.
Source code in `pydantic_ai_slim/pydantic_ai/models/huggingface.py`
```
457
458
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
```
| ```
@dataclass
class HuggingFaceStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for Hugging Face models."""

    _model_name: str
    _model_profile: ModelProfile
    _response: AsyncIterable[ChatCompletionStreamOutput]
    _provider_name: str
    _provider_url: str
    _provider_timestamp: datetime | None = None
    _timestamp: datetime = field(default_factory=_utils.now_utc)

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
        if self._provider_timestamp is not None:  # pragma: no branch
            self.provider_details = {'timestamp': self._provider_timestamp}
        async for chunk in self._response:
            self._usage += _map_usage(chunk)

            if chunk.id:  # pragma: no branch
                self.provider_response_id = chunk.id

            try:
                choice = chunk.choices[0]
            except IndexError:
                continue

            if raw_finish_reason := choice.finish_reason:
                self.provider_details = {**(self.provider_details or {}), 'finish_reason': raw_finish_reason}
                self.finish_reason = _FINISH_REASON_MAP.get(cast(HuggingFaceFinishReason, raw_finish_reason), None)

            # Handle the text part of the response
            content = choice.delta.content
            if content:
                for event in self._parts_manager.handle_text_delta(
                    vendor_part_id='content',
                    content=content,
                    thinking_tags=self._model_profile.thinking_tags,
                    ignore_leading_whitespace=self._model_profile.ignore_streamed_leading_whitespace,
                ):
                    yield event

            for dtc in choice.delta.tool_calls or []:
                maybe_event = self._parts_manager.handle_tool_call_delta(
                    vendor_part_id=dtc.index,
                    tool_name=dtc.function and dtc.function.name,  # type: ignore
                    args=dtc.function and dtc.function.arguments,
                    tool_call_id=dtc.id,
                )
                if maybe_event is not None:
                    yield maybe_event

    @property
    def model_name(self) -> str:
        """Get the model name of the response."""
        return self._model_name

    @property
    def provider_name(self) -> str:
        """Get the provider name."""
        return self._provider_name

    @property
    def provider_url(self) -> str:
        """Get the provider base URL."""
        return self._provider_url

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
provider_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Get the provider name.
####  provider_url `property`
```
provider_url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Get the provider base URL.
####  timestamp `property`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")

```

Get the timestamp of the response.
© Pydantic Services Inc. 2024 to present
