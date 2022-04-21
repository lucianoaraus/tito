import sys

class PrenotamiWebPage:
    def __init__(self, service = ''):

        self.__check_args(service, str)
        self._url = 'https://prenotami.esteri.it/Language/ChangeLanguage?lang=2'
        self._services = ['direct_son', 'reconstruction', 'passport']

        if service not in self._services:
            print('Please, enter a valid service name')
            sys.exit()

        self._locators = {
                            'login' : {
                                        'BY' : 'ID', # How to locate the elements
                                        'LOGIN_EMAIL' : "login-email", # By.ID
                                        'LOGIN_PASSWORD' : "login-password" # By.ID
                                    },

                            'user_area' : {
                                            'BY' : 'LINK_TEXT', # How to locate the elements
                                            'USERAREA_PRENOTA' : 'Prenota' # By.LINK_TEXT
                                        },

                            'direct_son' : {
                                            'BY' : 'XPATH', # How to locate the elements
                                            'SERVICE_BUTTON' : '//*[@id="dataTableServices"]/tbody/tr[1]/td[4]/a/button' # By.XPATH
                                            },

                            'reconstruction' : {},

                            'passport' : {},
                        }
        return

    def get_locator(self, name = ''):
        self.__check_args(name, str)
        self._service_name = name.lower()

        if name not in self._locators.keys():
            print('Name is wrong')
            sys.exit()

        return self._locators[name]

    def get_url(self):
        return self._url

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