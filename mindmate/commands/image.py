import click
from mindmate.utils.utils import utility
from mindmate.utils.helper import help
from mindmate.utils.conf import constants
from mindmate.services.openai import OpenAIManager
from mindmate.services.generic import Prompt, Image
from mindmate.error import ArgumentError, Error

@click.group()
def image():
    """Image-based operations, see sub-commands"""
    pass

@click.command(name='create')
@click.option('-P', '--platform', required=True, default='openai', show_default=False, type=click.Choice(constants.PLATFORM_OPTIONS), help='use platform as an underlying technology')
@click.option('-p', '--prompt', required=False, show_default=False, type=str, help='Your prompt to AI')
@click.option('--use-last-prompt', required=False, default=False, show_default=True, type=bool, help='pass your last prompt as an input to this call')
def create(platform, prompt, use_last_prompt):
    """offers image-based response to your prompt"""
    click.echo(help.generating())
    # click.echo(click.get_current_context().params)
    if use_last_prompt:
        prompt = Prompt(prompt, store_prompt=False)
    else:
        if prompt is None:
            raise ArgumentError(Error.MISSING_PROMPT)
        prompt = Prompt(prompt, store_prompt=True)
    KEYS = utility.get_yaml_state(constants.FILE_PATH+'/'+constants.FILE_NAME)['keys']
    if platform == 'openai':
        openai_client = OpenAIManager(id=KEYS['openai_id'], token=KEYS['openai_token'])
        url = openai_client.generate_image(prompt=prompt)
        Image(url).download_image_to_current_path()
        click.echo(f'Image has been saved to your local.\nimage url for reference: {url}')

image.add_command(create)