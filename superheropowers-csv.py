
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

all_powers=[]

for member in members:
	powers=member['powers']
	for power in powers:
		all_powers.append(power)

#set makes list unique
#set only works for lists
#want to make into a list at the end
print(list(set(all_powers)))



#create csv file
# 'w' means writer
with open('members.csv','w') as f:
	writer = csv.writer(f)
	header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 
				'homeTown', 'formed', 'secretBase', 'active','first power']
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
			superheroes['active'],
			member['powers'][0]
		]
		writer.writerow(row)

