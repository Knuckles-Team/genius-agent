FROM python:3.11.6-slim-bookworm AS base
RUN apt update && apt upgrade -y && pip install --upgrade pip
COPY ./genius_agent /
WORKDIR /genius_agent
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
CMD ["uvicorn", "genius_agent_api:app", "--reload", "--host", "0.0.0.0", "--port", "7999"]