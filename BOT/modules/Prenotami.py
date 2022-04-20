class Prenotami:
    def __init__(self):
        self.services = ['direct_son', 'reconstruction', 'passport']
        return

    def service(self, name = ''):
        name = name.lower()
        if not isinstance(name, str) or name == '':
            return None
        else if name not in self.services:
            return None
        else:
            self.service_name = name
            if self.service_name == self.services[0]:
                self.xpath = '//*[@id="dataTableServices"]/tbody/tr[1]/td[4]/a/button'
            return
