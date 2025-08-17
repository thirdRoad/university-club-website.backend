FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry
RUN poetry install --no-root

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
