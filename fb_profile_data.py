from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import random
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_options = Options()

chrome_options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

proxyList = [
    '112.137.142.8:3128'
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
txtUser.send_keys("nguyenbababa88@gmail.com")

txtPass = browser.find_element(By.XPATH, '//*[@id="m_login_password"]')
txtPass.send_keys("QqqPPassword99.     ")

txtPass.send_keys(Keys.ENTER)

sleep(3)

llink = "https://www.facebook.com/nammpeo226"
link = llink.split("com/")[1]
mlink = "https://mbasic.facebook.com/" + link
wlink = "https://www.facebook.com/" + link

profile_data_columns = ['UserName', 'Profile_image', 'Background_image', 'Intro', 'Home_town', 'Current_town/city',
                        'Date_of_birth', 'Gender', 'Joined_on', 'Follower', 'Nickname', 'Profile_link']
other_profile_data_columns = ['Contact_info', 'Family_member', 'University',
                              'University_time', 'High_School', 'High_School_time', 'Work', 'Work_time', 'Relationship ']

profile_data = []
other_profile_data = []

browser.get(wlink)  # mbasic link post
sleep(3)
#comment_list = browser.find_elements(By.XPATH, '//div[@class="_2a_i"]')
#print("***", type(comment_list))

userName = browser.find_element(
    By.XPATH, '//div[@class="x78zum5 xdt5ytf x1wsgfga x9otpla"]/div/span/h1').text
# //div[@class="x78zum5 xdt5ytf x1wsgfga x9otpla"]/div[@class="x1e56ztr x1xmf6yo"]/
# span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso
# x1gmr53x x1cpjm7i x1fgarty x1943h6x x14qwyeo xw06pyt x579bpy xjkpybl x1xlr1w8 xzsf02u x1yc453h"]/h1
# //div[@class=""]/h1[@class="x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"]
# //div/div/span/div/h1[@class="x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"]
try:
    try:
        profile_image = browser.find_element(By.XPATH,
                                             '//div[@class="x1jx94hy x14yjl9h xudhj91 x18nykt9 xww2gxu x1iorvi4 x150jy0e xjkvuk6 x1e558r4"]/div/*[1]/*[2]/*[1]').get_attribute('xlink:href')
    except:
        profile_image = browser.find_element(By.XPATH,
                                             '//a[@role="link"]/div[@class="x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z"]/*[@role="img"]/*[2]/*[1]').get_attribute('xlink:href')
except:
    profile_image = "0"

try:
    background_image = browser.find_element(By.XPATH,
                                            '//img[@data-imgperflogname="profileCoverPhoto"]').get_attribute('src')
except:
    background_image = "0"

try:
    intro = browser.find_element(
        By.XPATH, '//div[@class="x2b8uid xdppsyt x1l90r2v"]/span').text
except:
    intro = "0"

browser.get(mlink)
sleep(3)

try:
    joinedOn = browser.find_element(
        By.XPATH, '//i[@class="_3-90 img sp_kLxvoX_vJ0L sx_ced215"]/../../../div[2]/div/div/div/span').text
except:
    joinedOn = "0"

try:
    home_town = browser.find_element(
        By.XPATH, '//i[@class="_3-90 img sp_kLxvoX_vJ0L sx_54abd0"]/../../../div[2]/div/div/div/span/strong/span').text
except:
    home_town = "0"

try:
    current_town = browser.find_element(
        By.XPATH, '//i[@class="_3-90 img sp_kLxvoX_vJ0L sx_abdaf2"]/../../../div[2]/div/div/div/span/strong/span').text
except:
    current_town = "0"

try:
    follower = browser.find_element(
        By.XPATH, '//i[@class="_3-90 img sp_kLxvoX_vJ0L sx_bcd225"]/../../../div[2]/div/div/div/span').text
    follower = follower.split(" ")[1]
except:
    follower = "0"

aboutLink = mlink + "/about"
browser.get(aboutLink)
sleep(2)

basicInfo = browser.find_elements(By.XPATH,
                                  '//div[@id="basic-info"]/div[@class="_55x2 _5ji7"]/div[@class="_5cds _2lcw _5cdu"]/div[@class="lr"]/div[@class="_5cdv r"]')
gender = ""
dob = ""
if len(basicInfo) == 0:
    gender = "0"
    dob = "0"
if len(basicInfo) == 1:
    gender = basicInfo[0].text
    dob = "0"
if len(basicInfo) == 2:
    gender = basicInfo[1].text
    dob = basicInfo[0].text

try:
    nickName = browser.find_element(By.XPATH,
                                    '//div[@id="nicknames"]/div/div/div/div[@class="_5cdv r"]').text
except:
    nickName = "0"

profile_data.append([userName, profile_image, background_image, intro,
                     home_town, current_town,
                     dob, gender, joinedOn, follower, nickName, wlink])

df = pd.DataFrame(profile_data, columns=profile_data_columns)

print(df)
df.to_csv('fb_profiles_data.csv')
