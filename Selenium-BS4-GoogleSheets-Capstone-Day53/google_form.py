import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver.v2 as uc
options = uc.ChromeOptions()
GOOGLE_LOGIN = 'xxx'
GOOGLE_PWD = 'xxx'
s = Service('C:\\Program Files\\Google\\chromedriver.exe')
## Using Undetected_Chromedriver as chromedriver no longer works with google.
options.user_data_dir = 'C:\\temp\\profile'
options.add_argument('--user-data-dir=C:\\temp\\profile2')
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)
## create a form, populate it with the scraped data.
my_form = 'https://docs.google.com/forms/d/e/1FAIpQLScG3RosgJG9a5Vv_whVdjCCMf0tzka9mLGJ1JQh4XcKF9UVlg/viewform'
google_sign = 'https://accounts.google.com/signin/v2/challenge/pwd?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward&TL=AM3QAYawhnRn-cds80UGRM-e7N41U5BlT31V34A5Be-jDimaS3K6mjaMb4hQNSMk'
##Disable pop-ups in chrome, both in-browser and out.
#option = Options()  # Creating instance
#option.add_argument('--disable-notifications') # modify Default Notification

#driver = webdriver.Chrome(service=s, options=option)
def login():
    try:
        go_sign_in = driver.find_element(By.XPATH, '//*[@id="SMMuxb"]/a[1]')
        go_sign_in.click()
        login_window = driver.window_handles[1]
        driver.switch_to.window(login_window)
        time.sleep(2)
        log_me_in = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        log_me_in.send_keys(GOOGLE_LOGIN)
        time.sleep(2)
        next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
        next_button.click()
        time.sleep(2)
        pwd_button = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        pwd_button.send_keys(GOOGLE_PWD)
        time.sleep(2)
        second_next = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
        second_next.click()
        time.sleep(2)
    except NoSuchElementException:
        pass

def fill_out_form(listings):  ## using Selenium
    driver.get(my_form)
    login()
    print('Starting_To_Fill_Up_form...')
    num_items = len(listings)
    num = 1
    for key,value in listings.items():
        print(f'Adding {num} of {num_items}')
        address = key
        link = value[0]
        price = value[1]

        add_address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        add_address.send_keys(address)

        add_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        add_link.send_keys(link)

        add_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        add_price.send_keys(price)

        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()
        time.sleep(2)

        another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another.click()
        time.sleep(2)

    # go to Responses tab
    my_full_form = 'https://docs.google.com/forms/d/1njDoiPOdalPVGW2FEQzRByjzGWKuO8byU3qDEiyAKNk/edit?usp=sharing'
    driver.get(my_full_form)
    time.sleep(5)
    responses = driver.find_element(By.XPATH, '//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]')
    responses.click()
    print('On responses now')
    print(driver.window_handles)
    time.sleep(1)

    # go to sheets
    sheet = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div')
    sheet.click()

    time.sleep(2)
    input('')

    driver.quit()
