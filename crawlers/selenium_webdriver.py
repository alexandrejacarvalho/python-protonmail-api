from config import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def selenium_webdriver():
    # print('Starting webdriver...')

    options = Options()
    # options.headless = True

    return webdriver.Chrome(CHROMEDRIVER_PATH, options=options)


def selenium_webdriver_login(driver, email, password):
    # print('Starting login...')

    wait = WebDriverWait(driver, 10)

    driver.get('https://mail.protonmail.com/login')

    wait.until(EC.element_to_be_clickable((By.ID, 'username')))

    driver.find_element_by_id('username').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_id('login_btn').click()

    # check if the page loaded by waiting for button "COMPOSE to be clickable
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pm_sidebar"]/button')))

    # print('Login Done!')

    return driver
