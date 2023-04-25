import click
import yaml
import uuid
import os
from mindmate.utils.utils import utility
from mindmate.utils.conf import constants

@click.command()
def configure():
    """collect keys from user and save it into state file as yaml"""

    # PATH = '~/.mindmate'
    # FILE_NAME = 'environment.yaml'

    while not os.path.isfile(constants.FILE_PATH+'/'+constants.FILE_NAME):
        try:
            os.makedirs(constants.FILE_PATH)
        except FileExistsError as f:
            pass
        data = {
            'version':1,
            'keys': {
                'openai_token':'xxxx',
                'openai_id':'xxxx',
            }
        }
        with open(constants.FILE_PATH+'/'+constants.FILE_NAME, 'w') as outputfile:
            yaml.dump(data, outputfile, default_flow_style=False)

    file = utility.set_yaml_state(constants.FILE_PATH+'/'+constants.FILE_NAME)
    #TODO: check environment variable first before setting values into yaml file. If exist, then skip yaml update
    openai_value = file['keys']['openai_token']
    openai_user_token = click.prompt(f'OPENAI TOKEN [****************{openai_value[-4:]}]', type=str)
    file['keys']['openai_token'] = openai_user_token
    file['keys']['openai_id'] = str(uuid.uuid4())
    utility.update_yaml_state(state=file, file_path=constants.FILE_PATH+'/'+constants.FILE_NAME)
