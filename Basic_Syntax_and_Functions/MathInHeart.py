print('欢迎来到口算天天练！每道题答案均为正整数。\n确认答案无误，请按回车键提交。请在10秒内给出作答，否则算做错。\n\
不作答或者输入任意其他类型数字、非数字字符可停止练习{}\nCopyright Tom © 2011-2019'.format(chr(9997)*2))
from random import *
import string
from time import *
print('\n第一部分：三位数以内加减法练习（共20题）')
score=0
for i in range(20):
    a=randint(1,999)
    b=randint(1,999)
    a,b=max(a,b),min(a,b)
    op=choice(['+','-'])
    startTime=perf_counter()
    ans=input('{}{}{}='.format(a,op,b))
    if ans.isnumeric():
        ans=int(ans)
        endTime=perf_counter()
        if (endTime-startTime<=10):
            if op=='+':
                score+=(ans==a+b)
            else:
                score+=(ans==a-b)
        else:
            print('可惜了，您已超时！您本题用时{}秒。'.format(round(endTime-startTime,2)))
    else:
        print('您做到第{}题，答对{}题，正确率{:.1%}。'.format(i+1,score,score/(i+1)))
        input('输入任意键退出程序')
        exit()
else:
    print('{}太棒啦，您已做完本部分全部题目！\n本部分您答对{}题，正确率{:.1%}。\n10秒钟后开始下一部分的练习！'.format(chr(9996),score,score/20))

sleep(10)
print('第二部分：简单的乘法练习（共20题）')
score=0
for i in range(20):
    a=randint(1,99)
    b=randint(1,11)
    startTime=perf_counter()
    ans=input('{}×{}='.format(a,b))
    if ans.isnumeric():
        ans=int(ans)
        endTime=perf_counter()
        if (endTime-startTime<=10):
            score+=(ans==a*b)
        else:
            print('可惜了，您已超时！您本题用时{}秒。'.format(round(endTime-startTime,2)))
    else:
        print('您做到第{}题，答对{}题，正确率{:.1%}。'.format(i+1,score,score/(i+1)))
        input('输入任意键退出程序')
        exit()
else:
    print('{}太棒啦，您已做完本部分全部题目！\n本部分您答对{}题，正确率{:.1%}。'.format(chr(9996),score,score/20))
