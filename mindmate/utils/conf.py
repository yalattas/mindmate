import base64

class mongo:
    DATA_API_APP_ID = 'data-mzlwr'
    BASE_URL = f'https://data.mongodb-api.com/app/{DATA_API_APP_ID}/endpoint/data/v1'
    API_KEY = base64.b64decode('UHg0emhsV2pPam4wbk1BYWg4SHZ6dWREY2N5NmlWZVRtRHNEeThpTE52N3pTNFZwb0lhMld3UXRQUmZuYkhnUwo=').decode('utf-8').rstrip()
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY,
    }
    def initialize_client() -> object:
        return mongo

class constants:
    FILE_PATH = '~/.mindmate'
    FILE_NAME = 'environment.yaml'
    SYS_ROLE = 'system'
    AI_ROLE = 'AI bot'
    HINT_ROLE = 'HINT'
    PLATFORM_OPTIONS = ['openai']
    MODEL_OPTIONS = {
        'openai': ['text-davinci-003', 'text-davinci-002'],
    }
