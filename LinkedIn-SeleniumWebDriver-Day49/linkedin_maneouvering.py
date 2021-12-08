import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOGIN = os.environ['LINKEDIN_LOGIN']
PWD = os.environ['LINKEDIN_PWD']
s = Service('C:\\Program Files\\Google\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

def signin():
    login_page = 'https://www.linkedin.com/home'
    driver.get(login_page)
    log_in = driver.find_element(By.LINK_TEXT, 'Sign in')
    log_in.click()
    name = driver.find_element(By.ID, 'username')
    name.send_keys(LOGIN)
    pwd = driver.find_element(By.ID, 'password')
    pwd.send_keys(PWD)
    synin = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    synin.click()


def job_search():
    link_list = []
    # Job search terms "python" and 'Remote' and 'Easy Apply'
    linkedin_search = 'https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&keywords=python'
    driver.get(linkedin_search)
    links = driver.find_elements(By.CLASS_NAME, 'job-card-list')
    for item in links:
        my_link = item.find_element(By.TAG_NAME, 'a')
        link_list.append(my_link.get_attribute('href'))

    for job in link_list:
        driver.get(job)
        save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
        save_button.click()








