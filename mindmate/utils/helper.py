import click

class help:
    @staticmethod
    def generic_message() -> str:
        return "thinking ..."
    @staticmethod
    def generating() -> str:
        return "generating ..."

@click.command()
def helper():
    """Helper command for providing additional functionality."""
    click.echo('This is a helper command.')
