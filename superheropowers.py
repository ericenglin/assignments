#read the json file
import json
with open('superheroes.json','r') as f:
	superheroes = json.load(f)

#get the members
members = superheroes['members']
#print(members)

#loop through each member 
#for each member, get a list of the powers

data=[]

for member in members:
	powers = member['powers']
	for power in powers:
		data.append(power)

print(data)

# filter for only unique values
unique_powers = set(data)


