from .selenium_webdriver import *
from config import *
import sys


def inbox_get_by_page(page):
    selenium_driver = selenium_webdriver()
    driver = selenium_webdriver_login(selenium_driver, EMAIL, PASSWORD)

    wait = WebDriverWait(driver, 20)

    # print('Starting email crawling...')

    if page is not 1:
        driver.get("https://mail.protonmail.com/inbox?page=" + str(page))

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="conversation-list-rows"]/section/div[1]')))


    emails = []

    row = 1
    while True:
        email_div_xpath = '//*[@id="conversation-list-rows"]/section/div[' + str(row) + ']'

        try:
            email_div = driver.find_element_by_xpath(email_div_xpath)

            sender = driver.find_element_by_xpath(email_div_xpath + '/span[2]').text.strip()

            try:
                subject = driver.find_element_by_xpath(email_div_xpath + '/div[3]/h4/span[3]').text.strip()
            except NoSuchElementException:
                subject = driver.find_element_by_xpath(email_div_xpath + '/div[3]/h4/span[2]').text.strip()

            time = driver.find_element_by_xpath(email_div_xpath + '/time').text.strip()

            if 'read' not in email_div.get_attribute('class'):
                read = False
            else:
                read = True

            emails.append({
                'sender': sender,
                'subject': subject,
                'time': time,
                'read': read
            })

            row += 1
        except NoSuchElementException:
            break

    driver.close()

    return emails
