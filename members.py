#comment section
#author: Korbelz , AGB Corp
#Feedback: Discord: Korbelz#3504
#current scope: Auto generates a org member list in .csv format


from bs4 import BeautifulSoup
import scroll
import csv

file_name = "org_list" 

with open(f'{file_name}.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Name ', 'Dossier Link '])

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

#testing differnt ways to pull page_source, uncomment 3rd line to restore standalone
r = scroll.scroll(org_site)
#print (r)
#r = pita

#r = requests.get(f'{org_site}')

#soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(r, "html.parser")

table = soup.find_all(class_="name-wrap")

all_names = []
for table in table: 
    name = table.text.strip()
    name_clean = name.split('\n')
    all_names.append(name_clean)

clean_names = list(filter(lambda x: len(x) > 1, all_names))
#print (clean_names) #DO NOT DELETE THIS 

for clean_names in clean_names:
    pname = (f'{clean_names[0]}')
    plink = (f'https://robertsspaceindustries.com/citizens/{clean_names[1]}')
    with open(f'{file_name}.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([f'{pname}  ', f'{plink} '])

print ('Jobs done!, a new file called org list is ready to import to a spreadsheet')
input('Press ENTER to exit')
