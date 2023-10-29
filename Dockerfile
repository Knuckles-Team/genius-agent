FROM python3.11:slim AS base
RUN apt update && apt upgrade -y && pip install --upgrade pip
COPY . /
RUN pip install -r /requirements.txt
