[ Skip to content ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graphbetagraph_builder)
**Join us at the inaugural PyAI Conf in San Francisco on March 10th![Learn More](https://pyai.events/?utm_source=pydantic-ai) **
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "Pydantic AI")
Pydantic AI
pydantic_graph.beta.graph_builder
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
        * pydantic_graph.beta.graph_builder  [ pydantic_graph.beta.graph_builder  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/)
          * [ graph_builder  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder)
          * [ GraphBuilder  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder)
            * [ __init__  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.__init__)
            * [ name  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.name)
            * [ state_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.state_type)
            * [ deps_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.deps_type)
            * [ input_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.input_type)
            * [ output_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.output_type)
            * [ auto_instrument  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.auto_instrument)
            * [ start_node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.start_node)
            * [ end_node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.end_node)
            * [ step  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.step)
            * [ stream  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.stream)
            * [ add  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add)
            * [ add_edge  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add_edge)
            * [ add_mapping_edge  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add_mapping_edge)
            * [ edge_from  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.edge_from)
            * [ decision  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.decision)
            * [ match  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.match)
            * [ match_node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.match_node)
            * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.node)
            * [ build  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.build)
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


  * [ graph_builder  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder)
  * [ GraphBuilder  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder)
    * [ __init__  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.__init__)
    * [ name  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.name)
    * [ state_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.state_type)
    * [ deps_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.deps_type)
    * [ input_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.input_type)
    * [ output_type  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.output_type)
    * [ auto_instrument  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.auto_instrument)
    * [ start_node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.start_node)
    * [ end_node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.end_node)
    * [ step  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.step)
    * [ stream  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.stream)
    * [ add  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add)
    * [ add_edge  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add_edge)
    * [ add_mapping_edge  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add_mapping_edge)
    * [ edge_from  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.edge_from)
    * [ decision  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.decision)
    * [ match  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.match)
    * [ match_node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.match_node)
    * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.node)
    * [ build  ](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.build)


  1. [ Pydantic AI  ](https://ai.pydantic.dev/)
  2. [ API Reference  ](https://ai.pydantic.dev/api/ag_ui/)
  3. [ pydantic_graph  ](https://ai.pydantic.dev/api/pydantic_graph/graph/)
  4. [ Beta API  ](https://ai.pydantic.dev/api/pydantic_graph/beta/)


# `pydantic_graph.beta.graph_builder`
Graph builder for constructing executable graph definitions.
This module provides the GraphBuilder class and related utilities for constructing typed, executable graph definitions with steps, joins, decisions, and edge routing.
###  GraphBuilder `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT, DepsT, GraphInputT, GraphOutputT]`
A builder for constructing executable graph definitions.
GraphBuilder provides a fluent interface for defining nodes, edges, and routing in a graph workflow. It supports typed state, dependencies, and input/output validation.
Class Type Parameters:
Name | Bound or Constraints | Description | Default
---|---|---|---
`StateT` |  |  The type of the graph state |  _required_
`DepsT` |  |  The type of the dependencies |  _required_
`GraphInputT` |  |  The type of the graph input data |  _required_
`GraphOutputT` |  |  The type of the graph output data |  _required_
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
455
456
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
614
615
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
643
644
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
667
668
669
670
671
672
673
674
675
676
```
| ```
@dataclass(init=False)
class GraphBuilder(Generic[StateT, DepsT, GraphInputT, GraphOutputT]):
    """A builder for constructing executable graph definitions.

    GraphBuilder provides a fluent interface for defining nodes, edges, and
    routing in a graph workflow. It supports typed state, dependencies, and
    input/output validation.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        GraphInputT: The type of the graph input data
        GraphOutputT: The type of the graph output data
    """

    name: str | None
    """Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method."""

    state_type: TypeOrTypeExpression[StateT]
    """The type of the graph state."""

    deps_type: TypeOrTypeExpression[DepsT]
    """The type of the dependencies."""

    input_type: TypeOrTypeExpression[GraphInputT]
    """The type of the graph input data."""

    output_type: TypeOrTypeExpression[GraphOutputT]
    """The type of the graph output data."""

    auto_instrument: bool
    """Whether to automatically create instrumentation spans."""

    _nodes: dict[NodeID, AnyNode]
    """Internal storage for nodes in the graph."""

    _edges_by_source: dict[NodeID, list[Path]]
    """Internal storage for edges by source node."""

    _decision_index: int
    """Counter for generating unique decision node IDs."""

    Source = TypeAliasType('Source', SourceNode[StateT, DepsT, OutputT], type_params=(OutputT,))
    Destination = TypeAliasType('Destination', DestinationNode[StateT, DepsT, InputT], type_params=(InputT,))

    def __init__(
        self,
        *,
        name: str | None = None,
        state_type: TypeOrTypeExpression[StateT] = NoneType,
        deps_type: TypeOrTypeExpression[DepsT] = NoneType,
        input_type: TypeOrTypeExpression[GraphInputT] = NoneType,
        output_type: TypeOrTypeExpression[GraphOutputT] = NoneType,
        auto_instrument: bool = True,
    ):
        """Initialize a graph builder.

        Args:
            name: Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method.
            state_type: The type of the graph state
            deps_type: The type of the dependencies
            input_type: The type of the graph input data
            output_type: The type of the graph output data
            auto_instrument: Whether to automatically create instrumentation spans
        """
        self.name = name

        self.state_type = state_type
        self.deps_type = deps_type
        self.input_type = input_type
        self.output_type = output_type

        self.auto_instrument = auto_instrument

        self._nodes = {}
        self._edges_by_source = defaultdict(list)
        self._decision_index = 1

        self._start_node = StartNode[GraphInputT]()
        self._end_node = EndNode[GraphOutputT]()

    # Node building
    @property
    def start_node(self) -> StartNode[GraphInputT]:
        """Get the start node for the graph.

        Returns:
            The start node that receives the initial graph input
        """
        return self._start_node

    @property
    def end_node(self) -> EndNode[GraphOutputT]:
        """Get the end node for the graph.

        Returns:
            The end node that produces the final graph output
        """
        return self._end_node

    @overload
    def step(
        self,
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> Callable[[StepFunction[StateT, DepsT, InputT, OutputT]], Step[StateT, DepsT, InputT, OutputT]]: ...
    @overload
    def step(
        self,
        call: StepFunction[StateT, DepsT, InputT, OutputT],
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> Step[StateT, DepsT, InputT, OutputT]: ...
    def step(
        self,
        call: StepFunction[StateT, DepsT, InputT, OutputT] | None = None,
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> (
        Step[StateT, DepsT, InputT, OutputT]
        | Callable[[StepFunction[StateT, DepsT, InputT, OutputT]], Step[StateT, DepsT, InputT, OutputT]]
    ):
        """Create a step from a step function.

        This method can be used as a decorator or called directly to create
        a step node from an async function.

        Args:
            call: The step function to wrap
            node_id: Optional ID for the node
            label: Optional human-readable label

        Returns:
            Either a Step instance or a decorator function
        """
        if call is None:

            def decorator(
                func: StepFunction[StateT, DepsT, InputT, OutputT],
            ) -> Step[StateT, DepsT, InputT, OutputT]:
                return self.step(call=func, node_id=node_id, label=label)

            return decorator

        node_id = node_id or get_callable_name(call)

        step = Step[StateT, DepsT, InputT, OutputT](id=NodeID(node_id), call=call, label=label)

        return step

    @overload
    def stream(
        self,
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> Callable[
        [StreamFunction[StateT, DepsT, InputT, OutputT]], Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]
    ]: ...
    @overload
    def stream(
        self,
        call: StreamFunction[StateT, DepsT, InputT, OutputT],
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]: ...
    @overload
    def stream(
        self,
        call: StreamFunction[StateT, DepsT, InputT, OutputT] | None = None,
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> (
        Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]
        | Callable[
            [StreamFunction[StateT, DepsT, InputT, OutputT]],
            Step[StateT, DepsT, InputT, AsyncIterable[OutputT]],
        ]
    ): ...
    def stream(
        self,
        call: StreamFunction[StateT, DepsT, InputT, OutputT] | None = None,
        *,
        node_id: str | None = None,
        label: str | None = None,
    ) -> (
        Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]
        | Callable[
            [StreamFunction[StateT, DepsT, InputT, OutputT]],
            Step[StateT, DepsT, InputT, AsyncIterable[OutputT]],
        ]
    ):
        """Create a step from an async iterator (which functions like a "stream").

        This method can be used as a decorator or called directly to create
        a step node from an async function.

        Args:
            call: The step function to wrap
            node_id: Optional ID for the node
            label: Optional human-readable label

        Returns:
            Either a Step instance or a decorator function
        """
        if call is None:

            def decorator(
                func: StreamFunction[StateT, DepsT, InputT, OutputT],
            ) -> Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]:
                return self.stream(call=func, node_id=node_id, label=label)

            return decorator

        # We need to wrap the call so that we can call `await` even though the result is an async iterator
        async def wrapper(ctx: StepContext[StateT, DepsT, InputT]):
            return call(ctx)

        node_id = node_id or get_callable_name(call)

        return self.step(call=wrapper, node_id=node_id, label=label)

    @overload
    def join(
        self,
        reducer: ReducerFunction[StateT, DepsT, InputT, OutputT],
        *,
        initial: OutputT,
        node_id: str | None = None,
        parent_fork_id: str | None = None,
        preferred_parent_fork: Literal['farthest', 'closest'] = 'farthest',
    ) -> Join[StateT, DepsT, InputT, OutputT]: ...
    @overload
    def join(
        self,
        reducer: ReducerFunction[StateT, DepsT, InputT, OutputT],
        *,
        initial_factory: Callable[[], OutputT],
        node_id: str | None = None,
        parent_fork_id: str | None = None,
        preferred_parent_fork: Literal['farthest', 'closest'] = 'farthest',
    ) -> Join[StateT, DepsT, InputT, OutputT]: ...

    def join(
        self,
        reducer: ReducerFunction[StateT, DepsT, InputT, OutputT],
        *,
        initial: OutputT | Unset = UNSET,
        initial_factory: Callable[[], OutputT] | Unset = UNSET,
        node_id: str | None = None,
        parent_fork_id: str | None = None,
        preferred_parent_fork: Literal['farthest', 'closest'] = 'farthest',
    ) -> Join[StateT, DepsT, InputT, OutputT]:
        if initial_factory is UNSET:
            initial_factory = lambda: initial  # pyright: ignore[reportAssignmentType]  # noqa: E731

        return Join[StateT, DepsT, InputT, OutputT](
            id=JoinID(NodeID(node_id or generate_placeholder_node_id(get_callable_name(reducer)))),
            reducer=reducer,
            initial_factory=cast(Callable[[], OutputT], initial_factory),
            parent_fork_id=ForkID(parent_fork_id) if parent_fork_id is not None else None,
            preferred_parent_fork=preferred_parent_fork,
        )

    # Edge building
    def add(self, *edges: EdgePath[StateT, DepsT]) -> None:  # noqa: C901
        """Add one or more edge paths to the graph.

        This method processes edge paths and automatically creates any necessary
        fork nodes for broadcasts and maps.

        Args:
            *edges: The edge paths to add to the graph
        """

        def _handle_path(p: Path):
            """Process a path and create necessary fork nodes.

            Args:
                p: The path to process
            """
            for item in p.items:
                if isinstance(item, BroadcastMarker):
                    new_node = Fork[Any, Any](id=item.fork_id, is_map=False, downstream_join_id=None)
                    self._insert_node(new_node)
                    for path in item.paths:
                        _handle_path(Path(items=[*path.items]))
                elif isinstance(item, MapMarker):
                    new_node = Fork[Any, Any](id=item.fork_id, is_map=True, downstream_join_id=item.downstream_join_id)
                    self._insert_node(new_node)
                elif isinstance(item, DestinationMarker):
                    pass

        def _handle_destination_node(d: AnyDestinationNode):
            if id(d) in destination_ids:
                return  # prevent infinite recursion if there is a cycle of decisions

            destination_ids.add(id(d))
            destinations.append(d)
            self._insert_node(d)
            if isinstance(d, Decision):
                for branch in d.branches:
                    _handle_path(branch.path)
                    for d2 in branch.destinations:
                        _handle_destination_node(d2)

        destination_ids = set[int]()
        destinations: list[AnyDestinationNode] = []
        for edge in edges:
            for source_node in edge.sources:
                self._insert_node(source_node)
                self._edges_by_source[source_node.id].append(edge.path)
            for destination_node in edge.destinations:
                _handle_destination_node(destination_node)
            _handle_path(edge.path)

        # Automatically create edges from step function return hints including `BaseNode`s
        for destination in destinations:
            if not isinstance(destination, Step) or isinstance(destination, NodeStep):
                continue
            parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
            type_hints = get_type_hints(destination.call, localns=parent_namespace, include_extras=True)
            try:
                return_hint = type_hints['return']
            except KeyError:
                pass
            else:
                edge = self._edge_from_return_hint(destination, return_hint)
                if edge is not None:
                    self.add(edge)

    def add_edge(self, source: Source[T], destination: Destination[T], *, label: str | None = None) -> None:
        """Add a simple edge between two nodes.

        Args:
            source: The source node
            destination: The destination node
            label: Optional label for the edge
        """
        builder = self.edge_from(source)
        if label is not None:
            builder = builder.label(label)
        self.add(builder.to(destination))

    def add_mapping_edge(
        self,
        source: Source[Iterable[T]],
        map_to: Destination[T],
        *,
        pre_map_label: str | None = None,
        post_map_label: str | None = None,
        fork_id: ForkID | None = None,
        downstream_join_id: JoinID | None = None,
    ) -> None:
        """Add an edge that maps iterable data across parallel paths.

        Args:
            source: The source node that produces iterable data
            map_to: The destination node that receives individual items
            pre_map_label: Optional label before the map operation
            post_map_label: Optional label after the map operation
            fork_id: Optional ID for the fork node produced for this map operation
            downstream_join_id: Optional ID of a join node that will always be downstream of this map.
                Specifying this ensures correct handling if you try to map an empty iterable.
        """
        builder = self.edge_from(source)
        if pre_map_label is not None:
            builder = builder.label(pre_map_label)
        builder = builder.map(fork_id=fork_id, downstream_join_id=downstream_join_id)
        if post_map_label is not None:
            builder = builder.label(post_map_label)
        self.add(builder.to(map_to))

    # TODO(DavidM): Support adding subgraphs; I think this behaves like a step with the same inputs/outputs but gets rendered as a subgraph in mermaid

    def edge_from(self, *sources: Source[SourceOutputT]) -> EdgePathBuilder[StateT, DepsT, SourceOutputT]:
        """Create an edge path builder starting from the given source nodes.

        Args:
            *sources: The source nodes to start the edge path from

        Returns:
            An EdgePathBuilder for constructing the complete edge path
        """
        return EdgePathBuilder[StateT, DepsT, SourceOutputT](
            sources=sources, path_builder=PathBuilder(working_items=[])
        )

    def decision(self, *, note: str | None = None, node_id: str | None = None) -> Decision[StateT, DepsT, Never]:
        """Create a new decision node.

        Args:
            note: Optional note to describe the decision logic
            node_id: Optional ID for the node produced for this decision logic

        Returns:
            A new Decision node with no branches
        """
        return Decision(id=NodeID(node_id or generate_placeholder_node_id('decision')), branches=[], note=note)

    def match(
        self,
        source: TypeOrTypeExpression[SourceT],
        *,
        matches: Callable[[Any], bool] | None = None,
    ) -> DecisionBranchBuilder[StateT, DepsT, SourceT, SourceT, Never]:
        """Create a decision branch matcher.

        Args:
            source: The type or type expression to match against
            matches: Optional custom matching function

        Returns:
            A DecisionBranchBuilder for constructing the branch
        """
        # Note, the following node_id really is just a placeholder and shouldn't end up in the final graph
        # This is why we don't expose a way for end users to override the value used here.
        node_id = NodeID(generate_placeholder_node_id('match_decision'))
        decision = Decision[StateT, DepsT, Never](id=node_id, branches=[], note=None)
        new_path_builder = PathBuilder[StateT, DepsT, SourceT](working_items=[])
        return DecisionBranchBuilder(decision=decision, source=source, matches=matches, path_builder=new_path_builder)

    def match_node(
        self,
        source: type[SourceNodeT],
        *,
        matches: Callable[[Any], bool] | None = None,
    ) -> DecisionBranch[SourceNodeT]:
        """Create a decision branch for BaseNode subclasses.

        This is similar to match() but specifically designed for matching
        against BaseNode types from the v1 system.

        Args:
            source: The BaseNode subclass to match against
            matches: Optional custom matching function

        Returns:
            A DecisionBranch for the BaseNode type
        """
        node = NodeStep(source)
        path = Path(items=[DestinationMarker(node.id)])
        return DecisionBranch(source=source, matches=matches, path=path, destinations=[node])

    def node(
        self,
        node_type: type[BaseNode[StateT, DepsT, GraphOutputT]],
    ) -> EdgePath[StateT, DepsT]:
        """Create an edge path from a BaseNode class.

        This method integrates v1-style BaseNode classes into the v2 graph
        system by analyzing their type hints and creating appropriate edges.

        Args:
            node_type: The BaseNode subclass to integrate

        Returns:
            An EdgePath representing the node and its connections

        Raises:
            GraphSetupError: If the node type is missing required type hints
        """
        parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
        type_hints = get_type_hints(node_type.run, localns=parent_namespace, include_extras=True)
        try:
            return_hint = type_hints['return']
        except KeyError as e:  # pragma: no cover
            raise exceptions.GraphSetupError(
                f'Node {node_type} is missing a return type hint on its `run` method'
            ) from e

        node = NodeStep(node_type)

        edge = self._edge_from_return_hint(node, return_hint)
        if not edge:  # pragma: no cover
            raise exceptions.GraphSetupError(f'Node {node_type} is missing a return type hint on its `run` method')

        return edge

    # Helpers
    def _insert_node(self, node: AnyNode) -> None:
        """Insert a node into the graph, checking for ID conflicts.

        Args:
            node: The node to insert

        Raises:
            ValueError: If a different node with the same ID already exists
        """
        existing = self._nodes.get(node.id)
        if existing is None:
            self._nodes[node.id] = node
        elif isinstance(existing, NodeStep) and isinstance(node, NodeStep) and existing.node_type is node.node_type:
            pass
        elif existing is not node:
            raise GraphBuildingError(
                f'All nodes must have unique node IDs. {node.id!r} was the ID for {existing} and {node}'
            )

    def _edge_from_return_hint(
        self, node: SourceNode[StateT, DepsT, Any], return_hint: TypeOrTypeExpression[Any]
    ) -> EdgePath[StateT, DepsT] | None:
        """Create edges from a return type hint.

        This method analyzes return type hints from step functions or node methods
        to automatically create appropriate edges in the graph.

        Args:
            node: The source node
            return_hint: The return type hint to analyze

        Returns:
            An EdgePath if edges can be inferred, None otherwise

        Raises:
            GraphSetupError: If the return type hint is invalid or incomplete
        """
        destinations: list[AnyDestinationNode] = []
        union_args = _utils.get_union_args(return_hint)
        for return_type in union_args:
            return_type, annotations = _utils.unpack_annotated(return_type)
            return_type_origin = get_origin(return_type) or return_type
            if return_type_origin is End:
                destinations.append(self.end_node)
            elif return_type_origin is BaseNode:
                raise exceptions.GraphSetupError(  # pragma: no cover
                    f'Node {node} return type hint includes a plain `BaseNode`. '
                    'Edge inference requires each possible returned `BaseNode` subclass to be listed explicitly.'
                )
            elif return_type_origin is StepNode:
                step = cast(
                    Step[StateT, DepsT, Any, Any] | None,
                    next((a for a in annotations if isinstance(a, Step)), None),  # pyright: ignore[reportUnknownArgumentType]
                )
                if step is None:
                    raise exceptions.GraphSetupError(  # pragma: no cover
                        f'Node {node} return type hint includes a `StepNode` without a `Step` annotation. '
                        'When returning `my_step.as_node()`, use `Annotated[StepNode[StateT, DepsT], my_step]` as the return type hint.'
                    )
                destinations.append(step)
            elif return_type_origin is JoinNode:
                join = cast(
                    Join[StateT, DepsT, Any, Any] | None,
                    next((a for a in annotations if isinstance(a, Join)), None),  # pyright: ignore[reportUnknownArgumentType]
                )
                if join is None:
                    raise exceptions.GraphSetupError(  # pragma: no cover
                        f'Node {node} return type hint includes a `JoinNode` without a `Join` annotation. '
                        'When returning `my_join.as_node()`, use `Annotated[JoinNode[StateT, DepsT], my_join]` as the return type hint.'
                    )
                destinations.append(join)
            elif inspect.isclass(return_type_origin) and issubclass(return_type_origin, BaseNode):
                destinations.append(NodeStep(return_type))

        if len(destinations) < len(union_args):
            # Only build edges if all the return types are nodes
            return None

        edge = self.edge_from(node)
        if len(destinations) == 1:
            return edge.to(destinations[0])
        else:
            decision = self.decision()
            for destination in destinations:
                # We don't actually use this decision mechanism, but we need to build the edges for parent-fork finding
                decision = decision.branch(self.match(NoneType).to(destination))
            return edge.to(decision)

    # Graph building
    def build(self, validate_graph_structure: bool = True) -> Graph[StateT, DepsT, GraphInputT, GraphOutputT]:
        """Build the final executable graph from the accumulated nodes and edges.

        This method performs validation, normalization, and analysis of the graph
        structure to create a complete, executable graph instance.

        Args:
            validate_graph_structure: whether to perform validation of the graph structure
                See the docstring of _validate_graph_structure below for more details.

        Returns:
            A complete Graph instance ready for execution

        Raises:
            ValueError: If the graph structure is invalid (e.g., join without parent fork)
        """
        nodes = self._nodes
        edges_by_source = self._edges_by_source

        nodes, edges_by_source = _replace_placeholder_node_ids(nodes, edges_by_source)
        nodes, edges_by_source = _flatten_paths(nodes, edges_by_source)
        nodes, edges_by_source = _normalize_forks(nodes, edges_by_source)
        if validate_graph_structure:
            _validate_graph_structure(nodes, edges_by_source)
        parent_forks = _collect_dominating_forks(nodes, edges_by_source)
        intermediate_join_nodes = _compute_intermediate_join_nodes(nodes, parent_forks)

        return Graph[StateT, DepsT, GraphInputT, GraphOutputT](
            name=self.name,
            state_type=unpack_type_expression(self.state_type),
            deps_type=unpack_type_expression(self.deps_type),
            input_type=unpack_type_expression(self.input_type),
            output_type=unpack_type_expression(self.output_type),
            nodes=nodes,
            edges_by_source=edges_by_source,
            parent_forks=parent_forks,
            intermediate_join_nodes=intermediate_join_nodes,
            auto_instrument=self.auto_instrument,
        )

```

---|---
####  __init__
```
__init__(
    *,
    name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    state_type: TypeOrTypeExpression[StateT] = NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType"),
    deps_type: TypeOrTypeExpression[DepsT] = NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType"),
    input_type: TypeOrTypeExpression[
        GraphInputT
    ] = NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType"),
    output_type: TypeOrTypeExpression[
        GraphOutputT
    ] = NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType"),
    auto_instrument: bool[](https://docs.python.org/3/library/functions.html#bool) = True
)

```

Initialize a graph builder.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method. |  `None`
`state_type` |  `TypeOrTypeExpression[StateT]` |  The type of the graph state |  `NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType")`
`deps_type` |  `TypeOrTypeExpression[DepsT]` |  The type of the dependencies |  `NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType")`
`input_type` |  `TypeOrTypeExpression[GraphInputT]` |  The type of the graph input data |  `NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType")`
`output_type` |  `TypeOrTypeExpression[GraphOutputT]` |  The type of the graph output data |  `NoneType[](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType")`
`auto_instrument` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  Whether to automatically create instrumentation spans |  `True`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def __init__(
    self,
    *,
    name: str | None = None,
    state_type: TypeOrTypeExpression[StateT] = NoneType,
    deps_type: TypeOrTypeExpression[DepsT] = NoneType,
    input_type: TypeOrTypeExpression[GraphInputT] = NoneType,
    output_type: TypeOrTypeExpression[GraphOutputT] = NoneType,
    auto_instrument: bool = True,
):
    """Initialize a graph builder.

    Args:
        name: Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method.
        state_type: The type of the graph state
        deps_type: The type of the dependencies
        input_type: The type of the graph input data
        output_type: The type of the graph output data
        auto_instrument: Whether to automatically create instrumentation spans
    """
    self.name = name

    self.state_type = state_type
    self.deps_type = deps_type
    self.input_type = input_type
    self.output_type = output_type

    self.auto_instrument = auto_instrument

    self._nodes = {}
    self._edges_by_source = defaultdict(list)
    self._decision_index = 1

    self._start_node = StartNode[GraphInputT]()
    self._end_node = EndNode[GraphOutputT]()

```

---|---
####  name `instance-attribute`
```
name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = name

```

Optional name for the graph, if not provided the name will be inferred from the calling frame on the first call to a graph method.
####  state_type `instance-attribute`
```
state_type: TypeOrTypeExpression[StateT] = state_type

```

The type of the graph state.
####  deps_type `instance-attribute`
```
deps_type: TypeOrTypeExpression[DepsT] = deps_type

```

The type of the dependencies.
####  input_type `instance-attribute`
```
input_type: TypeOrTypeExpression[GraphInputT] = input_type

```

The type of the graph input data.
####  output_type `instance-attribute`
```
output_type: TypeOrTypeExpression[GraphOutputT] = (
    output_type
)

```

The type of the graph output data.
####  auto_instrument `instance-attribute`
```
auto_instrument: bool[](https://docs.python.org/3/library/functions.html#bool) = auto_instrument

```

Whether to automatically create instrumentation spans.
####  start_node `property`
```
start_node: StartNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.StartNode "StartNode \(pydantic_graph.beta.node.StartNode\)")[GraphInputT]

```

Get the start node for the graph.
Returns:
Type | Description
---|---
`StartNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.StartNode "StartNode \(pydantic_graph.beta.node.StartNode\)")[GraphInputT]` |  The start node that receives the initial graph input
####  end_node `property`
```
end_node: EndNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.EndNode "EndNode \(pydantic_graph.beta.node.EndNode\)")[GraphOutputT]

```

Get the end node for the graph.
Returns:
Type | Description
---|---
`EndNode[](https://ai.pydantic.dev/api/pydantic_graph/beta_node/#pydantic_graph.beta.node.EndNode "EndNode \(pydantic_graph.beta.node.EndNode\)")[GraphOutputT]` |  The end node that produces the final graph output
####  step
```
step(
    *, node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None, label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
    [StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT]],
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT],
]

```

```
step(
    call: StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT],
    *,
    node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]

```

```
step(
    call: (
        StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT] | None
    ) = None,
    *,
    node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> (
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]
    | Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
        [StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT]],
        Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT],
    ]
)

```

Create a step from a step function.
This method can be used as a decorator or called directly to create a step node from an async function.
Parameters:
Name | Type | Description | Default
---|---|---|---
`call` |  `StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT] | None` |  The step function to wrap |  `None`
`node_id` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional ID for the node |  `None`
`label` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional human-readable label |  `None`
Returns:
Type | Description
---|---
`Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT] | Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[StepFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepFunction "StepFunction \(pydantic_graph.beta.step.StepFunction\)")[StateT, DepsT, InputT, OutputT]], Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, OutputT]]` |  Either a Step instance or a decorator function
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def step(
    self,
    call: StepFunction[StateT, DepsT, InputT, OutputT] | None = None,
    *,
    node_id: str | None = None,
    label: str | None = None,
) -> (
    Step[StateT, DepsT, InputT, OutputT]
    | Callable[[StepFunction[StateT, DepsT, InputT, OutputT]], Step[StateT, DepsT, InputT, OutputT]]
):
    """Create a step from a step function.

    This method can be used as a decorator or called directly to create
    a step node from an async function.

    Args:
        call: The step function to wrap
        node_id: Optional ID for the node
        label: Optional human-readable label

    Returns:
        Either a Step instance or a decorator function
    """
    if call is None:

        def decorator(
            func: StepFunction[StateT, DepsT, InputT, OutputT],
        ) -> Step[StateT, DepsT, InputT, OutputT]:
            return self.step(call=func, node_id=node_id, label=label)

        return decorator

    node_id = node_id or get_callable_name(call)

    step = Step[StateT, DepsT, InputT, OutputT](id=NodeID(node_id), call=call, label=label)

    return step

```

---|---
####  stream
```
stream(
    *, node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None, label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
    [StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]],
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]],
]

```

```
stream(
    call: StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT],
    *,
    node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]]

