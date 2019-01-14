import csv

# Write a CSV file
# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])

# # Read from a csv

# with open('testwrite.csv','r') as f:
# 	reader=csv.DictReader(f)
# 	rows = list(reader)

# for row in rows:
#     print(row)

#can also use pretty print (pprint)

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('veggies.csv', 'w') as f:
	#loop through veggies
	writer = csv.writer(f)
	writer.writerow(['name','length','color'])
	for vegetable in vegetables:
		print(vegetable['name'])
		name = vegetable['name']
		color = vegetable['color']
		length = len(vegetable['name'])
		row=[name,length, color]
		writer.writerow(row)