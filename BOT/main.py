try:
    # Import Selenium if installed
    from selenium import webdriver
except ModuleNotFoundError:
    # If not installed, install it via pip
    import pip
    pip.main(['install', '-U', 'selenium', '--user'])
    
    # Once installed, import it
    from selenium import webdriver

# Import another useful classes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the Chrome Driver
PATH_TO_CHROME_DRIVER = './chromedriver.exe'
# Path to the Edge Driver
PATH_TO_EDGE_DRIVER = './msedgedriver.exe'

# e-mail direction
EMAIL = '<email>'

# Prenot@Mi password
PASSWORD = '<pass>'

# Preont@Mi web page URL
PRENOTA_URL = 'https://prenotami.esteri.it/Language/ChangeLanguage?lang=2'


# Set a random user agent in order to avoid captcha
opt = webdriver.ChromeOptions()

# Set some options in order to avoid bot detection
opt.add_argument('start-maximized')
opt.add_argument('single-process')
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
opt.add_argument('--disable-infobars')
opt.add_argument('--allow-http-screen-capture')
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_experimental_option('useAutomationExtension', False)

# Create the instance of Chrome WebDriver
driver = webdriver.Chrome(executable_path = PATH_TO_CHROME_DRIVER, options = opt)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

# Get the URL
driver.get(url = PRENOTA_URL)

time.sleep(2)

# Search for the e-mail field of the main form
email = driver.find_element(by = By.ID, value = 'login-email')
# Complete the field with the user e-mail
email.send_keys(EMAIL)

time.sleep(2)

# Same thing with the password
password = driver.find_element(by = By.ID, value = 'login-password')
password.send_keys(PASSWORD)

time.sleep(2)

# Submit the form
password.submit()

#WebDriverWait(driver, 10).until(EC.url_contains(url = 'UserArea'))

time.sleep(5)