```

```
stream(
    call: (
        StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]
        | None
    ) = None,
    *,
    node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> (
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]]
    | Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
        [StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]],
        Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]],
    ]
)

```

```
stream(
    call: (
        StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]
        | None
    ) = None,
    *,
    node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> (
    Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]]
    | Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[
        [StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]],
        Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]],
    ]
)

```

Create a step from an async iterator (which functions like a "stream").
This method can be used as a decorator or called directly to create a step node from an async function.
Parameters:
Name | Type | Description | Default
---|---|---|---
`call` |  `StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT] | None` |  The step function to wrap |  `None`
`node_id` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional ID for the node |  `None`
`label` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional human-readable label |  `None`
Returns:
Type | Description
---|---
`Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]] | Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[StreamFunction[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StreamFunction "StreamFunction \(pydantic_graph.beta.step.StreamFunction\)")[StateT, DepsT, InputT, OutputT]], Step[](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.Step "Step



      dataclass
   \(pydantic_graph.beta.step.Step\)")[StateT, DepsT, InputT, AsyncIterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")[OutputT]]]` |  Either a Step instance or a decorator function
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def stream(
    self,
    call: StreamFunction[StateT, DepsT, InputT, OutputT] | None = None,
    *,
    node_id: str | None = None,
    label: str | None = None,
) -> (
    Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]
    | Callable[
        [StreamFunction[StateT, DepsT, InputT, OutputT]],
        Step[StateT, DepsT, InputT, AsyncIterable[OutputT]],
    ]
):
    """Create a step from an async iterator (which functions like a "stream").

    This method can be used as a decorator or called directly to create
    a step node from an async function.

    Args:
        call: The step function to wrap
        node_id: Optional ID for the node
        label: Optional human-readable label

    Returns:
        Either a Step instance or a decorator function
    """
    if call is None:

        def decorator(
            func: StreamFunction[StateT, DepsT, InputT, OutputT],
        ) -> Step[StateT, DepsT, InputT, AsyncIterable[OutputT]]:
            return self.stream(call=func, node_id=node_id, label=label)

        return decorator

    # We need to wrap the call so that we can call `await` even though the result is an async iterator
    async def wrapper(ctx: StepContext[StateT, DepsT, InputT]):
        return call(ctx)

    node_id = node_id or get_callable_name(call)

    return self.step(call=wrapper, node_id=node_id, label=label)

```

