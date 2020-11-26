# -*- coding:utf-8 -*-
import os
import time

from selenium import webdriver
from bs4 import BeautifulSoup

# dotenv init
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY_NAME = os.getenv("NAME")
SECRET_KEY_PW = os.getenv("PW")

###
#
# selenium setting
#
###
_chrome_options = webdriver.ChromeOptions()
_chrome_options.add_argument('disable-infobars')
_chrome_options.add_argument('headless')
_chrome_options.add_argument("lang=ko_KR")
_chrome_options.add_argument('--no-sandbox')
_chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver', options=_chrome_options)


def login():
    driver.get(
        'https://www.instagram.com/accounts/login/?source=auth_switcher'
    )
    time.sleep(3)

    id_input = driver.find_elements_by_css_selector(
        '#loginForm > div > div:nth-child(1) > div > label > input'
    )[0]
    id_input.send_keys(SECRET_KEY_NAME)
    password_input = driver.find_elements_by_css_selector(
        '#loginForm > div > div:nth-child(2) > div > label > input'
    )[0]
    password_input.send_keys(SECRET_KEY_PW)
    password_input.submit()
    driver.save_screenshot("1.png")

    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/div/button'
    ).click()

    
    driver.save_screenshot("2.png")


def search(word):
    driver.get('https://www.instagram.com/explore/tags/%s' % (word))
    time.sleep(3)
    driver.save_screenshot("tmp.png")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.html.body.find_all("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 1초 대기
    time.sleep(1)


login()
search('행복')
driver.quit()















