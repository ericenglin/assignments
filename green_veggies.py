import csv

#open veggies.csv
with open('veggies.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

green_veggies=[]
for row in rows:
 	if row['color']=='green':
 		print(row['name'])
 		green_veggies.append(row)


print(green_veggies)

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

