# -*- coding: utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
import urllib
import time
import re
import sys

dstrip = re.compile('[^0-9]+')
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
    driver.find_element_by_css_selector(".inp.username input").send_keys(username)
    driver.find_element_by_css_selector(".inp.password input").send_keys(password)
    #driver.find_element_by_css_selector(".info_list.login_btn a").click()
    time.sleep(15)
    #driver.execute_script("document.getElementsByClassName('login_btn')[1].getElementsByTagName('a')[0].click();")
    #driver.execute_script("alert('Now click the button.')")
    #wait_for(".send_weibo")

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

def get_followers(uid, max_pages = 1):
    followers = []
    for page in xrange(1, max_pages+1):
        #print ("http://weibo.com/p/%d/follow?relate=fans&page=%d" % (uid, page))
        driver.get("http://weibo.com/p/%d/follow?relate=fans&page=%d" % (uid, page))

        wait_for("ul.cnfList")
        elems = driver.find_elements_by_css_selector("ul.cnfList div.connect")
        #print elems
        #print elems[1]
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
    #return followers

if __name__ == "__main__":
    chromeOptions = webdriver.ChromeOptions()
    #prefs = {"profile.default_content_settings.images": 2}
    prefs = {}
    chromeOptions.add_experimental_option("prefs", prefs)
    #chromeOptions.add_argument("--disable-javascript")
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.set_script_timeout(1)
    login('ipestrov@gmail.com', '1234Sina1234*')
    #print get_followers(1002063206472652,20)
    #print get_page(sys.argv[1].decode('utf-8'), 50)
    driver.quit()
