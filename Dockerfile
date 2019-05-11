FROM python:3.7-slim-stretch

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=0.12.12

RUN groupadd -g 999 app && \
    useradd -r -u 999 -g app app

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY service /app/service/

RUN poetry config settings.virtualenvs.create false \
    && poetry build \
    && pip install dist/*.whl \
    && rm dist -rf

USER app

ENTRYPOINT ["python", "-m", "service.app"]