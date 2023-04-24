import click
from .utils import helper
from .commands.configure import configure
from .commands.initdb import initdb
from .commands.dropdb import dropdb
from .commands.nested_group import nested_group

@click.group()
def cli():
    """hi to mindmate cli, try option --help for more information"""
    pass

cli.add_command(configure)
cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(nested_group)

if __name__ == '__main__':
    cli()
