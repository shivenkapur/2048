# Project 2048

## Setup

### Create a new virtual environment

1. Run `python -m venv venv`
2. Run `source venv/bin/activate`

### Install dev dependencies

`pip install -e ".[dev]"`

### Or Install build only dependencies

`pip install .`

## Quality Checks

### Run tests

Run `python -m pytest`

### Flake8

Run `flake8 ./src/`

### Mypy

Run `mypy .`

## Play Game

1. [Optional] export your hugging face api key as an env variable for getting AI suggestions `export HUGGING_FACE_KEY={value}`
2. Run `python ./src/main.py`
3. Use the left, down, up or down arrow keys to pla your next move (no need to press enter)
4. Press a to ask AI for a recommendation. Wait for a bit to a get a response.

## To do

1. Improve test coverage for AI response
2. Refactor \_merge function in merge_algorithm to make intent clearer for each state
3. Improve test coverage for algorithm and add unit test coverage check
