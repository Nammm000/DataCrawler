import pickle
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
"""
proxyList = [
    '116.98.191.244:10003'
    # '216.215.123.174:8080'
    # '50.174.7.152:80'
]

chrome_options.add_argument(
    '--proxy-server=%s' % random.choice(proxyList))
"""
# chrome_options.add_extension("proxy.zip")
browser = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=chrome_options)

# 2. Mở thử một trang web
browser.get("https://m.facebook.com")  # mbasic

cookies = pickle.load(open("my_cookie.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# 3. Refresh the browser
sleep(2)
browser.get("https://m.facebook.com")

browser.get("https://mbasic.facebook.com/groups/vieclamCNTTDaNang")
sumLinks = []

x = 1
while x == 1:
    try:
        likeBtn = browser.find_elements(
            By.XPATH, '//*[contains(@id, "like_")]')
        if len(likeBtn):
            for id in likeBtn:
                idPost = id.get_attribute('id').replace("like_", "")
                if (idPost not in sumLinks):
                    sumLinks.append(idPost)
                    # print(idPost)
        nextBtn = browser.find_element(
            By.XPATH, '//a[contains(@href, "?bacr")]').click()
        sleep(6)
        # if (len(nextBtn)):
        # nextBtn.click()
        # print("next")
        # sleep(6)
    except:
        x = 0


# print("111111111111")
post_data = []
post_data_columns = ['PostID', 'Poster', 'PosterLink', 'Content']
# reaction //a[contains(@href, "/reaction/profile")]/div/div

for postId in sumLinks:
    try:
        browser.get("https://mbasic.facebook.com/" + postId)
        sleep(6)
        # print(postId)

        try:
            poster = browser.find_element(
                By.XPATH, '//h3/span/strong[1]/a')
            posterText = poster.text
            posterLink = poster.get_attribute('href')
            # print(posterText)
            # print(posterLink)
        except:
            posterText = 'x'
            posterLink = 'x'

        try:
            postContent = browser.find_element(
                By.XPATH, '//div[@data-ft=\'{"tn":"*s"}\']/div').text
            # print(postContent)
        except:
            postContent = 'x'

        post_img_vid = []
        post_img_vid_columns = ['Link']
        try:
            postImg = browser.find_elements(
                By.XPATH, '//div/div/a/img')  # //div[@data-ft='{\"tn\": \"H\"}']/div/a/img
            # print("23")
            post_img_vid = []
            # print("24")
            for img in postImg:
                post_img_vid.append([img.get_attribute('src')])

            # print("333")

        except:
            x = 0

        try:
            postVideo = browser.find_elements(
                By.XPATH, '//div/div/a/div/img/../..')  # //div/div/a/div/img
            for vi in postVideo:
                post_img_vid.append([vi.get_attribute('href')])
                # browser.find_element(By.TAG_NAME, 'body').send_keys(
                # Keys.CONTROL + Keys.TAB)

                #post_img_vid.append([browser.current_url]) lay current_url
                # browser.close()
                # browser.back()
        # print("22")
        except:
            x = 0

        df = pd.DataFrame(post_img_vid, columns=post_img_vid_columns)
        df.to_json(postId + '.json', orient="records")
        # print(postId)
        # print(posterText)
        # print(posterLink)
        # print(postContent)
        post_data.append([postId, posterText, posterLink, postContent])

    except:
        print(postId + " - xxx")

df = pd.DataFrame(post_data, columns=post_data_columns)
df.to_json('post_data.json', orient="records")

browser.close()
# browser.quit()
