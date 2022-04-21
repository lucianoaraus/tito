# Load installer class
from .Installer import Installer
import sys

try:
    # Import Selenium if installed
    from selenium import webdriver
except ModuleNotFoundError:
    # If not installed, install it
    Installer('selenium', True).install()

try:
    from fake_useragent import UserAgent
except ModuleNotFoundError:
    # If not installed, install it
    Installer('fake_useragent').install()

try:
    import undetected_chromedriver as uc
except ModuleNotFoundError:
    # If not installed, install it
    Installer('undetected-chromedriver').install()

# Selenium useful modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Undetectable Chrome
import undetected_chromedriver as uc

# Fake the User Agent
from fake_useragent import UserAgent

# Simplified class to perform scrapping
class Browser:

    # Constructor of the browser handler
    def __init__(self, PATH_TO_DRIVER = '', undetectable = False):
        self.__check_args(PATH_TO_DRIVER, str)
        self.__check_args(undetectable, bool)

        # Path to the Chrome driver
        self._PATH_TO_DRIVER = PATH_TO_DRIVER

        # Undetectable flag
        self._undetectable = undetectable

        # Set the options to avoid detection
        self._options = self.__set_options()

        # Create the driver instance
        if undetectable == False:
            # Set the driver
            self._driver = webdriver.Chrome(executable_path = self._PATH_TO_DRIVER, options = self._options)
        else:
            # Set the driver
            self._driver = uc.Chrome(options = self._options)

        # Avoid detection
        self._driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self._driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                                                                                "source":
                                                                                "const newProto = navigator.__proto__;"
                                                                                "delete newProto.webdriver;"
                                                                                "navigator.__proto__ = newProto;"
                                                                            }
                                    )

        self._driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent" : self._user_agent})
        return

    # Define options of the browser in order to avoid detection
    def __set_options(self):
        # Set a random user agent in order to avoid captcha
        self._user_agent = UserAgent().random

        if self._undetectable == True:
            return uc.ChromeOptions()
        else:
            # Instantiate a options object of Chrome
            opt = webdriver.ChromeOptions()
            
            # Set some options
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
            opt.add_argument('--user-agent={}'.format(self._user_agent))
            return opt

    # Find and HTML element
    def __find_element(self, by = '', value = ''):
        self.__wait_element_load(by = by, value = value)
        if by.lower() == 'id':
            return self._driver.find_element(by = By.ID, value = value)
        elif by.lower() == 'link_text':
            return self._driver.find_element(by = By.LINK_TEXT, value = value)
        elif by.lower() == 'xpath':
            return self._driver.find_element(by = By.XPATH, value = value)
        return
    
    # Validate arguments
    def __check_args(self, args = '', instance = ''):
        if isinstance(instance, list):
            for i in instance:
                if not isinstance(args, i) or args == '':
                    print("Argument is empty or wrong. Shutting down.")
                    sys.exit()
                else:
                    continue
        else:
            if not isinstance(args, instance) or args == '':
                print("Argument is empty or wrong. Shutting down.")
                sys.exit()
        return

    # Go to specific URL
    def go_to(self, url = ''):
        self.__check_args(url, str)
        self._url = url
        self._driver.get(url = self._url)
        return

    # Find and click a HTML element
    def find_and_click(self, by = '', value = ''):
        self.__check_args(by, str)
        self.__check_args(value, str)
        self.__find_element(by = by, value = value).click()
        return

    # Find a HTML element, fill it with text, then submit
    def find_fill_submit(self, by = '', value = '', keys = '', submit = False):
        self.__check_args(by, str)
        self.__check_args(value, str)
        self.__check_args(keys, (str, list))
        
        element = self.__find_element(by = by, value = value)

        if  isinstance(keys, str):
            element.send_keys(keys)
        elif isinstance(keys, list):
            element.send_keys(keys[0])
            if keys[1].lower() == 'return':
                element.send_keys(Keys.RETURN)

        if submit == True:
            element.submit()
            return

        return

    def __wait_element_load(self, by = '', value = ''):
        self.__check_args(by, str)
        self.__check_args(value, str)

        if by.lower() == 'id':
            locator = (By.ID, value)
        elif by.lower() == 'link_text':
            locator = (By.LINK_TEXT, value)
        elif by.lower() == 'xpath':
            locator = (By.XPATH, value)
        else:
            return
        
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator))
        return