ENVIRONMENT = prod
SRC_DIR = rota

install:
	poetry install $(test ${ENVIRONMENT} != "dev" && echo "--no-dev")

bandit:
	poetry run bandit --format txt --recursive ${SRC_DIR}

mypy:
	poetry run mypy ${SRC_DIR}

pylint:
	poetry run pylint ${SRC_DIR}

static-analysis: bandit mypy pylint

tests-unit:
	poetry run pytest tests/unit/

tests-coverage:
	poetry run pytest --cov-report term-missing --cov-fail-under=90 --cov=${SRC_DIR} tests/unit