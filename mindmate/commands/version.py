import click
from .. import meta

@click.command()
def version():
    version = meta.VERSION
    click.echo(f'mindmate cli version: {version}')