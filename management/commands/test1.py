import djclick as click

@click.command()
@click.argument('name')
def command(name):
    click.secho(f'Hello, {name}', fg='red')
