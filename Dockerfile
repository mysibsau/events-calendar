FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install pipenv
COPY Pipfile* /
RUN pipenv install --dev --deploy --system --ignore-pipfile

COPY src /app
