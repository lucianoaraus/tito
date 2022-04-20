# Libraries for handling configuration, time and paths
import configparser
import time
import os

# Class to handle web scrapping
from modules import Browser

if __name__ == "__main__":
    
    # Read data from .ini file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'BOT', 'user_data.ini'))

    # Preont@Mi web page URL
    PRENOTA_URL = config['PRENOTAMI_DATA']['url']

    # Prenot@Mi e-mail
    EMAIL = config['PRENOTAMI_DATA']['email']

    # Prenot@Mi password
    PASSWORD = config['PRENOTAMI_DATA']['pass']

    # Path to the Chrome Driver
    PATH_TO_CHROME_DRIVER = os.path.join(os.getcwd(), 'BOT', 'chromedriver.exe')

    # Create the instance of the browser
    browser = Browser(PATH_TO_DRIVER = PATH_TO_CHROME_DRIVER)

    # Get the URL
    browser.get_url(url = PRENOTA_URL)

    # Search for the e-mail field of the main form and complete it
    browser.find_complete_submit(by = 'ID', value = 'login-email', keys = EMAIL)

    # Search for the pass field of the main form, complete it and submit it
    browser.find_complete_submit(by = 'ID', value = 'login-password', keys = [PASSWORD, 'RETURN'])

    # Once submitted, wait
    time.sleep(5)

    # Click on book tab
    browser.find_and_click(by = 'LINK_TEXT', value = 'Prenota', click = True)
    time.sleep(1)

    # Click on the service
    browser.find_and_click(by = 'XPATH', value = '//*[@id="dataTableServices"]/tbody/tr[4]/td[4]/a', click = True)
    time.sleep(1)