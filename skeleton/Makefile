VIRTUALENV_DIR := .venv
ACTIVATE := $(VIRTUALENV_DIR)/bin/activate

# one time environment prep and dependency installation for development
env: $(ACTIVATE)

$(ACTIVATE): setup.py pyproject.toml
	@echo "Updating/installing virtual environment and dependencies..."
	@test -d $(VIRTUALENV_DIR) || python3 -m venv $(VIRTUALENV_DIR)
	@. $(ACTIVATE); pip install -U pip
	@. $(ACTIVATE); pip install -U pre-commit
	@. $(ACTIVATE); pip install -U -e ".[dev]"
	@. $(ACTIVATE); pre-commit install
	@echo "installation complete.  Type:   . '$(ACTIVATE)' to work interactively"
	@touch $(ACTIVATE)

# run unit/other tests
test: env
	@echo "Running tests and sanity checks..."
	@. $(ACTIVATE); pytest tests/
	# could add other C/C++ testing here

# execute automatic formatting and other code style/complexity checks.
lint: env
	@echo "running various checks..."
	@. $(ACTIVATE); pre-commit run --all-files

# cleanup any installed files
clean:
	@echo "Cleaning up created files..."
	@rm -rf $(VIRTUALENV_DIR)


.phony: env test lint clean
