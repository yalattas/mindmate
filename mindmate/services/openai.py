import sys
import openai
import click
from mindmate.utils.conf import constants
from mindmate.error import OpenAiError, Error
from mindmate.services.generic import Prompt

class OpenAIManager:
    openai_id : str
    openai_token: str

    def __init__(self, id, token) -> None:
        self.openai_id = id
        self.openai_token = token

    def set_openai_client(func):
        """This decorator facilitates the OpenAI client configuration by automatically assigning the specified token prior to making a request"""
        def wrapper(self, *args, **kwargs):
            openai.api_key = self.openai_token
            return func(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def check_model(model: str) -> None:
        if model not in constants.MODEL_OPTIONS['openai']:
            raise OpenAiError(Error.INVALID_MODEL)

    @set_openai_client
    def ask_ai(self, prompt: Prompt, model: str, max_tokens=5000, n=1) -> str:
        """
        Executes a request to the OpenAI API for text generation based on a given prompt.
        Args:
            self: The instance of the class containing this method.
            prompt (Prompt): The input has an attribute called last_prompt which is string to guide the text generation.
            model (str): The identifier of the model to be used for the text generation.
            max_tokens (int, optional): The maximum length of the generated text. Defaults to 100.
            n (int, optional): The number of text outputs to generate. Defaults to 1.

        Returns:
            str: The generated text from the API.

        Note:
            This method requires an OpenAI API token to be set prior to execution. @set_openai_client decorator will take care of it as long as it's exist in environment.yaml file
        """
        try:
            completion = openai.Completion.create(
                model=model,
                temperature=0,
                stream=False,
                max_tokens=max_tokens,
                user=self.openai_id,
                prompt = prompt.last_prompt
            )
            response = completion['choices'][0]['text']
        except openai.error.AuthenticationError as e:
            raise OpenAiError(Error.AUTHENTICATION_ERROR)
        except openai.error.RateLimitError as r:
            raise OpenAiError(Error.RATE_LIMIT_ERROR)
        except openai.error.InvalidRequestError as t:
            raise OpenAiError(Error.INVALID_MODEL)
        return response.strip()

    @set_openai_client
    def ask_ai_with_stream(self, prompt: Prompt, model: str, max_tokens=5000, n=1) -> object:
        """
        Executes a request to the OpenAI API for text generation based on a given prompt.
        Args:
            self: The instance of the class containing this method.
            prompt (Prompt): The input has an attribute called last_prompt which is string to guide the text generation.
            model (str): The identifier of the model to be used for the text generation.
            max_tokens (int, optional): The maximum length of the generated text. Defaults to 100.
            n (int, optional): The number of text outputs to generate. Defaults to 1.

        Returns:
            object: Partial text to be returned whenever it's ready from the call till its completion

        Note:
            This method requires an OpenAI API token to be set prior to execution. @set_openai_client decorator will take care of it as long as it's exist in environment.yaml file
        """
        try:
            completion = openai.Completion.create(
                model=model,
                temperature=0,
                stream=True,
                max_tokens=max_tokens,
                user=self.openai_id,
                prompt = prompt.last_prompt,
            )
            for token in completion:
                yield token['choices'][0]['text']
        except openai.error.AuthenticationError as e:
            raise OpenAiError(Error.AUTHENTICATION_ERROR)
        except openai.error.RateLimitError as r:
            raise OpenAiError(Error.RATE_LIMIT_ERROR)
        except openai.error.InvalidRequestError as t:
            raise OpenAiError(Error.INVALID_MODEL)

    @set_openai_client
    def generate_image(self, prompt: Prompt, n=1) -> str:
        try:
            completion = openai.Image.create(
                    user=self.openai_id,
                    prompt = prompt.last_prompt
                )
            response = completion['data'][0]['url']
        except openai.error.AuthenticationError as e:
            raise OpenAiError(Error.AUTHENTICATION_ERROR)
        except openai.error.RateLimitError as r:
            raise OpenAiError(Error.RATE_LIMIT_ERROR)
        except openai.error.InvalidRequestError as t:
            raise OpenAiError(Error.INVALID_MODEL)
        return response

    def __str__(self) -> str:
        return self.openai_id + ' -- ' + self.openai_token