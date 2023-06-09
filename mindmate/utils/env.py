# #TODO: validate below code
# import yaml
# import os

# def read_yaml_file(file_path):
#     """Read YAML file and return data as dictionary."""
#     with open(file_path, 'r') as file:
#         data = yaml.safe_load(file)
#     return data

# def override_with_environment_variables(data):
#     """Override YAML data with environment variables."""
#     for key in data:
#         if key in os.environ:
#             data[key] = os.environ[key]
#     return data

# # Example usage
# file_path = 'config.yaml'  # Update with your actual YAML file path
# data = read_yaml_file(file_path)
# data = override_with_environment_variables(data)
# print(data)
