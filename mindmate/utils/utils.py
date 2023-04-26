import yaml
import os
from mindmate.utils.conf import constants

class utility:
    def create_yaml_state(file: str) -> dict:
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
            return data
    def set_yaml_state(file: str) -> dict:
        """Read YAML file and return data as dictionary."""
        try:
            with open(file, 'r') as f:
                data_dict = yaml.load(f, Loader=yaml.FullLoader)
            return data_dict
        except FileNotFoundError as f:
            return utility.create_yaml_state(file)
    def update_yaml_state(state: dict, file_path: str) -> None:
        """update new yaml state with only changed keys and maintain unchanged values"""
        with open(file_path, 'w') as outputfile:
            yaml.dump(state, outputfile, default_flow_style=False)

    #TODO: below implementation is not associated with any functionality yet, require implementation to be completed
    def override_with_environment_variables(data: dict) -> dict:
        """Override YAML data with environment variables."""
        for key in data:
            if key in os.environ:
                data[key] = os.environ[key]
        return data