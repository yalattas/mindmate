import click
import sys
from mindmate.utils.utils import utility
from mindmate.utils.helper import help
from mindmate.utils.conf import constants
from mindmate.services.openai import OpenAIManager
from mindmate.services.generic import Prompt


def model_option_callback(ctx, param, value):
    try:
        platform = ctx.params['platform']
    except KeyError:
        click.echo(f"{constants.SYS_ROLE}: You can't specify a platform/model alone, you need to specify them both or don't specify both.")
        click.echo(f"{constants.HINT_ROLE}: try to re-order to the options and starts with --platform/-P then --model/-m and then --prompt/-p")
        sys.exit(1)
    if platform == 'openai':
        return value if value in constants.MODEL_OPTIONS['openai'] else None
    else:
        return None

@click.command()
@click.option('-P', '--platform', required=True, default='openai', show_default=False, type=click.Choice(constants.PLATFORM_OPTIONS), help='use platform as an underlying technology')
@click.option('-m', '--model', required=True, default='text-davinci-003', show_default=True, type=str, callback=model_option_callback, help='select targeted model to utilize')
@click.option('-p', '--prompt', required=True, show_default=False, type=str, help='Your prompt to AI')
@click.option('-s', '--stream', required=False, default=True, show_default=True, type=bool, help='stream AI response on your terminal')
@click.option('--max-tokens', required=False, default=100, show_default=True, type=int, help='stream AI response on your terminal')
def chat(platform, model, prompt, stream, max_tokens):
    """offers text-based response to your prompt"""
    click.echo(help.generic_message())
    # click.echo(click.get_current_context().params)
    KEYS = utility.get_yaml_state(constants.FILE_PATH+'/'+constants.FILE_NAME)['keys']
    if platform == 'openai':
        openai_client = OpenAIManager(id=KEYS['openai_id'], token=KEYS['openai_token'])
        openai_client.check_model(model)
        prompt = Prompt(prompt)
        if stream == False:
            response = openai_client.ask_ai(prompt=prompt, model=model, max_tokens=max_tokens)
            click.echo(f'{constants.AI_ROLE}: {response}')
        elif stream == True:
            click.echo(f'{constants.AI_ROLE}: ', nl=False)
            for response in openai_client.ask_ai_with_stream(prompt=prompt, model=model, max_tokens=max_tokens): click.echo(response, nl=False)
    else:
        click.echo(f'{constants.SYS_ROLE}: platform ({platform}) is not supported yet')
