import string

def getCharlist(fileName):
    txt=open(fileName,"r").read()
    txt=txt.upper()
    return list(txt)

file=str(input("欢迎来到中英字符字频统计小程序。请输入一个文本的文件名:"))
try:
    charlist=getCharlist(file)
except:
    print("哎呀出错了！")
    exit()

dic={}
for char in charlist:
    if char.isalpha():
        dic[char]=dic.get(char,0)+1
    else:
        pass

item=sorted(list(dic.items()), key=lambda x:x[-1], reverse=True)

N=eval(input("你想要字频最高的前几名:"))
N=min(N,len(item))
print("前 {} 名的字符是:\n{:<4}{:<4}{:^6}".format(N,"名次","字","频数"))
rank={}
for i in range(N):
    word, count=item[i]
    if i>0 and count==item[i-1][-1]:
        rank[i]=rank[i-1]
    else:
        rank[i]=i+1
    print("{:<6}{:<5}{:>6}".format(rank[i],word,count))
