from mindmate.utils.conf import constants
import logging
from enum import Enum

logger = logging.getLogger()

class Error(Enum):
    # general errors
    MISSING_PROMPT = "prompt is missing, must pass a string prompt"

    # openai errors
    INVALID_MODEL = f"invalid model, pass one of the correct options python main.py chat --model {constants.MODEL_OPTIONS['openai']}"
    AUTHENTICATION_ERROR = "invalid credentials, use 'mindmate configure' command to provide valid token, see https://platform.openai.com/account/api-keys"
    RATE_LIMIT_ERROR = "You exceeded your current OPENAI quota, check your plan and billing details"

class ExecutionError(Exception):
    def __init__(self, error: Error):
        self.error = error
        logger.info(error.value)

    def __str__(self) -> str:
        return self.error.value

class OpenAiError(ExecutionError):
    def __init__(self, error: Error):
        self.error = error
        logger.info(error.value)

    def __str__(self) -> str:
        return self.error.value

class ArgumentError(Exception):
    def __init__(self, error: Error):
        self.error = error
        logger.info(error.value)

    def __str__(self) -> str:
        return self.error.value
