__author__ = 'denisantyukhov'
from weibo import APIClient
import webbrowser
import requests


APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
CALLBACK_URL = 'https://github.com/gaphex'
ACCESS_TOKEN = '2.00no3HpF_CjAmD38b962df537ZLw8B'
access_token = ACCESS_TOKEN
expires_in = 100500
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token (access_token, expires_in)
r = client.statuses.user_timeline.get (uid = 5336013309)
for st in r.statuses:
    print st.text
