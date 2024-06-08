# make-management-command

[![Tests](https://github.com/frankwiles/make-management-command/actions/workflows/test.yml/badge.svg)](https://github.com/frankwiles/make-management-command/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-bsd-3.svg)](https://github.com/frankwiles/make-management-command/blob/master/LICENSE)

Create the proper paths and a base django-click command.  Django management commands are a
useful and powerful way to make easy-to-use command line tools for your Django project.

However, Django assumes your commands live in Python files in a very specific file system
layout relative to your Django app.  Specifically, they need to live in `<app_name>/management/commands/`
and each of these folders needs an empty `__init__.py`.

Frankly, I'm too old to be bothered to manually create this structure on at least a weekly basis so
I built this little utility to do it for me.  It will create the paths, empty `__init__.py` files and
X number of very simple [django-click](https://pypi.org/project/django-click/) commands based on the names I pass as arguments.

Without any arguments, it will simply create the proper path structure for you.

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

Just create the path structure:
```bash
make-management-command
```

Create two commands named `foo` and `bar`:
```bash
make-management-command foo bar
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
