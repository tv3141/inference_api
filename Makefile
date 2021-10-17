SHELL := /bin/bash
VENV="venv"

.PHONY: install
install:
	python -m venv $(VENV)
	./$(VENV)/bin/pip install \
		--upgrade pip \
		--requirement requirements.txt \
		--no-cache
	source ./$(VENV)/bin/activate
	pip install -e .

.PHONY: install-test
install-test:
	python -m venv $(VENV)
	./$(VENV)/bin/pip install \
		--upgrade pip \
		--requirement requirements.txt \
		--requirement requirements_dev.txt
	source ./$(VENV)/bin/activate
	pip install -e .

.PHONY: test
test:
	./$(VENV)/bin/python -m pytest tests
