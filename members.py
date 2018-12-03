#comment section
#author: Korbelz , AGB Corp
#Feedback: Discord: Korbelz#3504
#current scope: Auto generates a org member list in .csv format

import requests
from bs4 import BeautifulSoup

print ('*** This app auto generates a org member list then prints it to a file ***')
print ('*** Written by Korbelz, AGB Corp ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
print ('***')
print ("Org member URL example: https://robertsspaceindustries.com/orgs/AGBCORP/members")
print ('***')
input('Press ENTER to continue')

#http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html
#https://robertsspaceindustries.com/orgs/SECPRO/members
#https://robertsspaceindustries.com/orgs/AGBCORP/members
org_site = input('Paste org member list page from RSI site: ')

r = requests.get(f'{org_site}')
print(r.url)

soup = BeautifulSoup(r.content, "html.parser")

#<span class="name-wrap">
#soup.find_all(class_="name-wrap")


table = soup.find_all(class_="name-wrap")
print (table[2])  

all_names = []
for table in table: 
    name = table.text
    all_names.append(name)
print (all_names)



