#scroll to bottom of the page

from selenium import webdriver
import time

#Below are some example sites to test on.
#https://robertsspaceindustries.com/orgs/SECPRO/members
#https://robertsspaceindustries.com/orgs/AGBCORP/members

def scroll(target_url):
    driver = webdriver.Chrome()
    driver.get(f'{target_url}')
    driver.page_source

    SCROLL_PAUSE_TIME = 3
    time.sleep(SCROLL_PAUSE_TIME)

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        #pita = driver.page_source
        #return pita
        return driver.page_source

#pita = scroll('https://robertsspaceindustries.com/orgs/AGBCORP/members')
#print (pita)

        