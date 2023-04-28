import pickle
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import random
import pandas as pd
from selenium.webdriver.common.proxy import Proxy, ProxyType

def browser_cookie(path):
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_extension("proxy.zip")
    #chrome_options.add_argument(
    #'--proxy-server=%s' % proxy)

    browser = webdriver.Chrome(
    executable_path=path, options=chrome_options)

    return browser

browser5 = browser_cookie("./chromedriver5/chromedriver.exe")
print("xxxxxxx")
# 2. Mở thử một trang web
cookies5 = pickle.load(open("my_cookie_5.pkl", "rb"))
for cookie in cookies5:
    browser5.add_cookie(cookie)
print("xxxxxxx")
sleep(random.randint(6, 8))
# 3. Refresh the browser

browser5.get("https://m.facebook.com")  # mbasic
sleep(random.randint(3, 6))

browser5.get("https://mbasic.facebook.com/lam.latleo.3?v=timeline")

#timeLineBtn = browser1.find_element(
#    By.XPATH, '//a[contains(@href, "?v=timeline")]').click()

sumLinks = []

x = 1
z = 0
while x == 1 and z<40:
    try:
        likeBtn = browser5.find_elements(
            By.XPATH, '//*[contains(@id, "like_")]')
        if len(likeBtn):
            for id in likeBtn:
                idPost = id.get_attribute('id').replace("like_", "")
                if (idPost not in sumLinks):
                    sumLinks.append(idPost)
                    # print(idPost)
        nextBtn = browser5.find_element(
            By.XPATH, '//a[contains(@href, "?cursor")]').click()
        z += 1
        if z%2==0:
            sleep(random.randint(10, 15))
        else:
            sleep(random.randint(15, 20))
        
    except:
        # print("next")
        x = 0

browser5.close()
browser5.quit()

browser3 = browser_cookie("./chromedriver3/chromedriver.exe")
browser4 = browser_cookie("./chromedriver.exe")

cookies3 = pickle.load(open("my_cookie_3.pkl", "rb"))
for cookie in cookies3:
    browser3.add_cookie(cookie)

cookies4 = pickle.load(open("my_cookie_4.pkl", "rb"))
for cookie in cookies4:
    browser4.add_cookie(cookie)

sleep(random.randint(6, 8))

browser3.get("https://mbasic.facebook.com/lam.latleo.3?v=timeline")
browser4.get("https://mbasic.facebook.com/lam.latleo.3?v=timeline")

sleep(random.randint(6, 8))

# print("111111111111")
user_all_post_data = []
user_all_post_data_columns = ['PostID', 'Content']

y = 1
for postId in sumLinks:
    try:
        if y == 1:
            browser = browser3
        else:
            browser = browser4

        
        browser.get("https://mbasic.facebook.com/" + postId)
        sleep(random.randint(2, 5))
        # print(postId)

        try:
            postContent = browser.find_element(
                By.XPATH, '//div[@data-ft=\'{"tn":"*s"}\']/div').text
            # print(postContent)
        except:
            postContent = ''

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
                #browser.get(vi.get_attribute('href'))
                # browser.find_element(By.TAG_NAME, 'body').send_keys(
                # Keys.CONTROL + Keys.TAB)

                v = vi.get_attribute('href')
                post_img_vid.append([v])
                # post_img_vid.append([browser.current_url])
                # browser.close()
                # browser.back()
        # print("22")
        except:
            x = 0

        df = pd.DataFrame(post_img_vid, columns=post_img_vid_columns)
        df.to_json(postId + '.json', orient="records")
        # print(postId)
        # print(postContent)
        user_all_post_data.append([postId, postContent])
        if y==2:
            y = 1
        else:
            y += 1

    except:
        print(postId + " - xxx")

df = pd.DataFrame(user_all_post_data, columns=user_all_post_data_columns)
df.to_json('user_all_post_data.json', orient="records")

browser3.close()
browser3.quit()

browser4.close()
browser4.quit()
