# -*- coding: utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
import urllib
import time
import re

dstrip = re.compile('[^0-9]+')
def digits(s):
    return dstrip.sub('', s)

query = u'研究'

driver = webdriver.Chrome()
driver.get("http://s.weibo.com/wb/%s&xsort=hot" % urllib.quote(query.encode("utf-8")))

while True:
    try:
        elems = driver.find_elements_by_css_selector("dd.content")
        break
    except:
        time.sleep(0.1488)

for i in elems:

    d = {
        "userId":     int("0"+digits(i.find_element_by_css_selector("p a").get_attribute('suda-data')[-15:])),
        "retweets":   int("0"+digits(i.find_element_by_css_selector("p i+a").text)),
        "likes":      int("0"+digits(i.find_element_by_css_selector("p.info a").text))
    }
    print d

driver.close()
