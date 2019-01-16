#Read vegetables.csv
import csv
with open('veggies.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

#Group by color
veggies_by_color={}
for row in rows:
 	color = row['color']
 	if color in veggies_by_color:
 		veggies_by_color[color].append(row)
 	else:
 		veggies_by_color[color]=[row]




#print to terminal	\
from pprint import pprint
pprint(veggies_by_color)

#output to json
import json
with open('veggies_by_color.json','w') as f:
	json.dump(veggies_by_color,f,indent=2)