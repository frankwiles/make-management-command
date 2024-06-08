# make-management-command

[![PyPI](https://img.shields.io/pypi/v/make-management-command.svg)](https://pypi.org/project/make-management-command/)
[![Changelog](https://img.shields.io/github/v/release/frankwiles/make-management-command?include_prereleases&label=changelog)](https://github.com/frankwiles/make-management-command/releases)
[![Tests](https://github.com/frankwiles/make-management-command/actions/workflows/test.yml/badge.svg)](https://github.com/frankwiles/make-management-command/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/frankwiles/make-management-command/blob/master/LICENSE)

Create the proper paths and a base django-click command

## Installation

Install this tool using `pip`:
```bash
pip install https://github.com/frankwiles/make-management-command
```
## Usage

For help, run:
```bash
make-management-command --help
```

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

```bash
cd make-management-command
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
pytest
```
