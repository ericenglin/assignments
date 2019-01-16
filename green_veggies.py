import csv
#open veggies.csv
with open('veggies.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

#put all the green veggies into an empty dataframe
green_veggies=[]
for row in rows:
 	if row['color']=='green':
 		print(row['name'])
 		green_veggies.append(row)


#put into a green veggies specific csv file
with open('green_veggies.csv','w') as f:
	writer = csv.writer(f)
	header = ['name', 'length', 'color']
	writer.writerow(header)

	#loop through each member
	for veggie in green_veggies:
		row = [
			veggie['name'], 
			veggie['length'], 
			veggie['color']
		]
		writer.writerow(row)


#also make a json file
import json
print(json.dumps(green_veggies,indent=2))