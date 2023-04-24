import click
import yaml
import os

def set_yaml_state(file: str) -> dict:
    with open(file, 'r') as f:
        data_dict = yaml.load(f, Loader=yaml.FullLoader)
    return data_dict
def update_yaml_state(state: dict, file_path: str) -> None:
    with open(file_path, 'w') as outputfile:
        yaml.dump(state, outputfile, default_flow_style=False)

@click.command()
def configure():
    """To configure the interface for future calls"""

    PATH = '~/.mindmate'
    FILE_NAME = 'environment.yaml'

    while not os.path.isfile(PATH+'/'+FILE_NAME):
        try:
            os.makedirs(PATH)
        except FileExistsError as f:
            pass
        data = {
            'keys': {
                'openai_token':'xxxx'
            }
        }
        with open(PATH+'/'+FILE_NAME, 'w') as outputfile:
            yaml.dump(data, outputfile, default_flow_style=False)

    file = set_yaml_state(PATH+'/'+FILE_NAME)
    openai_value = file['keys']['openai_token']
    openai_user_token = click.prompt(f'OPENAI TOKEN [****************{openai_value[-4:]}]', type=str)
    file['keys']['openai_token'] = openai_user_token
    update_yaml_state(state=file, file_path=PATH+'/'+FILE_NAME)
