# Ambiq standard project skeleton

[![tests](https://github.com/AmbiqAI/change_me/actions/workflows/tests.yml/badge.svg)](https://github.com/AmbiqAI/change_me/actions/workflows/tests.yml)

Provides a cohesive starting point for each Ambiq AI derived repository.

It is of course expected that you will update and modify this to fit your needs! At an absolute minimum, find and replace any instance of `change_me` you come across! :)

## Directory Layout

```bash
.
├── README.md  # this file
├── pyproject.toml  # python project configuration file
├── Makefile  # top-level command driver controlling building/running etc.
├── /checkpoints   # saved trained models
├── /configs  # configuration settings files
├── /datasets  # raw and derived datasets used as input to training/testing
├── /docs  # additional documentation files
├── /evb  # C code for deployment/inference on microcontroller devices
├── /notebooks  # jupyter notebook walkthroughs
├── /python   # python source code for training/inference
└── /tests   # unit and other test related code
```

## Python Environment

For managing the Python environment we are leveraging [Poetry](https://python-poetry.org) - _a Python packaging and dependency management tool similar to `npm` and `yarn`_. Poetry removes the need for having a `requirements.txt` and `setup.py` file. Instead all python configurations are managed via [pyproject.toml](https://python-poetry.org/docs/pyproject/). To setup the virtual environment and install project dependencies, we run `poetry install`. To add a new package, we run `poetry add new_package`. Poetry also ensures proper dependency version resolution. Poetry creates a `poetry.lock` file that tracks specific versions and ensure reproducible installs between developers. This lock file should be source controlled and should not be manually edited. To ensure lock file is up to date, we can run `poetry lock`.

## Some Useful Commands

```bash
sed -i 's/change_me/<your_repo_name>/g' *
mv python/change_me python/<your_repo_name>
```

Run this once from this directory replacing the text `<your_repo_name>` with the name of your project. This will update some of the setup scripts and ensure you build a python project with the name of your repo.

```bash
make env
```

This will setup a python virtual environment in this directory and ensure necessary dependencies for things like linting and running python tests are installed. This should only need to be run one time.

```bash
poetry shell
```

Activate the python environment.

```bash
make test
```

Execute any configured tests.

```bash
make lint
```

Execute a set of automatic code formatting and type/style/complexity checks. This will automatically be run any time you attempt to commit changes to a git repository.

```bash
make clean
```

Clean up any created python virtual environments and other files.
