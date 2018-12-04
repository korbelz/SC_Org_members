all_names = [['Carl Ramsey', 'Carl_Ramsey'], [''], ['Zaphod Hawke', 'Zaphod_Hawke'], ['KaynBot', 'KaynBot5297']]
#print (all_names)
clean_names = list(filter(lambda x: len(x) > 1, all_names))

print (clean_names)

for clean_names in clean_names:
    #i = 0
    print (f'Player name is: {clean_names[0]}')
    print (f'https://robertsspaceindustries.com/citizens/{clean_names[1]}')
    #i += 1

