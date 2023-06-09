import click
import uuid
from mindmate.utils.utils import utility
from mindmate.utils.conf import constants

@click.command()
def configure():
    """collect keys from user and save it into state file as yaml"""

    file = utility.get_yaml_state(constants.FILE_PATH+'/'+constants.FILE_NAME)
    #TODO: check environment variable first before setting values into yaml file. If exist, then skip yaml update
    openai_value = file['keys']['openai_token']
    openai_user_token = click.prompt(f'OPENAI TOKEN [****************{openai_value[-4:]}]', type=str)
    file['keys']['openai_token'] = openai_user_token
    file['keys']['openai_id'] = 'mindmate-'+str(uuid.uuid4())
    utility.update_yaml_state(state=file, file_path=constants.FILE_PATH+'/'+constants.FILE_NAME)
