try:
    # Import Selenium if installed
    import mechanize
except ModuleNotFoundError:
    # If not installed, install it via pip
    import pip
    pip.main(['install', 'mechanize'])
    
    # Once installed, import it
    import mechanize

import configparser
import time



""" /*** URL AND USER DATA DEFINITION ***/ """

# Read data from .ini file
config = configparser.ConfigParser()
config.read('user_data.ini')

# Preont@Mi web page URL
PRENOTA_URL = config['PRENOTAMI_DATA']['url']

# Prenot@Mi e-mail
EMAIL = config['PRENOTAMI_DATA']['email']

# Prenot@Mi password
PASSWORD = config['PRENOTAMI_DATA']['pass']



""" /*** PERFORM LOGIN ***/ """

# Instantiate a browser
br = mechanize.Browser()

# Open the Prenot@Mi web page
br.open(PRENOTA_URL)

# Select the main form
br.form = br.forms()[0]

# Input the email
br.set_value(name = 'Email', value = EMAIL)

# Input the password
br.set_value(name = 'Password', value = PASSWORD)

# Submit the form
br.submit()


""" /*** USER AREA ***/ """

# Go to services section
br.click_link(text = 'Prenota')

# Define the service link
service_link = mechanize.Link(
                                url      = '/Services/Booking/225',
                                base_url = 'https://prenotami.esteri.it',
                                text     = 'Prenota',
                                tag      = 'a',
                                attrs    = {'href' : '/Services/Booking/225'}
                            )

# Click in the link
br.follow_link(link = service_link)

# Select the main form
br.form = br.forms()[1]

#for i, v in enumerate(br.form.controls):
#    print('{} - {}'.format(i, v))

# Disable read only property
br.form.set_all_readonly(False)

br.form.controls[11].selected = True

# Set the AVO's name
#br.form.find_control(type = 'hidden', nr = 11).value = 'AVO NAME'

# Set the birth place
#br.form.find_control(type = 'hidden', nr = 15).value = 'PLACE OF BIRTH'

# Set the AVO's birth date
#br.form.find_control(type = 'hidden', nr = 19).value = '01/01/1950'

# Set the AVO's address
#br.form.find_control(type = 'hidden', nr = 23).value = 'AVO ADDRESS'

# Additional notes
#br.form.controls[26].value = 'NOTES'

# Checkbox
#br.form.controls[27].selected = True

#for i, v in enumerate(br.form.controls):
#    print('{} - {}'.format(i, v))

res = br.submit()

br.open(res.geturl())
print(br.title())

try:
    # Import Selenium if installed
    import lxml.html as lh
except ModuleNotFoundError:
    # If not installed, install it via pip
    import pip
    pip.main(['install', 'lxml'])
    
    # Once installed, import it
    import lxml.html as lh

with open('response.html', 'w+') as f:
    f.write(res.read().decode('utf-8'))