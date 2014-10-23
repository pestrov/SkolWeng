# -*- coding: utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
import urllib
import time
import re
import sys
import json
dstrip = re.compile('[^0-9]+')
users = [1853472775, 1626443785, 2165090317, 3235040884, 1642482194,1682207150, 2847927727,3034112034, 1651428902, 2011075080, 1649159940, 1873625985, 3763936545, 2737798435, 3830136640, 1663414103, 1663937380, 1256947091, 1642634100, 3446047612, 5016338752, 3237705130, 1642632622, 2418433987, 2410528240]

def digits(s):
    return dstrip.sub('', s)

def wait_for(selector):
    sys.stderr.write("Waiting for %s..." % selector)
    while True:
        try:
            driver.find_element_by_css_selector(selector)
            break
        except:
            time.sleep(0.1488)
    sys.stderr.write(" done.\n")

def login(username, password):
    driver.get("http://weibo.com/login.php")
    wait_for(".W_login_form .info_list")
    time.sleep(2)
    driver.find_element_by_css_selector(".inp.username input").send_keys(username)
    driver.find_element_by_css_selector(".inp.password input").send_keys(password)
    time.sleep(15)

def get_page(query, max_pages=1):
    res = []
    for page in xrange(1, max_pages+1):
        driver.get("http://s.weibo.com/wb/%s&xsort=hot&page=%d" % (urllib.quote(query.encode("utf-8")), page))
        wait_for("dd.content")
        elems = driver.find_elements_by_css_selector("dd.content")
        for i in elems:
            d = {
                "userId":     int("0"+digits(i.find_element_by_css_selector("p a").get_attribute('suda-data')[-15:])),
                "retweets":   int("0"+digits(i.find_element_by_css_selector("p i+a").text)),
                "likes":      int("0"+digits(i.find_element_by_css_selector("p.info a").text)),
                "text":       i.find_element_by_css_selector("em").text
            }
            res += [d]
    return res


def get_followers(uid, max_pages = 10):
    followers = []
    driver.get("http://weibo.com/%s/fans" % uid)
    wait_for(".S_line1")
    for page in xrange(1, max_pages+1):
        driver.get("http://weibo.com/p/100505%s/follow?relate=fans&page=%d" % (uid, page))
        wait_for("ul.cnfList")
        elems = driver.find_elements_by_css_selector("ul.cnfList div.connect")

        for i in elems:
            d = {
                "following":  int("0"+digits(i.find_element_by_css_selector("a").text)),
                "followers":  int("0"+digits(i.find_element_by_css_selector("a+i+a").text)),
                "tweets":     int("0"+digits(i.find_element_by_css_selector("a+i+a+i+a").text)),
                "userId":     int("0"+digits(i.find_element_by_css_selector("a+i+a+i+a").get_attribute("href")))
            }
            followers += [d]
        print json.dumps(followers)
        followers = []

def get_following(uid, max_pages = 10):
    following = []
    driver.get("http://weibo.com/%s/follow" % uid)
    wait_for(".S_line1")
    account_type = str(digits(driver.find_element_by_css_selector(".W_pages a+a").get_attribute("href")))[:6]
    for page in xrange(1, max_pages+1):
        driver.get("http://weibo.com/p/%s%s/follow?page=%d" % (account_type, uid, page))
        print "http://weibo.com/p/%s%s/follow?page=%d" % (account_type, uid, page)
        wait_for("ul.cnfList")
        elems = driver.find_elements_by_css_selector("ul.cnfList div.connect")

        for i in elems:
            d = {
                "following":  int("0"+digits(i.find_element_by_css_selector("a").text)),
                "followers":  int("0"+digits(i.find_element_by_css_selector("a+i+a").text)),
                "tweets":     int("0"+digits(i.find_element_by_css_selector("a+i+a+i+a").text)),
                "userId":     int("0"+digits(i.find_element_by_css_selector("a").get_attribute("href")))
            }
            following += [d]

    filename = str(uid)+'.json'
    with open(filename,'w') as outfile:
        json.dump(following,outfile)




if __name__ == "__main__":
    for user in users:
        chromeOptions = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.set_script_timeout(1)
        login('ipestrov@gmail.com', '1234Sina1234*')
        get_following(user, 10)
        driver.quit()
