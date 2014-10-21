__author__ = 'denisantyukhov'
from weibo import APIClient
import webbrowser
import requests


APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
CALLBACK_URL = 'https://github.com/gaphex'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

webbrowser.open(url, new=1, autoraise=True)
code = raw_input()

r = client.request_access_token(code)
access_token = r.access_token
expires_t = r.expires

print access_token

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL,
                   access_token=access_token, expires=expires_t)


