# -*- coding: utf-8 -*-
import requests

APP_KEY = '3457835747'
APP_SECRET = '04c6dac1c5eb0226c14e85a50ef9274d'
ACCESS_TOKEN = '2.00no3HpF_CjAmD38b962df537ZLw8B'
WEIBO_BASE = 'https://api.weibo.com/2/'
users = [1191965271, 1986926181, 3288976495, 2230312052, 1751714412, 2217035934, 1814040741, 1796445350,1904769205, 1771925961, 2000961721, 2100623570, 2089800791, 1644489953, 1225314032, 5120783603, 1823887605, 1729332983, 2098122492, 2243807243, 1853472775, 1626443785, 2165090317, 3235040884, 1642482194,1682207150, 2847927727,3034112034, 1651428902, 2011075080, 1649159940, 1873625985, 3763936545, 2737798435, 3830136640, 1663414103, 1663937380, 1256947091, 1642634100, 3446047612, 5016338752, 3237705130, 1642632622, 2418433987, 2410528240]

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

def getUsersWithContent(content):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'content':content, 'count':50}
    r = requests.get(WEIBO_BASE+"suggestions/users/by_status.json", params=payload)
    return r.text

def getRelationship(uid1, uid2):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'source_id':uid1, 'target_id':uid2, 'count':50}
    r = requests.get(WEIBO_BASE+"friendships/show.json", params=payload)
    return r.text

def getUserTrends(userId):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'uid':userId, 'count':50}
    r = requests.get(WEIBO_BASE+"trends.json", params=payload)
    return r.text

def getUserTags(userId):
    payload = {'client_id': APP_KEY, 'access_token': ACCESS_TOKEN, 'uid':userId, 'count':50}
    r = requests.get(WEIBO_BASE+"tags.json", params=payload)
    return r.text

userStats = []
for user in users:
    userStat = getUserStats(user)
    userStats.append(userStat)
    print userStat