FROM python:3.7.1-alpine as app

RUN mkdir /app

WORKDIR /app

RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash

COPY requirements/src.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

COPY src /app/src/

COPY app.py setup.py /app/

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["python", "app.py"]


FROM app as tests

COPY requirements/tests.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

COPY tests /app/tests/