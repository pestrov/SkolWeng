# -*- coding: utf-8 -*-
import requests

APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
ACCESS_TOKEN = '2.00no3HpF_CjAmD38b962df537ZLw8B'

WEIBO_BASE = 'https://api.weibo.com/2/'

def getUserActiveFollowers(userId):
    payload = {'access_token':ACCESS_TOKEN,'uid':userId,'count':200}
    r = requests.get(WEIBO_BASE+"friendships/followers/active.json", params=payload)
    return r.text

def getUserFollowersId(userId, startFrom):
    payload = {'access_token':ACCESS_TOKEN,'uid':userId,'count':5000}
    r = requests.get(WEIBO_BASE+"friendships/followers/ids.json", params=payload)
    return r.text

def getUserInfo(userId):
    payload = {'access_token':ACCESS_TOKEN,'uid':userId}
    r = requests.get(WEIBO_BASE+"users/show.json", params=payload)
    return r.text

  def getUsersForKeyword(keyWord):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'q':keyWord, 'count':50}
    r = requests.get("https://api.weibo.com/2/search/suggestions/users.json", params=payload)
    return r.text

def getHotUsersForCategory(category):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'category':category, 'count':50}
    r = requests.get("https://api.weibo.com/2/suggestions/users/hot.json", params=payload)
    return r.text

print getUserInfo(2003324087)
