import datetime
import requests
import os
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

    def __init__(self, prompt, store_prompt=True) -> None:
        self.expires_at = int(datetime.datetime.utcnow().timestamp() + 360) # now + seconds
        if store_prompt:
            self.last_prompt = prompt
            self.memorize_last_prompt()
        else:
            self.last_prompt = utility.get_yaml_state(constants.FILE_PATH+'/'+constants.FILE_NAME)['prompt']['last_prompt']
    def __str__(self) -> str:
        return self.last_prompt +' -- '+ str(self.expires_at)

class Image:
    url: str or None
    def __init__(self, url) -> None:
        self.url = url
    def download_image_to_current_path(self) -> None:
        image = requests.get(self.url)
        current_path = utility.get_the_current_path()
        image_path = os.path.join(current_path, utility.generate_random_string())
        with open(image_path+'.png', 'wb') as f:
            f.write(image.content)