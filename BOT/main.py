# Libraries for handling configuration, time and paths
import configparser
import time
import os
import sys

# Set the correct current working directory
if not os.getcwd()[-3:].lower() == 'bot':
    os.chdir(os.path.join(os.getcwd(), 'BOT'))

# Import all modules
from modules import *

# Start the script
if __name__ == "__main__":
    
    """/*** LOAD DATA FROM INI FILE ***/"""
    # Read data from .ini file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'user_data.ini'))
    
    # Prenot@Mi e-mail
    EMAIL = config['PRENOTAMI_DATA']['email']

    # Prenot@Mi password
    PASSWORD = config['PRENOTAMI_DATA']['pass']

    # Service required
    SERVICE = config['PRENOTAMI_DATA']['service']

    # The form data
    FORM_DATA = config[SERVICE.upper()]

    # Path to the Chrome Driver
    PATH_TO_CHROME_DRIVER = os.path.join(os.getcwd(), 'chromedriver.exe')



    """/*** GET INTO PRENOTAMI WEBPAGE AND LOGIN ***/"""
    # Create the instance of the browser
    browser = Browser(PATH_TO_DRIVER = PATH_TO_CHROME_DRIVER)

    # Create the Web Page object to retrieve locators
    web_page = PrenotamiWebPage(service = SERVICE)

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

    # Delete the variable
    del(loc)

    # Locate the required service button
    loc = web_page.get_locator(SERVICE)

    # Click on the service
    browser.find_and_click(by = loc['BY'], value = loc['SERVICE_BUTTON'])
    


    """/*** FILL THE FORM AND SUBMIT ***/"""

    # Fill the form with the specified data
    for field in FORM_DATA:
        browser.find_fill_submit(by = loc['BY'], value = loc[field.upper()], keys = FORM_DATA[field])

    # Check the terms and conditions
    browser.find_and_click(by = loc['BY'], value = loc['CHECKBOX'])

    # Submit the form
    browser.find_and_click(by = loc['BY'], value = loc['SUBMIT'])

    # Press OK in the popup window
    browser.handle_popup(action = 'accept')

    # Delete the variable
    del(loc)

    time.sleep(5)