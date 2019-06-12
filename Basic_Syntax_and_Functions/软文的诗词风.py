inText=input('Please enter some texts:')
lineWidth=30 #Fixed width

def textSplit(txt):
    puncList=[',','.','?',':',';','!','，','。','？','：','；','！']
    for punc in puncList:
        txt=txt.replace(punc,'\n')
    return txt.split('\n')

outText=textSplit(inText)
try:
    for line in outText:
        #Cut the too-long lines
        while len(line)>lineWidth:
            print(line[0:lineWidth])
            line=line[lineWidth:]
        print(line.center(lineWidth,chr(12288))) #12288是中文空格。这里有一个问题，中英文混合后就不对齐了
except:
    print("Something went wrong.")
    exit()
