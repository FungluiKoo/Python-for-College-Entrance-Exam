#Survey on Python Academy New-comers

#位置参数也称基本参数,positional para
def defaultPara(name,age=12,city='NYC'):
    print('位置参数：',name,'默认参数：',age,city)
    #默认参数必须是int,float,str,tuple等不变对象！
    #否则下次调用的时候会把前面的记住,造成bug
defaultPara('Amy',13)
defaultPara('Bob',city='Boston')

def defaultzero(ls = []):  #我们的本意是提供的list参数为0时 返回只有一个0的list
    ls.append(0)
    print(ls)
defaultzero()
defaultzero()
print('这显然不是我们想要的！\n')
#解决方案：使用None
def defaultzeroNew(lsn = None):  
    if lsn == None:
        lsn = []
    lsn.append(0)
    print(lsn)
defaultzeroNew()
defaultzeroNew()
print('舒服了。这说明list是一个对  象\n')

def devarPara(name,age=12,city='NYC',*hobby): 
    print('位置参数：',name,'默认参数：',age,city,'可变参数：',hobby)
devarPara('Bob',city='Boston') #可变参数可以不填
#devarPara('Bob',city='Boston',hobby='tennis')填不来hobby了
devarPara('Cindy','violin','baseball') #会覆盖到默认参数的位置上
devarPara('Cindy',*['violin','baseball']) #还是会覆盖
devarPara('Cindy',12,'NYC','violin','baseball') #这样实际上默认参数没有了效果，跟位置参数一样了

def varPara(name,*hobby): #可变参数返回tuple
    print('位置参数：',name,'可变参数：',hobby)
varPara('Cindy','violin','baseball')
varPara('David',('Piano','basketball'))
varPara('Eva',['dance','swim'])

def listSum(*num): #列表求和
    s=0
    for n in num:
        s+=n
    return s
lt=[1,2,3,4]
print('The sum of the list:',sum(lt),'=',listSum(*lt)) #注意这个*不能省略！

def kwPara(name,**note): #关键字参数返回dictionary
    print('位置参数：',name,"关键字参数：",note)
kwPara('Frank',status='Single') #叫不叫note都无所谓
kwPara('Gina',note='Married',tuition='Unpaid') #甚至可以混用

def nkwPara(name,*,status,tuition): #命名关键字，不是返回dict了
    print('位置参数：',name,"命名关键字参数：",status,tuition)
nkwPara('Gina',status='Married',tuition='Unpaid')
#此时就只能用星号后面有的status，并且命名关键字也不能搞重复
#nkwPara('Gina',note='Married')就会出错了

def varkwPara(name,*hobby,**note): #来看如何混合
    print('位置参数：',name,'可变参数：',hobby,'\n\t关键字参数：',note)

varkwPara('Henry',*['badminton','hiking','Go'],\
          **{'status':'single','tuition':'paid'})
