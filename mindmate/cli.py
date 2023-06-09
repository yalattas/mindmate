import click
from mindmate.utils import helper
from mindmate.commands.configure import configure
from mindmate.commands.chat import chat
from mindmate.commands.directory import directory
from mindmate.commands.image import image
from mindmate.commands.version import version

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """hi to mindmate cli, try option --help for more information"""
    pass

cli.add_command(configure)
cli.add_command(chat)
cli.add_command(directory)
cli.add_command(image)
cli.add_command(version)

if __name__ == '__main__':
    cli()
