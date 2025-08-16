FROM python:3.12-slim

WORKDIR /app

COPY wait-for-it.sh ./
RUN chmod +x ./wait-for-it.sh

COPY . .

RUN pip install poetry
RUN poetry install

CMD [ "/app/wait-for-it.sh", "postgres:5432", "--", "sh", "-c", "poetry run python src/manage.py migrate && poetry run python src/manage.py runserver 0.0.0.0:8000" ]
