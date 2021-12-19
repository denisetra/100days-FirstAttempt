import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

##Disable pop-ups in chrome, both in-browser and out.
option = Options()  # Creating instance
option.add_argument('--disable-notifications') # modify Default Notification


TINDER_NAME = os.environ['LOGIN']
TINDER_PWD = os.environ['PWD']
FB_EMAIL = os.environ['FB_EMAIL']
FB_PWD = os.environ['FB_PWD']
s = Service('C:\\Program Files\\Google\\chromedriver.exe')
driver = webdriver.Chrome(service=s, chrome_options=option)

def tinder_login():
    login_page = 'https://tinder.com/'
    driver.get(login_page)
    time.sleep(3)
    login_button = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    login_button.click()
    time.sleep(5)
    facebook_login_button = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login_button.click()
    time.sleep(3)
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    #print(f'PRE:{driver.title}')
    email_box = driver.find_element(By.XPATH, '//*[@id="email"]' )
    email_box.send_keys(FB_EMAIL)
    pwd_box = driver.find_element(By.XPATH, '//*[@id="pass"]')
    pwd_box.send_keys(FB_PWD)
    log_in= driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
    log_in.click()
    time.sleep(5)
    driver.switch_to.window(base_window)
    accept_cookies = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button')
    accept_cookies.click()
    time.sleep(6)

def dislike_tinder():
    n = 5
    for item in range(n):
        try:
            # dwn_btn = '//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span'
            # down_button = driver.find_element(By.XPATH, dwn_btn)
            # down_button.click()
            actions = ActionChains(driver)
            actions.send_keys(Keys.ARROW_LEFT)
            actions.perform()
            time.sleep(2)

            n -= 1
            print('Moving on to next person')
        except NoSuchElementException:
            print(f'{num}, failed, sleeping 4 seconds')
            time.sleep(4)





