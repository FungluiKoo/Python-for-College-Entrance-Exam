fi1=open('命运-网络版.txt','r',encoding='utf-8')
fi2=open('命运-网络版.txt','r',encoding='utf-8')
txt1=fi1.read()
txt2=fi2.read()
d1={}
for ch in txt1:
    d1[ch]=d1.get(ch,0)+1
d2={}
for ch in txt2:
    d2[ch]=d2.get(ch,0)+1
items1=sorted(list(d1.items()),lambda x:x[1],reverse=True)
items2=sorted(list(d2.items()),lambda x:x[1],reverse=True)

fo1=open('命运-字符统计.txt','w',encoding='utf-8')
fo2=open('寻梦-字符统计.txt','w',encoding='utf-8')
ls1=[]
ls2=[]
for item in items1[0:100]:
    ls1.append('{}:{}'.format(item[0],item[1]))
for item in items2[0:100]:
    ls2.append('{}:{}'.format(item[0],item[1]))
fo1.write(','.join(ls1))
fo2.write(','.join(ls2))
fo1.close()
fo2.close()
fo3=open('相同字符.txt','w',encoding='utf-8')
ls3=[]
for item1 in items1[0:100]:
    ch=item1[0]
    for item2 in items2[0:100]:
        if item2[0]!=ch:
            continue
        else:
            ls3.append(ch)
fo3.write(','.join(ls3))
