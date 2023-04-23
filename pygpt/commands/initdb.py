import click

@click.command()
@click.argument('name', type=str)
@click.option('--count', default=1, help='Number of times to initialize the database.')
def initdb(name, count):
    """Initialize the database with a given name."""
    click.echo(f'Initializing the database: {name} (count: {count})')
