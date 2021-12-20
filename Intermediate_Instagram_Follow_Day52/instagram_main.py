import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

##Disable pop-ups in chrome, both in-browser and out.
option = Options()  # Creating instance
option.add_argument('--disable-notifications') # modify Default Notification

INSTA_LOGIN = os.environ['INSTAGRAM_LOGIN']
INSTA_PW = os.environ['INSTAGRAM_PW']
SIMILAR_ACCOUNT = 'https://www.instagram.com/100daysofcode._/'
s = Service('C:\\Program Files\\Google\\chromedriver.exe')
INSTAGRAM = 'https://www.instagram.com/accounts/login/'


class InstaFollower():
    def __init__(self, s, option):
        self.driver = webdriver.Chrome(service=s, options=option)



    def login(self, INSTAGRAM, INSTA_LOGIN):
        self.driver.get(INSTAGRAM)
        time.sleep(3)
        login_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_name.send_keys(INSTA_LOGIN)
        login_pw = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_pw.send_keys(INSTA_PW)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()
        ## code below to NOT save login info.
        time.sleep(5)
        not_save = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_save.click()


        pass


    def find_followers(self, SIMILAR_ACCOUNT):
        global follow_buttons
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        print(f'StartingHeight={last_height}')

        follower_list = self.driver.find_element(By.XPATH,'/html/body/div[6]').click()

        time.sleep(10)

        pop_up = self.driver.find_element(By.CSS_SELECTOR,'.isgrP')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            time.sleep(2)
        follow_buttons = self.driver.find_elements(By.TAG_NAME, 'button')


    def follow(self):
        for button in follow_buttons:
            if button.text != 'Follow':
                pass
            else:
                button.click()
                time.sleep(2)
        print('done!')






bot = InstaFollower(s,option)
bot.login(INSTAGRAM, INSTA_LOGIN)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
