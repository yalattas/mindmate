import yaml
import os
import string, random
from mindmate.utils.conf import constants, mongo

class utility:
    def create_yaml_state(file: str) -> dict:
        while not os.path.isfile(constants.FILE_PATH+'/'+constants.FILE_NAME):
            os.makedirs(constants.FILE_PATH, exist_ok=True)
            data = {
                'version':1,
                'keys': {
                    'openai_token':'xxxx',
                    'openai_id':'xxxx',
                },
                'prompt': {
                    'last_prompt': None,
                    'expires_at': None,
                }
            }
            with open(constants.FILE_PATH+'/'+constants.FILE_NAME, 'w') as outputfile:
                yaml.dump(data, outputfile, default_flow_style=False)
            return data
    def get_yaml_state(file: str) -> dict:
        """Read YAML file and return data as dictionary."""
        try:
            with open(file, 'r') as f:
                data_dict = yaml.load(f, Loader=yaml.FullLoader)
            return data_dict
        except FileNotFoundError as f:
            return utility.create_yaml_state(file)
    def update_yaml_state(state: dict, file_path: str) -> None:
        """update new yaml state with only changed keys and maintain unchanged values"""
        existing_state = utility.get_yaml_state(constants.FILE_PATH+'/'+constants.FILE_NAME)
        existing_state.update(state)
        with open(file_path, 'w') as outputfile:
            yaml.dump(existing_state, outputfile, default_flow_style=False)

    #TODO: below implementation is not associated with any functionality yet, require implementation to be completed
    # def override_with_environment_variables(data: dict) -> dict:
    #     """Override YAML data with environment variables."""
    #     for key in data:
    #         if key in os.environ:
    #             data[key] = os.environ[key]
    #     return data

    def extract_results(result: dict) -> dict:
        final = {}
        for object in result:
            for key, value in object.items():
                if key != '_id':
                    final.update({key: value})
        return final
    def generate_random_string() -> str:
        length = random.randint(5, 10)
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string
    def get_the_current_path() -> str:
        return os.getenv('PWD')