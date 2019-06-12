from random import *

for i in range(20):
    print(randrange(0,100,3),end=',')

print('')
for i in range(10):
    print(randint(0,1),end=',')

print('')
print(sample([1,2,3,4,5,6,7],3))
