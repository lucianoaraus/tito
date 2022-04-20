# Libraries for handling configuration, time and paths
import configparser
import time
import os

# Libraries to execute command-line processes
import subprocess
import sys

# This function installs a package
def install(package, root = False):
    if root == True:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, '--user'])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    return

try:
    # Import Selenium if installed
    from selenium import webdriver
except ModuleNotFoundError:
    # If not installed, install it via pip
    install('selenium', True)
    
    # Once installed, import it
    from selenium import webdriver

try:
    from fp.fp import FreeProxy
except ModuleNotFoundError:
    # If not installed, install it via pip
    install('free-proxy')
    
    # Once installed, import it
    from fp.fp import FreeProxy

try:
    from fake_useragent import UserAgent
except ModuleNotFoundError:
    # If not installed, install it via pip
    install('fake_useragent')
    
    # Once installed, import it
    from fake_useragent import UserAgent

try:
    import undetected_chromedriver as uc
except ModuleNotFoundError:
    # If not installed, install it via pip
    install('undetected-chromedriver')
    
    # Once installed, import it
    import undetected_chromedriver as uc

# Selenium useful modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

# Function used to retrieve a random proxy IP address
def get_random_proxy():
    # Random countries list
    countries = ['US', 'AR', 'UZ', 'SG', 'FR', 'HK', 'ZA', 'RU', 'ID', 'TH', 'ZA', 'MX', 'DO', 'KR', 'HU']
    country = countries[np.random.randint(low = 0, high = len(countries))]
    # Get a working proxy IP
    try: 
        proxy = FreeProxy(country_id = country, rand = True, anonym = True).get()
    except:
        print('No working proxy now! Try again in a few seconds.')
        sys.exit()
    return proxy.split("://")[1]

if __name__ == "__main__":
    # Path to the Chrome Driver
    PATH_TO_CHROME_DRIVER = os.path.join(os.getcwd(), 'BOT', 'chromedriver.exe')

    # Read data from .ini file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'BOT', 'user_data.ini'))

    # Preont@Mi web page URL
    PRENOTA_URL = config['PRENOTAMI_DATA']['url']

    # Prenot@Mi e-mail
    EMAIL = config['PRENOTAMI_DATA']['email']

    # Prenot@Mi password
    PASSWORD = config['PRENOTAMI_DATA']['pass']

    # Set a random user agent in order to avoid captcha
    user_agent = UserAgent().random

    #ip = get_random_proxy()
    #print('IP: ' + ip + '\n')

    # Instantiate a options object of Chrome
    opt = webdriver.ChromeOptions()
    
    # Set some options in order to avoid bot detection
    opt.add_argument('--start-maximized')
    #opt.add_argument('--single-process')
    opt.add_argument('--incognito')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-blink-features')
    opt.add_argument('--disable-blink-features=AutomationControlled') 
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--disable-impl-side-painting')
    opt.add_argument('--disable-setuid-sandbox')
    opt.add_argument('--disable-seccomp-filter-sandbox')
    opt.add_argument('--disable-breakpad')
    opt.add_argument('--disable-client-side-phishing-detection')
    opt.add_argument('--disable-cast')
    opt.add_argument('--disable-cast-streaming-hw-encoding')
    opt.add_argument('--disable-cloud-import')
    opt.add_argument('--disable-popup-blocking')
    opt.add_argument('--ignore-certificate-errors')
    opt.add_argument('--disable-session-crashed-bubble')
    opt.add_argument('--disable-ipv6')
    opt.add_argument('--allow-http-screen-capture')
    opt.add_experimental_option('useAutomationExtension', False)
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    opt.add_argument('--disable-infobars')
    opt.add_argument('--user-agent={}'.format(user_agent))
    #opt.add_argument('--proxy-server={}'.format(ip))
    
    """
    # Set the proxy in Chrome
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
                                                        'httpProxy'  : ip,
                                                        'ftpProxy'   : ip,
                                                        'sslProxy'   : ip,
                                                        'noProxy'    : None,
                                                        'proxyType'  : 'MANUAL',
                                                        'autodetect' : False
                                                    }
    """
    
    # Accept SSL
    webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
    
    # Create the instance of Chrome WebDriver
    driver = webdriver.Chrome(executable_path = PATH_TO_CHROME_DRIVER, options = opt)
    
    # Execute some scripts to avoid detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                                                                        "source":
                                                                                    "const newProto = navigator.__proto__;"
                                                                                    "delete newProto.webdriver;"
                                                                                    "navigator.__proto__ = newProto;"
                                                                    }
                        )

    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent" : user_agent})

    # Get the URL
    driver.get(url = PRENOTA_URL)

    # Search for the e-mail field of the main form
    email = driver.find_element(by = By.ID, value = 'login-email')

    # Complete the field with the user e-mail
    email.send_keys(EMAIL)

    # Same thing with the password
    password = driver.find_element(by = By.ID, value = 'login-password')
    password.send_keys(PASSWORD)
    
    # Submit the form
    password.send_keys(Keys.RETURN)

    # Once submitted, wait
    time.sleep(5)

    # Click on book
    driver.find_element(by = By.LINK_TEXT, value = 'Prenota').click()
    time.sleep(5)

    # Click on the service
    driver.find_element(by = By.XPATH , value = '//*[@id="dataTableServices"]/tbody/tr[4]/td[4]/a').click()
    time.sleep(5)