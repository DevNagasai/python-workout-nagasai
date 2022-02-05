import csv

with open('stuff.csv' , 'w') as f:
    o = csv.writer(f)
    o.writerow(range(5))
    o.writerow(['a','b','c','d','e'])