__author__ = 'denisantyukhov'
import requests

APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
ACCESS_TOKEN = '2.00no3HpF_CjAmD38b962df537ZLw8B'

def getUsersForKeyword(keyWord):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'q':keyWord, 'count':50}
    r = requests.get("https://api.weibo.com/2/search/suggestions/users.json", params=payload)
    return r.text

def getHotUsersForCategory(category):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'category':category, 'count':50}
    r = requests.get("https://api.weibo.com/2/suggestions/users/hot.json", params=payload)
    return r.text

print(getHotUsersForCategory('tech'))
