f=open('琵琶行.txt','rt', encoding='utf-8')
print(f)
print(type(f))
txt=f.read()
print(txt)
f.seek(0)
lines=f.readlines(3)
print(lines)
line=f.readline()
print(line)
line2=f.readline()
print(line2)
f.close()
