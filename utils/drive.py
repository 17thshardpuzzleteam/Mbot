
import gspread
import os
import json
from dotenv import load_dotenv
from google.oauth2 import service_account


# Google Drive API functionality that is required by various cogs

class Drive:

    instance = None

    # override to ensure that only one Drive object is ever created
    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Drive, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # TODO: has to be a less silly way to organize this
        load_dotenv()
        self.key = os.getenv('GOOGLE_CLIENT_SECRETS')
        self.googledata = json.loads(self.key)
        self.googledata['private_key'] = self.googledata['private_key'].replace("\\n", "\n")
        self.oauthkey = os.getenv('GOOGLE_OAUTH_SECRETS')
        self.googleoauthdata = json.loads(self.oauthkey)
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.oauth_authuser = json.loads(os.getenv('GOOGLE_OAUTH_AUTH_USER'))
        gc, authorized_user = gspread.oauth_from_dict(credentials=self.googleoauthdata,authorized_user_info=self.oauth_authuser)
        self.gc = gc
        #self.credentials = service_account.Credentials.from_service_account_info(self.googledata, scopes=scopes)

    def gclient(self):
        return self.gc



