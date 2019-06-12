from random import *
seed(0x1010)
ls='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&'
shouzimu=[]
n=0
while n<10:
    kwd=''.join(sample(ls,10))
    if n>=1 and (kwd[0] in shouzimu):
        continue
    else:
        shouzimu.append(kwd[0])
        print(kwd)
        n+=1
