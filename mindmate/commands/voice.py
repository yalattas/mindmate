import click
from mindmate.utils.helper import help
from mindmate.services.voice import VoiceManager
from mindmate.services.generic import Prompt
from mindmate.error import ArgumentError, Error

@click.group()
def voice():
    """Voice-based operations, see sub-commands"""
    pass

@click.command(name='text_to_speech')
@click.option('-p', '--prompt', required=False, show_default=False, type=str, help='Your prompt to AI')
@click.option('--use-last-prompt', required=False, default=False, show_default=True, type=bool, help='pass your last prompt as an input to this call')
@click.option('-l', '--language', required=False, default='en', show_default=True, type=str, help='IETF language tag. Language to speak in')
@click.option('-o', '--output-file', required=False, default='speech', show_default=True, type=str, help='name output file like \'speech.mp3\'')
@click.option('-s', '--slow', required=False, default=False, show_default=True, type=bool, help='Whether to generate the audio in slow speed')
def text_to_speech(prompt, use_last_prompt, language, output_file, slow):
    """offers voice over response to your prompt"""
    click.echo(help.recording())
    # click.echo(click.get_current_context().params)
    if use_last_prompt:
        prompt = Prompt(prompt, store_prompt=False)
    else:
        if prompt is None:
            raise ArgumentError(Error.MISSING_PROMPT)
        prompt = Prompt(prompt, store_prompt=True)
    VoiceManager.generate_audio(prompt=prompt, language=language, output_file=output_file, slow=slow)

voice.add_command(text_to_speech)