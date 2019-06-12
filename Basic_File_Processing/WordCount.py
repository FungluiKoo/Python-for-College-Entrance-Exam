'''
ls=[1,2,3,4,5]
print(type(ls))
s=str(ls)
print(s)
print(type(s))
lt=[1,2,3,3,3,3,3,4,5]
print(lt.count(3))
'''

def getWordlist(fileName):
    txt=open(fileName,"r").read()
    txt=txt.lower()
    punc="`-=[]\;',./~!@#$%^&*()_+{{}}|:\"<>?"
    for char in punc:
        txt=txt.replace(char,' ')
    return txt.split()

file=str(input("Input the file name:"))
try:
    wordlist=getWordlist(file)
except:
    print("Something went wrong!")
    exit()

dic={}
for word in wordlist:
    dic[word]=dic.get(word,0)+1

item=sorted(list(dic.items()), key=lambda x:x[-1], reverse=True)

N=eval(input("How many of the toppest words do you want:"))
N=min(N,len(item)-1) #避免用户输入比所有的词的总数还多
print("Top {} words are:\n{:^20}{:6}".format(N,"Words","Counts"))
for i in range(N):
    word, count=item[i+1] #由于某种原因，第一名总是空格，我不知道该怎么办
    print("{:<20}{:>6}".format(word,count))
