try:
    # Import Selenium if installed
    import mechanize
except ModuleNotFoundError:
    # If not installed, install it via pip
    import pip
    pip.main(['install', 'mechanize'])
    
    # Once installed, import it
    import mechanize

import time


""" /*** URL AND USER DATA DEFINITION ***/ """

# Preont@Mi web page URL
PRENOTA_URL = 'https://prenotami.esteri.it/Language/ChangeLanguage?lang=2'

# Prenot@Mi e-mail
EMAIL = '<email>'

# Prenot@Mi password
PASSWORD = '<password>'


""" /*** LOGIN ***/ """

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

#print(br.submit().geturl())

# Submit the form
br.submit()


""" /*** USER AREA ***/ """

# Go to services section
br.click_link(text = 'Prenota')

# Define the service link
service_link = mechanize.Link(
                                url      = '/Services/Booking/222',
                                base_url = 'https://prenotami.esteri.it',
                                text     = 'Prenota',
                                tag      = 'a',
                                attrs    = {'href' : '/Services/Booking/222'}
                            )

# Click in the link
br.follow_link(link = service_link)

# Select the main form
br.form = br.forms()[1]

# Disable read only property
br.form.set_all_readonly(False)

# Set the AVO's name
br.form.find_control(type = 'hidden', nr = 11).value = 'AVO NAME'

# Set the birth place
br.form.find_control(type = 'hidden', nr = 15).value = 'PLACE OF BIRTH'

# Set the AVO's birth date
br.form.find_control(type = 'hidden', nr = 19).value = '01/01/1950'

# Set the AVO's address
br.form.find_control(type = 'hidden', nr = 23).value = 'AVO ADDRESS'

# Additional notes
br.form.controls[26].value = 'NOTES'

# Checkbox
br.form.controls[27].selected = True

for i, v in enumerate(br.form.controls):
    print('{} - {}'.format(i, v))

res = br.submit()
print(res.getcode())