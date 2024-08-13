.DEFAULT_GOAL=help

.PHONY: help hello venv install install-dev install-build docs check build upload update clean

VENV_DIR = .venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
TOX = $(VENV_DIR)/bin/tox
PRE_COMMIT = $(VENV_DIR)/bin/pre-commit

# Check if virtual environment is activated
define check_venv
	@ if [ "$$($(PYTHON) -c 'import sys; print(sys.prefix)')" != "$(CURDIR)/$(VENV_DIR)" ]; then \
		echo "Error: Virtual environment not activated. Please activate or create one."; \
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

install-dev: ## Install local development dependencies.
	$(call check_venv)
	$(PIP) install -U pip setuptools
	$(PIP) install -e .[dev]
	$(PIP) install -r docs/requirements.txt
	$(PRE_COMMIT) install
	@echo "Development dependencies installed."

install-build: ## Install project distribution dependencies.
	$(call check_venv)
	$(PIP) install -U build twine
	@echo "Build dependencies installed."

install: install-dev install-build ## Install all dependencies with one command.

docs: ## Generate project HTML documentation using Sphinx.
	$(call check_venv)
	@rm -rf docs/build
	@sphinx-build -M html docs/source/ docs/build/
	@echo "Project documentation successfully built."

check: ## Run code quality checks with Tox and Pre-commit
	$(call check_venv)
	$(TOX)
	$(PRE_COMMIT) run --all-files
	@echo "All checks passed"

build: ## Build the project source and wheel distribution.
	$(call check_venv)
	@rm -rf dist
	$(PYTHON) -m build
	@echo "Package built successfully."

upload: ## Upload the project to PyPI.
	$(call check_venv)
	$(PYTHON) -m twine upload dist/*
	@echo "Package uploaded to PyPI."

update: build upload ## Build and upload the project to PyPI in one command.

clean: ## Clean up all generated files and directories.
	@echo "Cleaning up the project..."
	@rm -rf $(VENV_DIR)
	@rm -rf .cache
	@rm -rf htmlcov coverage.xml .coverage
	@rm -rf .tox
	@rm -rf .mypy_cache
	@rm -rf .ruff_cache
	@rm -rf *.egg-info
	@rm -rf dist
	@find . -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name "build" -exec rm -rf {} +
	@echo "Cleanup completed."
