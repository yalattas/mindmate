import click

@click.command()
@click.option('--force', is_flag=True, help='Force drop the database without confirmation.')
def dropdb(force):
    """Drop the database."""
    if force:
        click.echo('Dropping the database (forced)...')
    else:
        click.confirm('Are you sure you want to drop the database?', abort=True)
        click.echo('Dropping the database...')

