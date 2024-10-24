.PHONY: format check test

format:
	ruff format .

check:
	ruff check --select I --fix

test:
	pytest tests

# You can combine format and check into a single command if desired:
lint: format check