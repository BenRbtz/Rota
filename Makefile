install-dev:
	poetry install

install:
	poetry install --no-dev

test-unit: install-dev
	poetry run pytest