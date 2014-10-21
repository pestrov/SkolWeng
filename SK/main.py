__author__ = 'denisantyukhov'
import requests

APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
CALLBACK_URL = 'https://github.com/gaphex'
ACCESS_TOKEN = '2.00no3HpF_CjAmD38b962df537ZLw8B'

def getUsersForKeyword(keyWord):
    client_id = '3457835747'
    payload = {'client_id': client_id, 'access_token': ACCESS_TOKEN, 'q':keyWord}
    r = requests.get("https://api.weibo.com/2/search/suggestions/users.json", params=payload)
    return r.text

print getUsersForKeyword('Education')