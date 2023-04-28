from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import random
import pandas as pd
#from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_options = Options()

chrome_options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

proxyList = [
    '116.98.191.244:10003'
    # '216.215.123.174:8080'
    # '50.174.7.152:80'
]


chrome_options.add_argument(
    '--proxy-server=%s' % random.choice(proxyList))

# chrome_options.add_extension("proxy.zip")
browser = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=chrome_options)
# browser.close()
browser.get("https://m.facebook.com")  # mbasic

txtUser = browser.find_element(By.ID, "m_login_email")
txtUser.send_keys("nba5167036@gmail.com")

txtPass = browser.find_element(By.XPATH, '//*[@id="m_login_password"]')
txtPass.send_keys("QqqPPassword99. ")  # QqqPPassword99.     #

txtPass.send_keys(Keys.ENTER)

sleep(9)

llink = "https://m.facebook.com/le.mink.5"
link = llink.split("com/")[1]
mlink = "https://m.facebook.com/" + link
wlink = "https://www.facebook.com/" + link


sleep(9)

browser.get(mlink + "/friends")

last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

friends_data = []
friends_data_columns = ['Name', 'Link']

followers_data = []

try:
    followers = browser.find_elements(
        By.XPATH, '//div[@class="item _1zq- tall acw abt"]/a')

    lenn = len(followers)
    for i in range(0, lenn):
        friends_data.append(
            [followers[i].text, followers[i].get_attribute('href')])

    df = pd.DataFrame(followers_data, columns=friends_data_columns)
    df.to_json('followers_data.json', orient="records")
except:
    followers = "0"

try:
    friends = browser.find_elements(
        By.XPATH, '//div[@class="_84l2"]/*[@class="_52jh _5pxc _8yo0"]/a')

    lenn = len(friends)
    for i in range(0, lenn):
        friends_data.append(
            [friends[i].text, friends[i].get_attribute('href')])

    df = pd.DataFrame(friends_data, columns=friends_data_columns)
    df.to_json('friends_data.json', orient="records")
except:
    friends = "0"

browser.close()
# browser.quit()
