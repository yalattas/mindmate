import click

@click.group()
def nested_group():
    pass

@click.group()
def user():
    pass

@click.group()
def group():
    pass

@click.command()
@click.argument('user_id', type=int)
def create(user_id):
    click.echo(f'Creating user with user_id: {user_id}')

@click.command()
@click.argument('user_id', type=int)
def delete(user_id):
    click.echo(f'Deleting user with user_id: {user_id}')

user.add_command(create)
user.add_command(delete)

@click.command()
@click.argument('group_id', type=int)
def create(group_id):
    click.echo(f'Creating group with group_id: {group_id}')

@click.command()
@click.argument('group_id', type=int)
def delete(group_id):
    click.echo(f'Deleting group with group_id: {group_id}')

group.add_command(create)
group.add_command(delete)

nested_group.add_command(user)
nested_group.add_command(group)


