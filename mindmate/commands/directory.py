import click
from mindmate.services.directory import manifest

def _generate_output(content: dict) -> None:
    # Determine the maximum length of keys for formatting
    try:
        max_key_length = max(len(str(key)) for key in content.keys())
    except ValueError as e:
        max_key_length = 5

    # Print the table headers
    header = f'{"platform":<{max_key_length}} reference'
    yield header + '\n'

    header_line = f'{"-" * max_key_length} {"-" * max_key_length}'
    yield header_line + '\n'

    # Print the keys and values in the table
    for key, value in content.items():
        row = f'{str(key):<{max_key_length}} {value}'
        yield row + '\n'

@click.group()
def directory():
    """Returns related functionalities to AI platforms"""
    pass

@click.group()
def chat():
    """Returns related functionalities to chat-based AI platforms"""
    pass

@click.group()
def image():
    """Returns related functionalities to image-based AI platforms"""
    pass

@click.group()
def video():
    """Returns related functionalities to video-based AI platforms"""
    pass

@click.group()
def prompting():
    """Returns related functionalities to chat-based AI platforms"""
    pass

@click.group()
def design():
    """Returns related functionalities to design-based AI platforms"""
    pass

@click.group()
def presentation():
    """Returns related functionalities to presentation-based AI platforms"""
    pass

@click.group()
def no_code():
    """Returns related functionalities to build apps with no code using AI platforms"""
    pass

@click.group()
def data():
    """Returns related functionalities to data manipulation AI platforms"""
    pass

@click.group()
def coding():
    """Returns related functionalities to code-based AI platforms"""
    pass

@click.command(name='list')
def list_chat():
    """a list of AI platforms that offer chat-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_writing()))

chat.add_command(list_chat)

@click.command(name='list')
def list_image():
    """a list of AI platforms that offer image-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_images()))

image.add_command(list_image)

@click.command(name='list')
def list_video():
    """a list of AI platforms that offer video-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_videos()))

video.add_command(list_video)

@click.command(name='list')
def list_prompting():
    """a list of AI platforms that offer image-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_prompting()))

prompting.add_command(list_prompting)

@click.command(name='list')
def list_design():
    """a list of AI platforms that offer design-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_designs()))

design.add_command(list_design)

@click.command(name='list')
def list_presentation():
    """a list of AI platforms that offer presentation-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_presentations()))

presentation.add_command(list_presentation)

@click.command(name='list')
def list_no_code_apps():
    """a list of AI platforms that offer no-code development platform"""
    click.echo_via_pager(_generate_output(manifest.list_no_code()))

no_code.add_command(list_no_code_apps)

@click.command(name='list')
def list_data():
    """a list of AI platforms that offer data-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_data()))

data.add_command(list_data)

@click.command(name='list')
def list_coding():
    """a list of AI platforms that offer code-based responses"""
    click.echo_via_pager(_generate_output(manifest.list_development()))

coding.add_command(list_coding)

directory.add_command(chat)
directory.add_command(image)
directory.add_command(video)
directory.add_command(prompting)
directory.add_command(design)
directory.add_command(presentation)
directory.add_command(no_code)
directory.add_command(data)
directory.add_command(coding)
