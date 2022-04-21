class PrenotamiWebPage:
    def __init__(self):
        self.services = ['direct_son', 'reconstruction', 'passport']
        return

    def book_service(self, name = ''):
        name = name.lower()
        if not isinstance(name, str) or name == '':
            return None
        elif name not in self.services:
            return None
        else:
            self.service_name = name
            if self.service_name == self.services[0]:
                # Direct son book button
                self.xpath = '//*[@id="dataTableServices"]/tbody/tr[1]/td[4]/a/button'
            elif self.service_name == self.services[1]:
                # Reconstruction book button
                self.xpath = '' # Averiguar
            elif self.service_name == self.services[2]:
                # Passport book button
                self.xpath = '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button'
        
        return self.xpath