from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import random
import pandas as pd
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#chrome_options = webdriver.ChromeOptions()
"""
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-notifications")
"""
chrome_options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

browser = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=chrome_options)
# browser.close()
browser.get("http://m.facebook.com")  # mbasic

txtUser = browser.find_element(By.ID, "m_login_email")
txtUser.send_keys("nguyenbababa88@gmail.com")

txtPass = browser.find_element(By.XPATH, '//*[@id="m_login_password"]')
txtPass.send_keys("QqqPPassword99.     ")

txtPass.send_keys(Keys.ENTER)

sleep(5)

"""
browser.get(
    "https://www.facebook.com/?sk=welcome&tbua=1")  # https://www.facebook.com/?sk=welcome&tbua=1
sleep(3)

search_link = browser.find_element(By.XPATH, '//span[@class="_7iz_"]')
search_link.click()
sleep(4)


search = browser.find_element(
    By.XPATH, '//input[@aria-label="Tìm kiếm trên Facebook"]')  # Tìm kiếm trên Facebook Tìm kiếm theo tên
search.click()
search.click()
search.send_keys(input('Enter your keyword:'))  # input('Enter your keyword:')
search.send_keys(Keys.ENTER)
sleep(6)
"""
link = "https://www.facebook.com/search/top?q="
kw = input('Enter your keyword:')  # input('Enter your keyword:')
link = link + kw
browser.get(link)
sleep(3)
"""
people = browser.find_element(
    By.XPATH, '//span[contains(text(), "Mọi người")]')  # //span[contains(text(), "Mọi người")] //i[@class="x1b0d499 xaj1gnb"]
people.click()
sleep(3)
"""
people = "https://www.facebook.com/search/people/?q=" + kw
browser.get(people)
sleep(2)
SCROLL_PAUSE_TIME = 6

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


users_data_columns = ['userNam', 'Profile_link']
users_data = []
users = browser.find_elements(
    By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]')
for user in users:
    user_link = user.get_attribute('href')
    path = "//a[@href=" + '"' + user_link + '"' + "]/span/div/div/span/div"
    try:
        verified = browser.find_element(
            By.XPATH, path).get_attribute("aria-label")
    except:
        verified = "Chưa được xác minh"
    users_data.append([user.text, user_link, verified])

df2 = pd.DataFrame(users_data, columns=users_data_columns)
print(df2)
df2.to_csv('fb_keyword_people_data.csv')
