
import gspread
import os
import json
from dotenv import load_dotenv
from google.oauth2 import service_account


load_dotenv()
oauthkey = os.getenv('GOOGLE_OAUTH_SECRETS')
googleoauthdata = json.loads(oauthkey)
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
gc, authorized_user = gspread.oauth_from_dict(googleoauthdata)
print("add this line to your .env file (make sure it's all in one line)")
print("GOOGLE_OAUTH_AUTH_USER=" + authorized_user)
