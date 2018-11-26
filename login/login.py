#!/usr/bin/env python3

from selenium import webdriver
import time

# Set Username and Password
username = 'example@gmail.com' # USER MUST REPLACE CREDENTIALS HERE
password = 'example1234' # USER MUST REPLACE CREDENTIALS HERE

# URL path
url = 'https://www.facebook.com/'

# Get rid of pop-up
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# Path to chromedriver exe file
### USER MUST REPLACE THIS PATH WITH THE PATH TO WHERE THEY HAVE THE CHROMEDRIVER FILE LOCATED ###
driver = webdriver.Chrome('/Users/benhutton/Desktop/facebook/chromedriver', chrome_options=chrome_options)

def login():
    ''' Login into Facebook '''

    # Open Chrome
    driver.get(url)
   
    # Find id for email and send it the username (inspect in email box on Chrome)
    driver.find_element_by_id('email').send_keys(username)
    # Find id for password and send it the password (inspect in password box on Chrome) --may have to inspect twice 
    driver.find_element_by_id('pass').send_keys(password)
    # Find id for login and click it (inspect the button)
    driver.find_element_by_id('loginbutton').click()

if __name__=='__main__':
    login()
