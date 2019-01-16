
#Headers
# name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active
# 'r' means reader
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
# 'w' means writer
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
			#below data is at the superhero level, not within each member
			superheroes['squadName'], 
			superheroes['homeTown'], 
			superheroes['formed'], 
			superheroes['secretBase'], 
			superheroes['active']
		]
		writer.writerow(row)

print(data)