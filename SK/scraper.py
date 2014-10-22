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
    time.sleep(8)
    #driver.execute_script("document.getElementsByClassName('login_btn')[1].getElementsByTagName('a')[0].click();")
    #driver.execute_script("alert('Now click the button.')")
    #wait_for(".send_weibo")

def get_page(query, page=0):
    driver.get("http://s.weibo.com/wb/%s&xsort=hot" % urllib.quote(query.encode("utf-8")))

    wait_for("dd.content")
    res = []
    elems = driver.find_elements_by_css_selector("dd.content")
    for i in elems:
        d = {
            "userId":     int("0"+digits(i.find_element_by_css_selector("p a").get_attribute('suda-data')[-15:])),
            "retweets":   int("0"+digits(i.find_element_by_css_selector("p i+a").text)),
            "likes":      int("0"+digits(i.find_element_by_css_selector("p.info a").text))
        }
        res += [d]

    return res


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.set_script_timeout(1)
    login('ipestrov@gmail.com', '1234Sina1234*')
    print get_page(u'研究')
    driver.quit()
