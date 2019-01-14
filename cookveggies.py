#read veggies.csv
import csv
with open('veggies.csv','r') as f:
	reader = csv.DictReader(f)
	vegetables=list(reader)


#print variable vegetables
print(vegetables)

#output to json

import json
with open('cookedveggies.json', 'w') as f:
    json.dump(vegetables, f, indent=2)
