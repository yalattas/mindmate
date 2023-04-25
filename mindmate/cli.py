import click
from mindmate.utils import helper
from mindmate.commands.configure import configure
from mindmate.commands.chat import chat
from mindmate.commands.ai import ai
from mindmate.commands.initdb import initdb
from mindmate.commands.dropdb import dropdb

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """hi to mindmate cli, try option --help for more information"""
    pass

cli.add_command(configure)
cli.add_command(chat)
cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(ai)

if __name__ == '__main__':
    cli()
