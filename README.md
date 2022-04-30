# bot-tito
tito is a bot used to book a day to request italian citizenship (by any method) or passport at Prenot@Mi website.

It's coded in Python, with the Selenium package for web scraping.

### Usage:

1. Clone this repository in your computer. For this, open a CLI and copy&paste the following command:
```
gh repo clone hvignolo87/tito
```
2. Create a file inside the **BOT** folder, named *user_data.ini*, with the following structure:
```
[PRENOTAMI_DATA]
# The Prenot@mi email
email = <your email here>

# The Prenot@mi password
pass = <you password here>

# The required service. Chose one of this options: reconstruction, direct_son, passport, notarial.
service = notarial


# Form data
[RECONSTRUCTION]
# Insert notes for the embassy, if needed
NOTES = <notes here>

# Form data
[DIRECT_SON]
PARENT_NAME = <AVO's name>
BIRTH_PLACE = <AVO's birth place>
BIRTH_DATE = <AVO's birth date [DD/MM/YYYY]>
ADDRESS = <AVO's address>

# Insert notes for the embassy, if needed
NOTES = <notes here>

# Form data
[PASSPORT]
# Insert notes for the embassy, if needed
NOTES = <notes here>

# Form data
[NOTARIAL]
# Insert notes for the embassy, if needed
NOTES = <notes here>
```

3. Fill the **email**, **pass** and **service** fields with your data, then go to the selected service section and fill the form data. For example:
```
[PRENOTAMI_DATA]
email = johndoe@gmail.com
pass = JohnDoe
service = notarial

[NOTARIAL]
NOTES = This is a note for the embassy.
```

4. Open a CLI and navigate to the **BOT** folder with the *cd* command. Once there, copy&paste the following command:
```
python main.py
```

5. Depending on the selected service, the script runs until the OTP code is required (this depends on the location of the selected embassy). Once the popup window shows, you need to enter it manually and click **OK**.

6. Enjoy.

## Future improvings
- [x] Develop a user-friendly web interface with Flask.
- [ ] Automate the OTP code insertion.
- [ ] Evaluate real time response, with high traffic in the website, in order to improve performance.
