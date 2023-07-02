import click
from mindmate.services.generic import Prompt
from mindmate.utils.utils import utility
from gtts import gTTS

class VoiceManager:
    @staticmethod
    def generate_audio(prompt: Prompt, language: str, output_file: str, slow=False) -> None:
        """
        Generate audio file from a given prompt using the gTTS (Google Text-to-Speech) library.

        Args:
            prompt (Prompt): The prompt object containing the text to convert to audio.
            language (str): The language code for the desired language of the audio.
            output_file (str): The name of the output audio file (without the extension).
            slow (bool, optional): Whether to generate the audio in slow speed. Defaults to False.

        Returns:
            None

        Raises:
            None

        Example usage:
            VoiceManager.generate_audio(prompt, language='en', output_file='output', slow=False)
        """
        current_path = utility.get_the_current_path()
        converter = gTTS(text=prompt.last_prompt, lang= language, slow=slow)
        converter.save(current_path+'/'+output_file+'.mp3')
        click.echo(f"saved to ->  {current_path}/{output_file}.mp3")