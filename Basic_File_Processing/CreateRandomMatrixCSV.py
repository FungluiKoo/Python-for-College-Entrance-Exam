# a rows * b columns
try:
    a=int(input('How many rows do you want:'))
    b=int(input('How many columns do you want:'))
except:
    print('Something went wrong!')
    exit()

#Create a random matrix
import random
ls=[]
for row in range(a):
    ls.append([])
    for col in range(b):
        ls[row].append(str(round(random.random(),2)))

#Create a CSV
try:
    fileName=str(input('Please name the CSV file:'))
    f=open(fileName,'w')
except:
    print('Something went wrong!')
    exit()
for row in ls:
    f.write(','.join(row)+'\n')
f.close()

#Again read from the csv file
f=open(fileName,'r')
lt=f.readlines()
lsNew=[]
for row in lt:
    lsNew.append(row.strip('\n').split(','))
print(lsNew)
