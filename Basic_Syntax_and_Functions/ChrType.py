print(type(chr(0x7777)))

txt='全国计算机等级考试二级Python语言程序设计'
d ={}
c = 0x4e00
for i in range(20902):
    d[chr(i+c)] = chr((i+10451) % 20902 + c)
ls=[]
for ch in txt:
    ls.append(d.get(ch,ch))
print("".join(ls))

s=''
for ch in txt:
    if 0x4e00<=ord(ch)<=0x9fa5:
        s+=chr(0x4e00+(ord(ch)-0x4e00+10451)%20902)
    else:
        s+=ch
print(s)
