FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY wait-for-it.sh /wait-for-it.sh

RUN chmod +x /wait-for-it.sh
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
