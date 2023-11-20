FROM python:3.11.6-slim-bookworm AS base
RUN apt update && apt upgrade -y && pip install --upgrade pip
RUN pip install --upgrade genius-agent[rag,openai,chromadb,pgvector,api,memgpt]
#COPY ./genius_agent /
#WORKDIR /genius_agent
#COPY ./requirements_core.txt ./requirements_api.txt ./requirements_chromadb.txt ./requirements_core.txt \
#     ./requirements_lmm.txt ./requirements_memgpt.txt ./requirements_openai.txt ./requirements_pgvector.txt \
#     ./requirements_rag.txt /
#RUN pip install -r ./requirements_core.txt \
#    && pip install -r ./requirements_api.txt \
#    && pip install -r ./requirements_chromadb.txt \
#    && pip install -r ./requirements_core.txt \
#    && pip install -r ./requirements_lmm.txt \
#    && pip install -r ./requirements_memgpt.txt \
#    && pip install -r ./requirements_openai.txt \
#    && pip install -r ./requirements_pgvector.txt
CMD ["uvicorn", "genius_agent_api:app", "--reload", "--host", "0.0.0.0", "--port", "7999"]