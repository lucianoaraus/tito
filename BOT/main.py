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
from datetime import datetime

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

    # OTP code insertion delay
    OTP_DELAY_TIME = int(config['PRENOTAMI_DATA']['otp_delay'])

    # The form data
    FORM_DATA = config[SERVICE.upper()]




    """/*** GET INTO PRENOTAMI WEBPAGE AND LOGIN ***/"""
    # Create the instance of the browser
    browser = Browser()

    # Create the Web Page object to retrieve locators
    web_page = PrenotamiWebPage(service=SERVICE)

    # Get the URL
    browser.go_to(url=web_page.get_url())
    
    # Locate login form
    loc = web_page.get_locator('login')
    
    # Search for the e-mail field and fill it
    browser.find_fill_submit(by=loc['BY'], value=loc['LOGIN_EMAIL'], keys=EMAIL)

    # Search for the pass field, fill it and submit the form
    browser.find_fill_submit(by=loc['BY'], value=loc['LOGIN_PASSWORD'], keys=[PASSWORD, 'RETURN'])

    # Delete the variable
    del(loc)



    """/*** GO TO BOOK SECTION AND CLICK ON THE SERVICE ***/"""
    # Locate book link
    loc = web_page.get_locator('user_area')

    # Check if it's time to start
    now = datetime.now()
    init_hour = datetime.now().replace(hour=19, minute=00, 
                                       second=0, microsecond=0)
    diff = init_hour - now
    diff = diff.total_seconds()

    if diff >= 0:
        print(f'Waiting until {init_hour}...')
        print(f'Time left: {diff} seconds.')
        time.sleep(diff)
    else:
        print('Too late. Try again tomorrow.')
        sys.exit()

    # Click on book tab
    browser.find_and_click(by=loc['BY'], value=loc['USERAREA_PRENOTA'])

    # Delete the variable
    del(loc)

    # Locate the required service button
    loc = web_page.get_locator(SERVICE)

    # Click on the service
    browser.find_and_click(by=loc['BY'], value=loc['SERVICE_BUTTON'])
    


    """/*** FILL THE FORM AND SUBMIT ***/"""
    
    # Fill the form with the specified data
    for field in FORM_DATA:
        try:
            browser.find_fill_submit(by=loc['BY'], value=loc[field.upper()], keys=FORM_DATA[field])
        except:
            continue

    # Check the terms and conditions
    browser.find_and_click(by=loc['BY'], value=loc['CHECKBOX'])
    
    # Submit the form
    browser.find_and_click(by=loc['BY'], value=loc['SUBMIT'])
    
    # Press OK in the popup window
    browser.handle_popup(action='accept')

    # Delete the variable
    del(loc)



    """/*** CALENDAR SECTION: FIND AN AVAILABLE DAY AND BOOK ***/"""

    # Locate the calendar buttons: backwards, month and forward
    loc = web_page.get_locator('calendar')

    # Flag to indicate whether is any day available in the month or no
    no_available_days = True

    # Initialize assuming no green days available
    green_days = []

    # Try for max 18 months
    max_tries = 18

    # Count each iteration
    iter_count = 0

    # Iterate the calendar until find and available day
    while no_available_days:
        try:
            # Find all the available days in a month
            green_days = browser.find_elements(by='class_name', value=loc['GREEN_DAYS'])
            if green_days == None:
                green_days = []
        except:
            pass
        
        # Logic to walk around the months
        if len(green_days) == 0:
            # Compare iteration number with stop limit
            if iter_count > max_tries:
                # No available days within 18 months
                no_available_days = False
            else:
                # Continue searching for available days in next month
                browser.find_and_click(by=loc['BY'], value=loc['FORWARD'])
                # Sum one iteration
                iter_month += 1
                # Wait until everything is loaded
                time.sleep(2)
                #Continue the loop
                continue
        else:
            # Change the flag
            no_available_days = False

            # Click on the first available day
            green_days[0].click()

            # Find the first available hour
            hours = browser.find_elements(by='class_name', value=loc['HOURS'])

            # Click on the first available hour
            hours[0].click()

            # Submit the form
            browser.find_and_click(by=loc['BY'], value=loc['SUBMIT'])

            # If there is an OTP code to insert, wait until the user writes it
            try:
                otp = browser.find_elements(by=loc['BY'], value=loc['OTP'])
            except:
                pass
            else:
                # Click on the input of the OTP window
                otp[0].click()
                
                # Get the OTP ok button
                otp_ok = browser.find_elements(by=loc['BY'], value=loc['OTP_OK'])
                
                # Wait until the user inserts the OTP code
                time.sleep(OTP_DELAY_TIME)
                
                # Submit the OTP form
                otp_ok[0].click()
    
    # Wait a long time to ensure the procces is ended
    time.sleep(10)

    # Then, end the script
    sys.exit()