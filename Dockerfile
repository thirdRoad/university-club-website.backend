FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl
RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-root

COPY src /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