---|---
####  add
```
add(*edges: EdgePath[StateT, DepsT]) -> None

```

Add one or more edge paths to the graph.
This method processes edge paths and automatically creates any necessary fork nodes for broadcasts and maps.
Parameters:
Name | Type | Description | Default
---|---|---|---
`*edges` |  `EdgePath[StateT, DepsT]` |  The edge paths to add to the graph |  `()`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def add(self, *edges: EdgePath[StateT, DepsT]) -> None:  # noqa: C901
    """Add one or more edge paths to the graph.

    This method processes edge paths and automatically creates any necessary
    fork nodes for broadcasts and maps.

    Args:
        *edges: The edge paths to add to the graph
    """

    def _handle_path(p: Path):
        """Process a path and create necessary fork nodes.

        Args:
            p: The path to process
        """
        for item in p.items:
            if isinstance(item, BroadcastMarker):
                new_node = Fork[Any, Any](id=item.fork_id, is_map=False, downstream_join_id=None)
                self._insert_node(new_node)
                for path in item.paths:
                    _handle_path(Path(items=[*path.items]))
            elif isinstance(item, MapMarker):
                new_node = Fork[Any, Any](id=item.fork_id, is_map=True, downstream_join_id=item.downstream_join_id)
                self._insert_node(new_node)
            elif isinstance(item, DestinationMarker):
                pass

    def _handle_destination_node(d: AnyDestinationNode):
        if id(d) in destination_ids:
            return  # prevent infinite recursion if there is a cycle of decisions

        destination_ids.add(id(d))
        destinations.append(d)
        self._insert_node(d)
        if isinstance(d, Decision):
            for branch in d.branches:
                _handle_path(branch.path)
                for d2 in branch.destinations:
                    _handle_destination_node(d2)

    destination_ids = set[int]()
    destinations: list[AnyDestinationNode] = []
    for edge in edges:
        for source_node in edge.sources:
            self._insert_node(source_node)
            self._edges_by_source[source_node.id].append(edge.path)
        for destination_node in edge.destinations:
            _handle_destination_node(destination_node)
        _handle_path(edge.path)

    # Automatically create edges from step function return hints including `BaseNode`s
    for destination in destinations:
        if not isinstance(destination, Step) or isinstance(destination, NodeStep):
            continue
        parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
        type_hints = get_type_hints(destination.call, localns=parent_namespace, include_extras=True)
        try:
            return_hint = type_hints['return']
        except KeyError:
            pass
        else:
            edge = self._edge_from_return_hint(destination, return_hint)
            if edge is not None:
                self.add(edge)

