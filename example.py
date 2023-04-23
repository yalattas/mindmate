import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name', type=str)
def initdb(count, name):
    click.echo(f'Initialized the database: {name} with count: {count}')

@click.command()
def dropdb():
    click.echo('Dropped the database')

@click.group()
def nested_group():
    pass

@click.command()
@click.option('--option1', help='Option 1 help text.')
def nested_command1(option1):
    click.echo(f'Nested Command 1 with option1: {option1}')

@click.command()
@click.option('--option2', help='Option 2 help text.')
def nested_command2(option2):
    click.echo(f'Nested Command 2 with option2: {option2}')

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(nested_group)

nested_group.add_command(nested_command1)
nested_group.add_command(nested_command2)

if __name__ == '__main__':
    cli()
