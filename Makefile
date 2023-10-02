# Makefile
.PHONY: checks test unittest

help:
	@echo "checks - Runs isort/black/flake8/mypy"
	@echo "test - Runs pytest with full cov"
	@echo "unittest - Runs pytest with no cov"

checks:
	poetry run isort --diff .
	poetry run black --check .
	poetry run flake8
	poetry run mypy

test:
	poetry run pytest --cov --cov-fail-under=100

unittest:
	poetry run pytest -vv --no-cov