```

---|---
####  add_edge
```
add_edge(
    source: Source[T],
    destination: Destination[T],
    *,
    label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> None

```

Add a simple edge between two nodes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `Source[T]` |  The source node |  _required_
`destination` |  `Destination[T]` |  The destination node |  _required_
`label` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional label for the edge |  `None`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def add_edge(self, source: Source[T], destination: Destination[T], *, label: str | None = None) -> None:
    """Add a simple edge between two nodes.

    Args:
        source: The source node
        destination: The destination node
        label: Optional label for the edge
    """
    builder = self.edge_from(source)
    if label is not None:
        builder = builder.label(label)
    self.add(builder.to(destination))

```

---|---
####  add_mapping_edge
```
add_mapping_edge(
    source: Source[Iterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable")[T]],
    map_to: Destination[T],
    *,
    pre_map_label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    post_map_label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    fork_id: ForkID | None = None,
    downstream_join_id: JoinID | None = None
) -> None

```

Add an edge that maps iterable data across parallel paths.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `Source[Iterable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable")[T]]` |  The source node that produces iterable data |  _required_
`map_to` |  `Destination[T]` |  The destination node that receives individual items |  _required_
`pre_map_label` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional label before the map operation |  `None`
`post_map_label` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional label after the map operation |  `None`
`fork_id` |  `ForkID | None` |  Optional ID for the fork node produced for this map operation |  `None`
`downstream_join_id` |  `JoinID | None` |  Optional ID of a join node that will always be downstream of this map. Specifying this ensures correct handling if you try to map an empty iterable. |  `None`
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def add_mapping_edge(
    self,
    source: Source[Iterable[T]],
    map_to: Destination[T],
    *,
    pre_map_label: str | None = None,
    post_map_label: str | None = None,
    fork_id: ForkID | None = None,
    downstream_join_id: JoinID | None = None,
) -> None:
    """Add an edge that maps iterable data across parallel paths.

    Args:
        source: The source node that produces iterable data
        map_to: The destination node that receives individual items
        pre_map_label: Optional label before the map operation
        post_map_label: Optional label after the map operation
        fork_id: Optional ID for the fork node produced for this map operation
        downstream_join_id: Optional ID of a join node that will always be downstream of this map.
            Specifying this ensures correct handling if you try to map an empty iterable.
    """
    builder = self.edge_from(source)
    if pre_map_label is not None:
        builder = builder.label(pre_map_label)
    builder = builder.map(fork_id=fork_id, downstream_join_id=downstream_join_id)
    if post_map_label is not None:
        builder = builder.label(post_map_label)
    self.add(builder.to(map_to))

```

---|---
####  edge_from
```
edge_from(
    *sources: Source[SourceOutputT],
) -> EdgePathBuilder[StateT, DepsT, SourceOutputT]

```

Create an edge path builder starting from the given source nodes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`*sources` |  `Source[SourceOutputT]` |  The source nodes to start the edge path from |  `()`
Returns:
Type | Description
---|---
`EdgePathBuilder[StateT, DepsT, SourceOutputT]` |  An EdgePathBuilder for constructing the complete edge path
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def edge_from(self, *sources: Source[SourceOutputT]) -> EdgePathBuilder[StateT, DepsT, SourceOutputT]:
    """Create an edge path builder starting from the given source nodes.

    Args:
        *sources: The source nodes to start the edge path from

    Returns:
        An EdgePathBuilder for constructing the complete edge path
    """
    return EdgePathBuilder[StateT, DepsT, SourceOutputT](
        sources=sources, path_builder=PathBuilder(working_items=[])
    )

```

---|---
####  decision
```
decision(
    *, note: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None, node_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None
) -> Decision[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.Decision "Decision



      dataclass
   \(pydantic_graph.beta.decision.Decision\)")[StateT, DepsT, Never[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Never "typing_extensions.Never")]

```

Create a new decision node.
Parameters:
Name | Type | Description | Default
---|---|---|---
`note` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional note to describe the decision logic |  `None`
`node_id` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Optional ID for the node produced for this decision logic |  `None`
Returns:
Type | Description
---|---
`Decision[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.Decision "Decision



      dataclass
   \(pydantic_graph.beta.decision.Decision\)")[StateT, DepsT, Never[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Never "typing_extensions.Never")]` |  A new Decision node with no branches
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
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
```
| ```
def decision(self, *, note: str | None = None, node_id: str | None = None) -> Decision[StateT, DepsT, Never]:
    """Create a new decision node.

    Args:
        note: Optional note to describe the decision logic
        node_id: Optional ID for the node produced for this decision logic

    Returns:
        A new Decision node with no branches
    """
    return Decision(id=NodeID(node_id or generate_placeholder_node_id('decision')), branches=[], note=note)

```

---|---
####  match
```
match(
    source: TypeOrTypeExpression[SourceT],
    *,
    matches: Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")], bool[](https://docs.python.org/3/library/functions.html#bool)] | None = None
) -> DecisionBranchBuilder[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranchBuilder "DecisionBranchBuilder



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranchBuilder\)")[
    StateT, DepsT, SourceT, SourceT, Never[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Never "typing_extensions.Never")
]

