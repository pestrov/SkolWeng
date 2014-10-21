# -*- coding: utf-8 -*-
import requests

APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
ACCESS_TOKEN = '2.00no3HpF_CjAmD38b962df537ZLw8B'
WEIBO_BASE = 'https://api.weibo.com/2/'

def getUserInfo(userId):
    payload = {'access_token':ACCESS_TOKEN,'uid':userId}
    r = requests.get(WEIBO_BASE+"users/show.json", params=payload)
    return r.text

def getUserStats(userId):
    payload = {'access_token':ACCESS_TOKEN,'uids':userId}
    r = requests.get(WEIBO_BASE+"users/counts.json", params=payload)
    return r.text

def getUsersForKeyword(keyWord):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'q':keyWord, 'count':50}
    r = requests.get(WEIBO_BASE+"search/suggestions/users.json", params=payload)
    return r.text

def getHotUsersForCategory(category):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'category':category, 'count':50}
    r = requests.get(WEIBO_BASE+"suggestions/users/hot.json", params=payload)
    return r.text

def getRelationship(uid1, uid2):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'source_id':uid1, 'target_id':uid2, 'count':50}
    r = requests.get(WEIBO_BASE+"friendships/show.json", params=payload)
    return r.text



print getUserStats([2100027704])
