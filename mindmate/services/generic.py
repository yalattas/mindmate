import datetime
from mindmate.utils.utils import utility
from mindmate.utils.conf import constants

class Prompt:
    last_prompt: str
    expires_at: datetime

    # @property
    # def expires_at(self) -> int:
    #     value = None
    #     if self._expires_at is None:
    #         value = 0
    #     else:
    #         value = int(datetime.datetime.utcnow().timestamp() + 360) # now + seconds
    #     return value
    def memorize_last_prompt(self) -> None:
        utility.update_yaml_state({'prompt': vars(self)}, file_path=constants.FILE_PATH+'/'+constants.FILE_NAME)

    def __init__(self, prompt) -> None:
        self.last_prompt = prompt
        self.expires_at = int(datetime.datetime.utcnow().timestamp() + 360) # now + seconds
        self.memorize_last_prompt()
    def __str__(self) -> str:
        return self.last_prompt +' -- '+ str(self.expires_at)