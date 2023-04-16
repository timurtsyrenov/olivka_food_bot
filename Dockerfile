FROM python:3.9-slim

WORKDIR /olivka_food_bot

RUN apt update && \
    pip install --upgrade pip && \
    pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create false

COPY pyproject.toml /olivka_food_bot
COPY poetry.lock /olivka_food_bot

RUN poetry install

COPY . /olivka_food_bot
