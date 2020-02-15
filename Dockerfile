FROM python:3.8-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.3

RUN groupadd -g 999 app && \
    useradd -r -u 999 -g app app

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY Makefile poetry.lock pyproject.toml /app/
COPY rota /app/rota/

RUN make install

USER app

ENTRYPOINT ["python", "-m", "rota.adapters.driver.app"]