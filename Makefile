.DEFAULT_GOAL=help

.PHONY: help hello venv install check clean build upload update

VENV_DIR = .venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
TOX = $(VENV_DIR)/bin/tox
PRE_COMMIT = $(VENV_DIR)/bin/pre-commit

# Check if virtual environment is activated
define check_venv
	@ if [ "$$($(PYTHON) -c 'import sys; print(sys.prefix)')" != "$(CURDIR)/$(VENV_DIR)" ]; then \
		echo "Error: Virtual environment not activated. Please create or activate the virtual environment."; \
		exit 1; \
	fi
endef

help: ## Display this help message with available make commands.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

hello: ## Display a welcome message for contributors.
	@echo "Your face show, your shoe shine. Thank you for contributing to Fakernaija. E go better for you!"

venv: ## Create a virtual environment for project isolation.
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created."
	@echo "Activate with the command 'source $(VENV_DIR)/bin/activate'"

install: ## Install project dependencies for development.
	$(call check_venv)
	$(PIP) install --upgrade pip setuptools
	$(PIP) install -e .[dev]
	@echo "Successfully installed development packages."

check: ## Run code quality checks
	$(call check_venv)
	$(TOX)
	$(PRE_COMMIT) install
	$(PRE_COMMIT) run --all-files
	@echo "All checks passed"

build: ## Build the project source and wheel distribution.
	$(call check_venv)
	$(PYTHON) -m pip install --upgrade build
	@rm -rf dist
	$(PYTHON) -m build
	@echo "Package built successfully."

upload: ## Upload the project to PyPI.
	$(call check_venv)
	$(PYTHON) -m pip install --upgrade twine
	$(PYTHON) -m twine upload dist/*
	@echo "Package uploaded to PyPI."

update: build upload ## Build and upload the project in one command.

clean: ## Remove generated files and directories to reset the project state.
	@echo "Cleaning up the project of generated files and directories..."
	@rm -rf $(VENV_DIR)
	@rm -rf .cache
	@rm -rf htmlcov coverage.xml .coverage
	@rm -rf .tox
	@rm -rf .mypy_cache
	@rm -rf .ruff_cache
	@rm -rf *.egg-info
	@rm -rf dist
	@find . -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "Clean up successfully completed."