```

Create a decision branch matcher.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `TypeOrTypeExpression[SourceT]` |  The type or type expression to match against |  _required_
`matches` |  `Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")], bool[](https://docs.python.org/3/library/functions.html#bool)] | None` |  Optional custom matching function |  `None`
Returns:
Type | Description
---|---
`DecisionBranchBuilder[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranchBuilder "DecisionBranchBuilder



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranchBuilder\)")[StateT, DepsT, SourceT, SourceT, Never[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Never "typing_extensions.Never")]` |  A DecisionBranchBuilder for constructing the branch
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def match(
    self,
    source: TypeOrTypeExpression[SourceT],
    *,
    matches: Callable[[Any], bool] | None = None,
) -> DecisionBranchBuilder[StateT, DepsT, SourceT, SourceT, Never]:
    """Create a decision branch matcher.

    Args:
        source: The type or type expression to match against
        matches: Optional custom matching function

    Returns:
        A DecisionBranchBuilder for constructing the branch
    """
    # Note, the following node_id really is just a placeholder and shouldn't end up in the final graph
    # This is why we don't expose a way for end users to override the value used here.
    node_id = NodeID(generate_placeholder_node_id('match_decision'))
    decision = Decision[StateT, DepsT, Never](id=node_id, branches=[], note=None)
    new_path_builder = PathBuilder[StateT, DepsT, SourceT](working_items=[])
    return DecisionBranchBuilder(decision=decision, source=source, matches=matches, path_builder=new_path_builder)

