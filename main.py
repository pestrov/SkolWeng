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
print(code)


