# Ambiq standard project skeleton

[![tests](https://github.com/AmbiqAI/CHANGE_ME/actions/workflows/tests.yml/badge.svg)](https://github.com/AmbiqAI/CHANGE_ME/actions/workflows/tests.yml)

Provides a cohesive starting point for each Ambiq AI derived repository.

It is of course expected that you will update and modify this to fit your
needs!  At an absolute minimum, find and replace any instance of `CHANGE_ME`you
come across! :)


## Directory Layout

```
.
+-- README.md  # this file
+-- pyproject.toml  # python project configuration file
+-- setup.py  # python setup script
+-- Makefile  # top-level command driver controlling building/running etc.
+-- /checkpoints   # saved trained models
+-- /configs  # configuration settings files
+-- /datasets  # raw and derived datasets used as input to training/testing
+-- /docs  # additional documentation files
+-- /evb  # C code for deployment/inference on microcontroller devices
+-- /notebooks  # jupyter notebook walkthroughs
+-- /python   # python source code for training/inference
+-- /tests   # unit and other test related code
```

## Some Useful Commands
```
sed -i 's/CHANGE_ME/<your_repo_name>/g' *
```
run this once from this directory replacing the text `<your_repo_name>` with
the name of your project.
This will update some of the setup scripts and ensure you build a python
project with the name of your repo.

```
make env
```
This will setup a python virtual environment in this directory and ensure
necessary dependencies for things like linting and running python tests
are installed.  This should only need to be run one time.

```
make test
```
Execute any configured tests

```
make lint
```
Execute a set of automatic code formatting and type/style/complexity checks.
This will automatically be run any time you attempt to commit changes to a
git repository.

```
make clean
```
Cleanup any created pytohn virtual environments and other files.
