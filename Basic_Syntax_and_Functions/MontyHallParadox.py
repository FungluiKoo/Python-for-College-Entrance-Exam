# Monty Hall Paradox
import random
N=10000 # test case numbers
score1=0 # the questioner will not die
score2=0 # the questioner will die
d={"A":"Survive","B":"Survive","C":"Die"}
for i in range(N):
    selection=random.choice('ABC') # randomly one prisoner asks
    if selection=='A': # Prisoner A come to the warden
        score1+=1
    elif selection=='B': # Prisoner B come to the warden
        score1+=1
    else: # Prisoner C come to the warden
        score2+=1

print('P[Not die]=',score1,'P[Die]=',score2)
