from .Browser import Browser
from .Installer import Installer

import configparser
import os
import time

class OTP():
    def __init__(self, user:str = '', password:str = ''):
        self.user = user
        self.password = password
        self.otp = None
        self.__login_email()
        return

    def __login_email(self):
        DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver.exe')
        self.browser = Browser(PATH_TO_DRIVER = DRIVER_PATH)
        self.browser.get_url(url = 'https://accounts.google.com/ServiceLogin')
        time.sleep(5)
        self.browser.find_fill_submit(by = 'ID', value = 'identifierId', keys = [self.user, 'return'])
        time.sleep(5)
        return

#otp = OTP(user = 'vignolo.hernan@gmail.com', password = 'Hernan6938')