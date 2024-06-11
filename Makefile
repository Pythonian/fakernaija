# Makefile for setting up the fakernaija project

.DEFAULT_GOAL=help

# Define commands to be explicitly invoked
.PHONY: all venv install tox clean help hello docs

# Define the name of the virtual environment directory
VENV_DIR = .venv

# Define the python command for creating virtual environments
PYTHON = python3

# Define the pip executable within the virtual environment
PIP = $(VENV_DIR)/bin/pip

# Define the tox executable within the virtual environment
TOX = $(VENV_DIR)/bin/tox

# Define the command to install the pre-commit setup
PRE_COMMIT = $(VENV_DIR)/bin/pre-commit

# Help command to show usage instructions
help: ## Show this help
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all                Setup a complete development environment and run checks"
	@echo "  venv               Create a virtual environment"
	@echo "  install            Install development packages and pre-commit hooks"
	@echo "  tox                Run all checks using tox"
	@echo "  clean              Clean the project of unneeded files"
	@echo "  docs				Build sphinx documentation"
	@echo "  hello              Read our welcome note"
	@echo "  help               Show this help message"

hello: ## Read our welcome note
	@echo "Welcome to FakerNaija! Let's make Nigeria proud with awesome fake data. Enjoy your coding journey!"

# Setup the development environment
all: venv install tox docs

venv: ## Create a virtual environment
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created."
	@echo "Activate with the command 'source .venv/bin/activate'"

install: ## Install development packages
	$(PIP) install --upgrade pip
	$(PIP) install tox==4.15.0 pre-commit==3.7.1
	$(PRE_COMMIT) install
	@echo "Development packages and pre-commit hooks installed"

docs: ## Build sphinx documentation
	$(PIP) install sphinx==7.3.7 sphinx-rtd-theme==2.0.0
	$(PIP) install -e .
	@sphinx-build -M html docs/source/ docs/build/
	@echo "Project documentation successfully built."

tox: ## Run all checks using tox
	$(TOX)
	@echo "All checks passed"

clean: ## Clean the project of unneeded files
	@echo "Cleaning up the project of unneeded files..."
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
