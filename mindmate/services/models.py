from mindmate.utils.conf import mongo
import requests, json

class base:
    def get_client() -> object:
        return mongo.initialize_client()

class Writing:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'writing',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class Image:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'images',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class Video:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'video',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class Prompt:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'prompting',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class Design:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'design',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class Presentation:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'presentation',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class NoCodeDevelopmentPlatform:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'no_code',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class Data:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'data',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result

class DevelopmentPlatform:
    @staticmethod
    def get_all() -> list:
        db = base.get_client()
        data = json.dumps({
            'dataSource': 'mindmate',
            'database':'platforms',
            'collection':'coding',
        })
        result = requests.post(db.BASE_URL + '/action/find', headers=db.headers, data=data).json()['documents']
        return result