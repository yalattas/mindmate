import click
from .utils import helper
from .commands.initdb import initdb
from .commands.dropdb import dropdb
from .commands.nested_group import nested_group

@click.group()
def cli():
    pass

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(nested_group)

if __name__ == '__main__':
    cli()
