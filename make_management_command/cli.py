import os

import click


def green(message: str, nl=True):
    click.secho(message, nl=nl, fg="green")


def yellow(message: str, nl=True):
    click.secho(message, nl=nl, fg="yellow")


def red(message: str, nl=True):
    click.secho(message, nl=nl, fg="red")


def build_path(base_path: str) -> None:
    """
    Determine if there already exists a directory path that looks like
    `./management/commands/` which also contains the proper `__init__.py` files.
    If not, correct that as we go.
    """
    green("Checking for ./management/commands/ directory...", nl=False)

    if not os.path.exists(os.path.join(base_path, "management", "commands")):
        os.makedirs(os.path.join(base_path, "management", "commands"), exist_ok=True)
        green("created.")
    else:
        yellow("exists.")

    inits = [
        os.path.join(base_path, "management", "__init__.py"),
        os.path.join(base_path, "management", "commands", "__init__.py"),
    ]

    for init_file in inits:
        if not os.path.exists(init_file):
            f = open(init_file, "w")
            f.close()
            green(f"Creating {init_file}...")


@click.command()
@click.argument("names", nargs=-1)
def cli(names):
    """Create a Django management command structure and an simple django-click command(s) by name"""
    cwd = os.getcwd()
    build_path(base_path=cwd)

    command_path = os.path.join(cwd, "management", "commands")

    for name in names:
        with open(os.path.join(command_path, f"{name}.py"), "w") as f:
            f.write("import djclick as click\n\n")

            f.write("@click.command()\n")
            f.write("@click.argument('name')\n")
            f.write("def command(name):\n")
            f.write("    click.secho(f'Hello, {name}', fg='red')\n")
