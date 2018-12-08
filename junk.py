#table = soup.find_all(class_="trans-03s frontinfo")
#table = soup.find_all(class_="rank")
#table = soup.find_all(class_="name-wrap")
# and list need to add these two together somehow
#table = soup.find_all(class_=["name-wrap", "rank"])
#table = soup.find_all(class_=["trans-03s name", "rank"])
table = soup.select("span.name")
table_nick = soup.select("span.nick")
table_rank = soup.select("span.rank")
print (table + table_nick + table_rank)

'''
somethings=[]
class something():
    def __init__(self,table):
        self.name=table.select_one("span.name")
        self.nick=table.select_one("span.nick")
        self.rank=table.select_one("span.rank")
        somethings.append(self)
    def __repr__(self):
        return '<%s name=%s, nick=%s, rank=%s>'%(self.__class__.__name__,self.name,self.nick,self.rank)
    __str__=__repr__

table = soup.find_all(class_="trans-03s frontinfo")
for table in table:
    something(table)

print(somethings)
'''
#name = []
#nick = []
#rank = []

#print (table)
#name = soup.find_all(table).text
#print (name)

'''
table_name = soup.select("span.name")
table_nick = soup.select("span.nick")
table_rank = soup.select("span.rank")
table = (name + nick + rank)
print (table)
'''
'''
all_names = []
for table in table: 
    name = table.text.strip()
    #name_strip = name.strip('\n')
    name_clean = name.split('\n')
    all_names.append(name_clean)
'''