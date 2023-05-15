from firebase_admin import firestore
# import base64, json, ast

firebase = {
"type": "service_account",
"project_id": "mindmate-dc810",
"private_key_id": "a98714b4ad81fbec382c2d4ccc8f189834ee0db2",
"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKYEcpF2QzMPpt\noGx66ZF66TNkElaQlSRRdPfgDWd6ooz0SvxllWgyfPGGYzldHzT+66Cytw3F77Ut\nIjpJsFxMU5aeOGoCoj+H8vuRYNS8rYkAcw2ghQZ1dDzxrrcyktiMmgVWTVcVYQ42\ny15R+Ys/PNoZ2lRBEWoeZQHh5MG8fWyyC2BJXaBQQuQmGar3+UDaPng3W9npIHbN\nFtzCv3cnbZgRkyelPOB5eB4Lsm1t+JNSp0A+6GmI+3TMgVNuz3+yxv5c/K//XtUp\nFi5dyOrxmQa6NKnOu9/PpomsOuK20hU0FRdpPchv0g9axCOQ+CpbR3GVq2HpjPpG\nHkDH1E5vAgMBAAECggEAEseLYu9GP4/YdUrRNjitZNP2Dl+7Q7BrTdnGVLa5twIV\nhWfd8wlBwYmhmgBkJtWKA+vWni7pasg7LkSCVysz7WtGS0ld4P+wWIu+N3feVeHe\nmDmU9qPRfR27uAun+VvyF14Fh8QmhBfdC02k44N+HfCmJocBkYYtrENgQNeK+NQa\nfZDe0mIkraRJJ+ceLlUL6Lxlcebsj/PP8AZt+wvZmBCFVuxucNgjw8or5DcCzjoz\noSxDJQmgJoA5WawUCW9auUaaCyJLUulEUptCOa2ldUR1W9pbPFnd8krhRGZ3GZzl\nAn8IUTxEJdmbGeJ6rsjaD1AbOPgFQL24Jd0P6jl71QKBgQDnnD6m5zs4mcsZypDw\nSD2D/I9+DqYoCxDylZ+l7YJBGAiibwK6kyVsb1z8RDHLwxM53oS4kdJ8zw9pCIY0\ndX5O0owJhnJj6JvYinkosJ90laVV3BNm6Lzj+SZ54T/F1KHFAZnebgt0a1lxwB8j\nrzXfAGr6b5fM2f7InESxeqqCywKBgQDfr++av6ZOjJBh5CQ5ZOZuz2aGN5iGSIt9\nkpCItWFixLv5QeyJDVpA1YLYmiY7XfI3Js+nISE9haU/puAWWAkDN/E8HaUyl4FJ\ns1zbCXXb2oOAsrMzVewHTVIB48k6+mS8vlGZPa6TfdyywdTby6L7eRQM2yMrSU+P\nvfZcq5YabQKBgEnttpXh4yZa+Nhfr0nzVSdnG4paNLE9bwhvuAjnuhb7C+6FTrKt\nO1nUZjLjtZ1bxCxJmcWsTiqmkT2uid/+zPVuAWMc9jBr1CsXcDsLvaoiBidU2yCT\nE5AVPDHVM1z7VTOkIjA8og1kIqXLdGUYjTKEWKFds2+g+dGhB9A63mhnAoGAZLjO\nBTpi4l+867dU8FsUv7S4D5udHGoyFVsXpdc2gMjhc31RyuyuRR9fCbVvna/Rzy+0\ntSbf1toE7MJxiN4fQMnB4DXhGwTJfKw9FYwO++5K5HqS4nzACRGx6ZPuGpaBIdP4\n3i2+HD/CTuOku0vYma+NbbSHA4jBQJJjCptgvYkCgYEAta4GPwRlA7+cw6X1OO3y\nyXl0wFA/GwBcqzLFRgQYCKWBzmp2YaTUoVC4ICv8EqFQBKXume6NSNdMpgEPnLou\ntKM4HZ/iwgpedHRvzsybY4Lh2yQ3m6rPtHelz8NhqfqQsW4BLptVLxxIIlTAgHlb\njgrPbikqg7GYPLgw+HxO8PI=\n-----END PRIVATE KEY-----\n",
"client_email": "firebase-adminsdk-kl4wg@mindmate-dc810.iam.gserviceaccount.com",
"client_id": "107189152122943983475",
"auth_uri": "https://accounts.google.com/o/oauth2/auth",
"token_uri": "https://oauth2.googleapis.com/token",
"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-kl4wg%40mindmate-dc810.iam.gserviceaccount.com",
"universe_domain": "googleapis.com"
}

db = firestore.Client.from_service_account_info(firebase)

class constants:
    FILE_PATH = '~/.mindmate'
    FILE_NAME = 'environment.yaml'
    SYS_ROLE = 'system'
    HINT_ROLE = 'HINT'
    PLATFORM_OPTIONS = ['openai']
    MODEL_OPTIONS = {
        'openai': ['text-davinci-003'],
    }
    WRITING = db.collection("platform").document("writing").get().to_dict()
    IMAGES = db.collection("platform").document("images").get().to_dict()
    VIDEO = db.collection("platform").document("video").get().to_dict()
    PROMPTING = db.collection("platform").document("prompting").get().to_dict()
    DESIGN = db.collection('platform').document('design').get().to_dict()
    PRESENTATION = db.collection('platform').document('presentation').get().to_dict()
    NO_CODE = db.collection('platform').document('no_code').get().to_dict()
    DATA = db.collection('platform').document('data').get().to_dict()
    CODING = db.collection('platform').document('coding').get().to_dict()
