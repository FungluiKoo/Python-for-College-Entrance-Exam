fi=open('论语-网络版.txt','rt',encoding='utf-8')
txtls=fi.readlines()

lt1=[]
for i in range(len(txtls)):
    if '【原文】' in txtls[i]:
        line=txtls[i+2]
        while line[0] in ' .·1234567890':
            line=line[1:-1]
        while line[-1] in ' \n':
            line=line[0:-2]
        lt1.append(line)
    else:
        pass
fo1=open('论语-提取版.txt','w',encoding='utf-8')
fo1.write('\n'.join(lt1))
fo1.close()

lt2=[]
for line in lt1:
    for p in '()0123456789':
        line.replace(p,'')
    else:
        lt2.append(line)
fo2=open('论语-原文.txt','w',encoding='utf-8')
fo2.write('\n'.join(lt2))
fo2.close()

fi.close()
