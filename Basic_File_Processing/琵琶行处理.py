fi=open('琵琶行.txt','r',encoding='utf-8')
#第一题，统计正文字数（不含标点），以及每个字出现的次数，并排序
txtls=fi.readlines()
n=0
d={}
import string
for i in range(1,len(txtls)):
    for ch in txtls[i]:
        if ch.isalpha()==True:
            n+=1
            d[ch]=d.get(ch,0)+1
            continue
        else:
            pass
else:
    print('正文总字数：',n)
    fo1=open('琵琶行字符统计.csv','w',encoding='utf-8')
    chls=sorted(list(d.items()),key=lambda x:x[1],reverse=True)
    for item in chls:
        ch,cnt=item
        fo1.write('{},{}\n'.format(ch,cnt))
    fo1.close()
#第二题，统计正文词语及其出现次数，并排序
txt=''.join(txtls[1:])
import jieba
wds=jieba.lcut(txt)
d.clear()
for wd in wds:
    if len(wd)>1:
        d[wd]=d.get(wd,0)+1
    else:
        pass
wdls=sorted(list(d.items()),key=lambda x:x[1],reverse=True)
fo2=open('琵琶行词语统计.csv','w',encoding='utf-8')
for item in wdls:
    wd,cnt=item
    fo2.write('{},{}\n'.format(wd,cnt))
fo2.close()
#第三题，生成默写题
import random
for i in range(len(txtls)):
    try:
        txtls.remove('')
    except:
        break
print('开始默写！输入Q退出')
while True:
    juzi=random.choice(txtls[1:])
    juzils=juzi.split('，')
    r=random.randint(0,1)
    if r==0:
        print('?, ',juzils[1].strip('\n'),end='')
    else:
        print(juzils[0],', ?',end='')
    ans=input()
    if ans=='Q':
        break
    elif ans==juzils[r][0:7]:
        print('答对了')
        continue
    else:
        print('正确答案:',juzils[r][0:7])
fi.close()
