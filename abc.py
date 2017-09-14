import csv 
import sys
jobs=[]
chance=[]
d={}

f = open('occupations.csv', 'r')
reader = csv.reader(f)

for row in reader:
    jobs.append(row[0])
    chance.append(row[1])
f.close()
jobs=jobs[1:-1]
chance=chance[1:-1]

for x in range (len(chance)):
    
d = dict(zip(jobs, chance))
print d
