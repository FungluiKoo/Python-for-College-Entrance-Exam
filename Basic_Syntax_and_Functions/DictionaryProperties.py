d={}
print(type(d))

m={"201801":"Bob",201802:"Cindy",201803:"David",201800:"Amy"}
d.update(m)
print(d)
del m[201800]

print(m.keys())
print(list(m.keys()))

print(m[201802])
print(m.get(201804,"Not exist!"))
print(m.get(201805))
print(m.pop(201803))

print(m.popitem())
print(m)
m[201804]="Eve"
print(m)
