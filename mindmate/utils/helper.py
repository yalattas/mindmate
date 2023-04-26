import click

class help:
    @staticmethod
    def generic_message() -> str:
        return "thinking ..."
    def looking_message() -> str:
        return "looking ..."

@click.command()
def helper():
    """Helper command for providing additional functionality."""
    click.echo('This is a helper command.')
