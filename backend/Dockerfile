FROM python:3.12-slim AS builder

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1

# to run poetry directly as soon as it's installed
ENV PATH="$POETRY_HOME/bin:$PATH"

# install poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

# copy only pyproject.toml and poetry.lock to cache dependencies
COPY poetry.lock pyproject.toml ./

# this will create the folder /app/.venv (might need adjustment depending on which poetry version you are using)
RUN poetry install --no-root --no-ansi

# ---------------------------------------------------------------------

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# copy the venv folder from builder image 
COPY --from=builder /app/.venv ./.venv

# COPY secrets/.env secrets/.env
COPY prompt.txt .
COPY *.py .
COPY roboto.ttf .

EXPOSE 8000

CMD ["/app/.venv/bin/python3", "main.py"]
