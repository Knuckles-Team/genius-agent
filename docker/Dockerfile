# syntax=docker/dockerfile:1
# Slim multi-stage build: install in a builder, ship only /usr/local. Cuts the
# pushed image ~43% (no default-jre/dev-tools/source) so layer pushes finish well
# inside the registry's blob-upload window even under concurrency.
FROM python:3.14-slim@sha256:cea0e6040540fb2b965b6e7fb5ffa00871e632eef63719f0ea54bca189ce14a6 AS builder
COPY --from=ghcr.io/astral-sh/uv:0.11.7@sha256:240fb85ab0f263ef12f492d8476aa3a2e4e1e333f7d67fbdd923d00a506a516a /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_SYSTEM_PYTHON=1 \
    UV_HTTP_TIMEOUT=3600
# Some [all] deps (e.g. hnswlib, an agent-connector-sdk transitive) ship no manylinux
# wheel and build from sdist, needing a C++ toolchain. Install it in the builder
# only — the final stage copies just /usr/local, so no compiler ships.
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --upgrade --break-system-packages genius-agent[mcp]==4.2.0
