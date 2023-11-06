FROM python3.11:slim AS base
RUN apt update && apt upgrade -y && pip install --upgrade pip
COPY ./agent_constructs.py ./agent_functions ./genius_agent_api.py ./requirements.txt /
RUN pip install -r /requirements.txt
CMD ["uvicorn", "genius_agent_api:app", "--reload", "--host", "0.0.0.0", "--port", "7999"]