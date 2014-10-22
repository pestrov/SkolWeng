# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib

import time

import re


query = u'研究'

driver = webdriver.Chrome()
driver.get("http://s.weibo.com/wb/%s&xsort=hot" % urllib.quote(query.encode("utf-8")))

time.sleep(10)
elems = driver.find_elements_by_css_selector("dd.content")

for i in elems:
    print "user", i.find_element_by_css_selector("p a").get_attribute('suda-data')
    #print "likes", i.find_element_by_css_selector("p.info a").text
    #print "likes", i.find_element_by_css_selector("p.info a").text
    print "likes", i.find_element_by_css_selector("p.info a").text
