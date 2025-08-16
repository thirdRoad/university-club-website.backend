FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry install

CMD ["sh", "-c", "poetry run python src/manage.py migrate && poetry run python src/manage.py runserver 0.0.0.0:8000"]
