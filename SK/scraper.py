# -*- coding: utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
import urllib
import time
import re
import sys
import json
dstrip = re.compile('[^0-9]+')
users = [1853472775, 1626443785, 2243807243, 2401518092, 2165090317, 3235040884, 1642482194, 1682207150, 2847927727, 1639498782, 31263317424, 3034112034, 2201904677, 1651428902, 1703371307, 2248789552, 2011075080, 1823975091, 1650111241, 1859586112, 1784473157, 3225231435, 1684452940, 1407365952, 1850988623, 2286908003, 1191965271, 1722022490, 2496234595, 1986926181, 3928493164, 1787830893, 3288976495, 2230312052, 1069205631, 1720962692, 1751714412, 3908755088, 1747341974, 1241679004, 2217035934, 2397485727, 1814040741, 1796445350, 1734530730, 2051826355, 1904769205, 1771925961, 2000961721, 1709331645, 5335840456, 1735047885, 2100623570, 1641561812, 5155790040, 1851755225, 2089800791, 2712029404, 2800982237, 1644489953, 1749990115, 5340716263, 1625293545, 1225314032, 5120783603, 1823887605, 1729332983, 2098122492, 1195347197, 1745719040, 1649159940, 1323527941, 1873625985, 2458873097, 1314608344, 5078366996, 1657430300, 2088247582, 1677759264, 3763936545, 2737798435, 1988800805, 2215269084, 1709157165, 3817394480, 1774057271, 2439854907, 3830136640, 1873722533, 1806128454, 2696713033, 2810719061, 1663414103, 5245490013, 1974576991, 1338623632, 2189496674, 1663937380, 1735209835, 2826139505, 1256947091, 1642634100, 1649173367, 1666177401, 3446047612, 2280198017, 1887790981, 1414148492, 2065032077, 5016338752, 1891924883, 1722628512, 32935509413, 3237705130, 1642632622, 2230913455, 1945805232, 1699909555, 3232339102, 2849964471, 2418433987, 2499096521, 5333644235, 11751195602, 1901447125, 1699432410, 1961594843, 1298535315, 5288801759, 1878363622, 1924842983, 2410528240, 1663072851, 1779837945, 3355295740, 1653460650, 1642088277]

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
    for page in xrange(1, max_pages+1):
        driver.get("http://weibo.com/p/100505%s/follow?page=%d" % (uid, page))
        wait_for("ul.cnfList")
        elems = driver.find_elements_by_css_selector("ul.cnfList div.connect")

        for i in elems:
            d = {
                "following":  int("0"+digits(i.find_element_by_css_selector("a").text)),
                "followers":  int("0"+digits(i.find_element_by_css_selector("a+i+a").text)),
                "tweets":     int("0"+digits(i.find_element_by_css_selector("a+i+a+i+a").text)),
                "userId":     int("0"+digits(i.find_element_by_css_selector("a").get_attribute("href")))
            }
            #print i.find_element_by_css_selector("a").get_attribute("href")
            following += [d]
        filename = str(uid)+'.json'
        with open(filename,'w') as outfile:
            json.dump(following,outfile)
        following = []




if __name__ == "__main__":
    for user in users:
        chromeOptions = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.set_script_timeout(1)
        login('ipestrov@gmail.com', '1234Sina1234*')
        get_following(user, 3)
        driver.quit()
