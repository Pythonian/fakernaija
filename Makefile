.DEFAULT_GOAL=help

.PHONY: help hello venv install docs check clean

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
	@echo "Hey, $(USER)! Your face show, your shoe shine. Thank you for contributing to Fakernaija. E go better for you!"

venv: ## Create a virtual environment.
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created."
	@echo "Activate with the command 'source $(VENV_DIR)/bin/activate'"

install: ## Install local development dependencies.
	$(call check_venv)
	$(PIP) install -U pip setuptools pre-commit tox
	$(PIP) install -e .
	$(PIP) install -r docs/requirements.txt
	$(PRE_COMMIT) install
	@echo "Development dependencies installed."

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

clean: ## Clean up all generated files and directories.
	@echo "Cleaning up the project..."
	@rm -rf $(VENV_DIR) .cache htmlcov coverage.xml .coverage
	@rm -rf .tox .mypy_cache .ruff_cache *.egg-info dist build
	@find . -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type d -name "build" -exec rm -rf {} +
	@echo "Cleanup completed."
