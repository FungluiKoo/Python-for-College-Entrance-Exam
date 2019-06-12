fi=open('天龙八部-网络版.txt','r',encoding='utf-8')
txt=fi.read()
d={}
import string
for ch in txt:
    if ch.isalpha()==True:
        d[ch]=d.get(ch,0)+1
    else:
        continue
fo1=open('天龙八部-汉字统计.txt','w',encoding='utf-8')
ls=[]
for key in d:
    ls.append('{}:{}'.format(key,d[key]))
fo1.write(','.join(ls))
fo1.close()

fo2=open('天龙八部-词语统计.csv','w',encoding='utf-8')
import jieba
wordList=jieba.lcut(txt)
d.clear()
for word in wordList:
    d[word]=d.get(word,0)+1
lt=sorted(list(d.items()),key=lambda x:x[1],reverse=True)
for row in lt:
    fo2.write(','.join(row)+'\n')
fo2.close()
fi.close()
