d={}
for c in (65,97):
    for i in range(26):
        d[chr(i+c)]=chr((i+13)%26+c)
print(d)

e={}
for c in range(65,91): #Capital Letters
    e[chr(c)]=chr((c-52)%26+65)
for c in range(97,123): #Small Letters
    e[chr(c)]=chr((c-84)%26+97)
print(e)
