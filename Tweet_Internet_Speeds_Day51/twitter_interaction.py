import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

##Disable pop-ups in chrome, both in-browser and out.
option = Options()  # Creating instance
option.add_argument('--disable-notifications') # modify Default Notification

s = Service('C:\\Program Files\\Google\\chromedriver.exe')
SPEED_TEST = 'https://www.speedtest.net/'
TWITTER_NAME = os.environ['LOGIN']
TWITTER_PWD = os.environ['PWD']
TWITTER_LINK = 'https://twitter.com/i/flow/login'
TWEET_TO = os.environ['TWEET_TO']
G_LOGIN = os.environ['G_LOGIN']
G_PWD = os.environ['G_PWD']
MIN_DOWNSTREAM = 150
MIN_UPSTREAM = 10

class InternetSpeedTwitterBot():
    def __init__(self, driver_path,option):
        self.driver = webdriver.Chrome(service=driver_path,options=option)
        self.down = 0
        self.up = 0


    def get_internet_speed(self,speed_test):
        self.driver.get(speed_test)
        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        print('Running Speed-Test')
        time.sleep(5)
        while self.down == 0:
            try:
                d_s = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
                ds_text = d_s.text
                try:
                    my_float = float(ds_text)
                    if my_float > 0:
                        self.down = my_float
                except ValueError:
                    pass
            except NoSuchElementException:
                time.sleep(10)
        while self.up == 0:
            try:
                u_s = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span' )
                us_text = u_s.text
                try:
                    us_float = float(us_text)
                    if us_float > 0:
                        self.up = us_float
                except ValueError:
                    pass
            except NoSuchElementException:
                time.sleep(5)
        print(f'My Downstream is: {self.down}')
        print(f'My Upstream is: {self.up}')
        #self.driver.close()
        time.sleep(5)

    def tweet_at_provider(self,TWITTER_LINK,TWITTER_NAME,TWITTER_PWD,TWEET_TO):
        self.driver.get(TWITTER_LINK)
        time.sleep(5)
        #sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a')
        #sign_in.click()
        #time.sleep(10)
        twitter_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        twitter_username.send_keys(TWITTER_NAME)
        time.sleep(10)
        nx='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]'
        next_bttn = self.driver.find_element(By.XPATH, nx)
        next_bttn.click()
        time.sleep(10)
        pwd_bttn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        pwd_bttn.send_keys(TWITTER_PWD)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        log_in_button.click()
        ## Logged in at this point.
        time.sleep(10)
        twitter_message = f'My current Downstream internet speed is {self.down}MB/s, and my current Upstream speed is {self.up}MB/s!'
        my_message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        my_message.send_keys(twitter_message)
        tweet_button= '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div'
        go_tweet = self.driver.find_element(By.XPATH, tweet_button )
        go_tweet.click()
        









bot = InternetSpeedTwitterBot(s,option)
bot.get_internet_speed(SPEED_TEST)
bot.tweet_at_provider(TWITTER_LINK,TWITTER_NAME,TWITTER_PWD,TWEET_TO)