```

---|---
####  match_node
```
match_node(
    source: type[](https://docs.python.org/3/library/functions.html#type)[SourceNodeT],
    *,
    matches: Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")], bool[](https://docs.python.org/3/library/functions.html#bool)] | None = None
) -> DecisionBranch[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranch "DecisionBranch



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranch\)")[SourceNodeT]

```

Create a decision branch for BaseNode subclasses.
This is similar to match() but specifically designed for matching against BaseNode types from the v1 system.
Parameters:
Name | Type | Description | Default
---|---|---|---
`source` |  `type[](https://docs.python.org/3/library/functions.html#type)[SourceNodeT]` |  The BaseNode subclass to match against |  _required_
`matches` |  `Callable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")[[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")], bool[](https://docs.python.org/3/library/functions.html#bool)] | None` |  Optional custom matching function |  `None`
Returns:
Type | Description
---|---
`DecisionBranch[](https://ai.pydantic.dev/api/pydantic_graph/beta_decision/#pydantic_graph.beta.decision.DecisionBranch "DecisionBranch



      dataclass
   \(pydantic_graph.beta.decision.DecisionBranch\)")[SourceNodeT]` |  A DecisionBranch for the BaseNode type
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def match_node(
    self,
    source: type[SourceNodeT],
    *,
    matches: Callable[[Any], bool] | None = None,
) -> DecisionBranch[SourceNodeT]:
    """Create a decision branch for BaseNode subclasses.

    This is similar to match() but specifically designed for matching
    against BaseNode types from the v1 system.

    Args:
        source: The BaseNode subclass to match against
        matches: Optional custom matching function

    Returns:
        A DecisionBranch for the BaseNode type
    """
    node = NodeStep(source)
    path = Path(items=[DestinationMarker(node.id)])
    return DecisionBranch(source=source, matches=matches, path=path, destinations=[node])

```

---|---
####  node
```
node(
    node_type: type[](https://docs.python.org/3/library/functions.html#type)[BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, GraphOutputT]],
) -> EdgePath[StateT, DepsT]

```

Create an edge path from a BaseNode class.
This method integrates v1-style BaseNode classes into the v2 graph system by analyzing their type hints and creating appropriate edges.
Parameters:
Name | Type | Description | Default
---|---|---|---
`node_type` |  `type[](https://docs.python.org/3/library/functions.html#type)[BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode \(pydantic_graph.nodes.BaseNode\)")[StateT, DepsT, GraphOutputT]]` |  The BaseNode subclass to integrate |  _required_
Returns:
Type | Description
---|---
`EdgePath[StateT, DepsT]` |  An EdgePath representing the node and its connections
Raises:
Type | Description
---|---
`GraphSetupError[](https://ai.pydantic.dev/api/pydantic_graph/exceptions/#pydantic_graph.exceptions.GraphSetupError "GraphSetupError \(pydantic_graph.exceptions.GraphSetupError\)")` |  If the node type is missing required type hints
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
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
```
| ```
def node(
    self,
    node_type: type[BaseNode[StateT, DepsT, GraphOutputT]],
) -> EdgePath[StateT, DepsT]:
    """Create an edge path from a BaseNode class.

    This method integrates v1-style BaseNode classes into the v2 graph
    system by analyzing their type hints and creating appropriate edges.

    Args:
        node_type: The BaseNode subclass to integrate

    Returns:
        An EdgePath representing the node and its connections

    Raises:
        GraphSetupError: If the node type is missing required type hints
    """
    parent_namespace = _utils.get_parent_namespace(inspect.currentframe())
    type_hints = get_type_hints(node_type.run, localns=parent_namespace, include_extras=True)
    try:
        return_hint = type_hints['return']
    except KeyError as e:  # pragma: no cover
        raise exceptions.GraphSetupError(
            f'Node {node_type} is missing a return type hint on its `run` method'
        ) from e

    node = NodeStep(node_type)

    edge = self._edge_from_return_hint(node, return_hint)
    if not edge:  # pragma: no cover
        raise exceptions.GraphSetupError(f'Node {node_type} is missing a return type hint on its `run` method')

    return edge

```

---|---
####  build
```
build(
    validate_graph_structure: bool[](https://docs.python.org/3/library/functions.html#bool) = True,
) -> Graph[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.Graph "Graph



      dataclass
   \(pydantic_graph.beta.graph.Graph\)")[StateT, DepsT, GraphInputT, GraphOutputT]

```

Build the final executable graph from the accumulated nodes and edges.
This method performs validation, normalization, and analysis of the graph structure to create a complete, executable graph instance.
Parameters:
Name | Type | Description | Default
---|---|---|---
`validate_graph_structure` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  whether to perform validation of the graph structure See the docstring of _validate_graph_structure below for more details. |  `True`
Returns:
Type | Description
---|---
`Graph[](https://ai.pydantic.dev/api/pydantic_graph/beta_graph/#pydantic_graph.beta.graph.Graph "Graph



      dataclass
   \(pydantic_graph.beta.graph.Graph\)")[StateT, DepsT, GraphInputT, GraphOutputT]` |  A complete Graph instance ready for execution
Raises:
Type | Description
---|---
`ValueError[](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the graph structure is invalid (e.g., join without parent fork)
Source code in `pydantic_graph/pydantic_graph/beta/graph_builder.py`
```
638
639
640
641
642
643
644
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
667
668
669
670
671
672
673
674
675
676
```
| ```
def build(self, validate_graph_structure: bool = True) -> Graph[StateT, DepsT, GraphInputT, GraphOutputT]:
    """Build the final executable graph from the accumulated nodes and edges.

    This method performs validation, normalization, and analysis of the graph
    structure to create a complete, executable graph instance.

    Args:
        validate_graph_structure: whether to perform validation of the graph structure
            See the docstring of _validate_graph_structure below for more details.

    Returns:
        A complete Graph instance ready for execution

    Raises:
        ValueError: If the graph structure is invalid (e.g., join without parent fork)
    """
    nodes = self._nodes
    edges_by_source = self._edges_by_source

    nodes, edges_by_source = _replace_placeholder_node_ids(nodes, edges_by_source)
    nodes, edges_by_source = _flatten_paths(nodes, edges_by_source)
    nodes, edges_by_source = _normalize_forks(nodes, edges_by_source)
    if validate_graph_structure:
        _validate_graph_structure(nodes, edges_by_source)
    parent_forks = _collect_dominating_forks(nodes, edges_by_source)
    intermediate_join_nodes = _compute_intermediate_join_nodes(nodes, parent_forks)

    return Graph[StateT, DepsT, GraphInputT, GraphOutputT](
        name=self.name,
        state_type=unpack_type_expression(self.state_type),
        deps_type=unpack_type_expression(self.deps_type),
        input_type=unpack_type_expression(self.input_type),
        output_type=unpack_type_expression(self.output_type),
        nodes=nodes,
        edges_by_source=edges_by_source,
        parent_forks=parent_forks,
        intermediate_join_nodes=intermediate_join_nodes,
        auto_instrument=self.auto_instrument,
    )

```

---|---
© Pydantic Services Inc. 2024 to present
