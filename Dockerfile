FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY muzaic_mcp/ ./muzaic_mcp/

RUN pip install --no-cache-dir .

RUN adduser --disabled-password --gecos "" mcpuser
USER mcpuser

ENTRYPOINT ["muzaic-mcp"]
