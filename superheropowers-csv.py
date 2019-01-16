
#Headers
# name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active
import csv
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
	print(member)



#create csv file
with open('members.csv','w') as f:
	writer = csv.writer(f)
	header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 
				'homeTown', 'formed', 'secretBase', 'active']
	writer.writerow(header)

	#loop through each member
	members = superheroes['members']
	for member in members:
		row = [
			member['name'], 
			member['age'], 
			member['secretIdentity'], 
			member['powers'], 
			superheroes['squadName'], 
			superheroes['homeTown'], 
			superheroes['formed'], 
			superheroes['secretBase'], 
			superheroes['active']
		]
		writer.writerow(row)

print(data)