import csv 
import random
jobs=[]
chance=[]
firstline= False #rid of header text
percent=0;
total=99.8
d={} #dict

#reads file
f = open('occupations.csv', 'r')
reader = csv.reader(f)


#seperates into 2 lists
for row in reader:
    if firstline:
        jobs.append(row[0])
        chance.append(float(row[1]))
    else:
        firstline=True

f.close()

#rid of the total
jobs=jobs[:-1]
chance=chance[:-1]

#creates the dict by combining list
i=0
while i < len(jobs):
    d[jobs[i]]=chance[i]
    i+=1




percent = random.uniform(0, 99.8)

#Compare range of total and percent, if the key is larger than it's accepted
#Else, the total is subtract from the key
'''
percent = 100
red = 30
blue = 60
green = 10

percent: 20

total-random = 80
red < 80
total =  70

total-random=60
blue=60

blue

'''
for key in d:

    if (d[key] >= (total-percent)):
        print key
        break
    else:
        total-=d[key]