a,b=1,2
ls=[1,2]
while True:
    c=a**2+b**2
    if c<=1000000:
        ls.append(c)
        a,b=b,c
    else:
        break
print(','.join(ls))
