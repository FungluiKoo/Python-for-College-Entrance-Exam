fi=open('SunSign.csv','r',encoding='utf-8')
sunls=fi.readlines()
while True:
    sun=input('请输入星座名称：')
    if sun=='exit':
        break
    elif len(sun)<2:
        print('输入星座名称有误！')
    else:
        for item in sunls:
            if sun in item:
                itemls=item.split(',')
                print('{}的生日是{}至{}，符号是{}。'.format(itemls[0],itemls[1],itemls[2],chr(eval(itemls[3]))))
                break
            else:
                pass
        else:
            print('输入星座名称有误！')
