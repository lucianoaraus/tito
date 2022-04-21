# Libraries for handling configuration, time and paths
import configparser
import time
import os

# Import all modules
from modules import *

if __name__ == "__main__":
    
    """/*** USER DATA FROM INI FILE ***/"""
    # Read data from .ini file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'user_data.ini'))
    
    # Prenot@Mi e-mail
    EMAIL = config['PRENOTAMI_DATA']['email']

    # Prenot@Mi password
    PASSWORD = config['PRENOTAMI_DATA']['pass']

    # Path to the Chrome Driver
    PATH_TO_CHROME_DRIVER = os.path.join(os.getcwd(), 'chromedriver.exe')


    
    """/*** GET INTO PRENOTAMI WEBPAGE AND LOGIN ***/"""
    # Create the instance of the browser
    browser = Browser(PATH_TO_DRIVER = PATH_TO_CHROME_DRIVER)

    # Create the Web Page object to retrieve locators
    web_page = PrenotamiWebPage(service = 'reconstruction')

    # Get the URL
    browser.go_to(url = web_page.get_url())
    
    # Locate login form
    loc = web_page.get_locator('login')
    
    # Search for the e-mail field and fill it
    browser.find_fill_submit(by = loc['BY'], value = loc['LOGIN_EMAIL'], keys = EMAIL)

    # Search for the pass field, fill it and submit the form
    browser.find_fill_submit(by = loc['BY'], value = loc['LOGIN_PASSWORD'], keys = [PASSWORD, 'RETURN'])

    # Delete the variable
    del(loc)


    """/*** GO TO BOOK SECTION AND CLICK ON THE SERVICE ***/"""
    # Locate book link
    loc = web_page.get_locator('user_area')

    # Click on book tab
    browser.find_and_click(by = loc['BY'], value = loc['USERAREA_PRENOTA'])

    del(loc)

    # Locate 
    loc = web_page.get_locator('direct_son')

    # Click on the service
    browser.find_and_click(by = loc['BY'], value = loc['SERVICE_BUTTON'])
    


    """/*** FILL THE FORM AND SUBMIT ***/"""
    time.sleep(5)