PYTHON_VERSION = "python3.8"
ENV = "prod"

install:
	poetry env use ${PYTHON_VERSION}
	poetry install $(test ${ENV} != "dev" && echo "--no-dev")

tests-unit:
	poetry run pytest tests/unit/