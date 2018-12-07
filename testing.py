#comment section
#author: Korbelz , AGB Corp
#Feedback: Discord: Korbelz#3504
#current scope: Auto generates a org member list in .csv format

import requests
from bs4 import BeautifulSoup
import scroll
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

print ('*** This app auto generates a org member list then prints it to a file ***')
print ('*** Written by Korbelz, AGB Corp ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
print ('***')
print ("Org member URL example: https://robertsspaceindustries.com/orgs/AGBCORP/members")
print ('***')
input('Press ENTER to continue')

#Below are some example sites to test on.
#https://robertsspaceindustries.com/orgs/SECPRO/members
#https://robertsspaceindustries.com/orgs/AGBCORP/members
org_site = input('Paste org member list page from RSI site: ')

options = webdriver.ChromeOptions()

options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)
driver.get(f"{org_site}")
#This code will scroll down to the end
while True:
    try:
        # Action scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        break
    except: 
        pass

#comment out these two lines, uncomment 3rd line to restore orginal
#pita = scroll.scroll(org_site)

#r = requests.get(pita)

r = requests.get(f'{org_site}')

soup = BeautifulSoup(r.content, "html.parser")

table = soup.find_all(class_="name-wrap")

all_names = []
for table in table: 
    name = table.text.strip()
    name_clean = name.split('\n')
    all_names.append(name_clean)

clean_names = list(filter(lambda x: len(x) > 1, all_names))
#print (clean_names) #DO NOT DELETE THIS 

for clean_names in clean_names:
    print (f'Player name is: {clean_names[0]}')
    print (f'https://robertsspaceindustries.com/citizens/{clean_names[1]}')


