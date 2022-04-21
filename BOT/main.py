# Libraries for handling configuration, time and paths
import configparser
import time
import os

# Class to handle web scrapping
from modules import *

if __name__ == "__main__":
    
    """/*** USER DATA FROM INI FILE ***/"""
    # Read data from .ini file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'user_data.ini'))
    
    # Preont@Mi web page URL
    PRENOTA_URL = config['PRENOTAMI_DATA']['url']

    # Prenot@Mi e-mail
    EMAIL = config['PRENOTAMI_DATA']['email']

    # Prenot@Mi password
    PASSWORD = config['PRENOTAMI_DATA']['pass']

    # Path to the Chrome Driver
    PATH_TO_CHROME_DRIVER = os.path.join(os.getcwd(), 'chromedriver.exe')


    
    """/*** GET INTO PRENOTAMI WEBPAGE AND LOGIN ***/"""
    # Create the instance of the browser
    browser = Browser(PATH_TO_DRIVER = PATH_TO_CHROME_DRIVER)

    # Get the URL
    browser.get_url(url = PRENOTA_URL)
    
    # Search for the e-mail field of the main form and complete it
    browser.find_fill_submit(by = 'ID', value = 'login-email', keys = EMAIL)

    # Search for the pass field of the main form, complete it and submit it
    browser.find_fill_submit(by = 'ID', value = 'login-password', keys = [PASSWORD, 'RETURN'])



    """/*** GO TO BOOK SECTION AND CLICK ON THE SERVICE ***/"""
    # Click on book tab
    browser.find_and_click(by = 'LINK_TEXT', value = 'Prenota')

    # Click on the service
    browser.find_and_click(by = 'XPATH', value = '//*[@id="dataTableServices"]/tbody/tr[4]/td[4]/a/button')
    time.sleep(5)