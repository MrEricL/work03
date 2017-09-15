import csv 
import sys
import random
jobs=[]
chance=[]
firstline= False
percent=0;
val=0 #to make the precent


f = open('occupations.csv', 'r')
reader = csv.reader(f)

for row in reader:
    if firstline:
        jobs.append(row[0])
        val+=float(row[1])
        chance.append(val)
    else:
        firstline=True



f.close()
jobs=jobs[:-1]
chance=chance[:-1]

d= dict(zip(jobs, chance))
#print d

percent = random.uniform(0, 99.8)
print percent
for key in d:
    if (d[key] >= percent):
        print key
        break
        
    else:
        print key + " failed"
        print 
    

