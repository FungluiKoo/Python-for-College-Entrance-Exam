from turtle import *
import time
setup(1024,576)
screensize(1024,576)

def drawLeft():
    penup()
    hideturtle()
    goto(-500,0)
    pensize(10)
    color(1,0,1) #等价于'magenta'
    pendown()
    speed(2)
    fd(480)
    right(90)
    circle(20)

def drawStopBoard(StaNameCN,StaNameEN):
    penup()
    hideturtle()
    xCN=-40*len(StaNameCN)
    xEN=-13*len(StaNameEN)
    goto(xCN,80)
    color('black')
    pendown()
    write(StaNameCN,font=('Microsoft Yahei',60))
    penup()
    goto(xEN,30)
    pendown()
    write(StaNameEN,font=('Consolas',36))

def drawTransfer(TransCN,TransEN,TransColor):
    #drawTriangle
    penup()
    hideturtle()
    speed(6)
    goto(0,-120)
    setheading(0)
    color(TransColor)
    begin_fill()
    circle(60,steps=3)
    end_fill()
    penup()
    #drawLineName
    xCN=-13*len(TransCN)-72
    xEN=-6.5*len(TransEN)-75
    speed(1)
    goto(xCN,-180)
    color('black')
    pendown()
    write('换乘'+TransCN,font=('Microsoft Yahei',36))
    penup()
    goto(xEN,-210)
    pendown()
    write('Transfer to '+TransEN,font=('Consolas',18))

def drawRight():
    penup()
    hideturtle()
    goto(20,0)
    pensize(10)
    color('magenta')
    pendown()
    speed(2)
    fd(480)

def drawSta(StaNameCN,StaNameEN,TransCN,TransEN,TransColor):
    drawLeft()
    drawStopBoard(StaNameCN,StaNameEN)
    drawTransfer(TransCN,TransEN,TransColor)
    drawRight()
    time.sleep(3)
    reset()
def drawWelcome(welcomeCN,welcomeEN):
    penup()
    hideturtle()
    xCN=-40*len(welcomeCN)
    xEN=-13*len(welcomeEN)
    goto(xCN,20)
    color('black')
    pendown()
    write(welcomeCN,font=('Microsoft Yahei',60))
    penup()
    goto(xEN,-30)
    pendown()
    write(welcomeEN,font=('Consolas',36))
    time.sleep(3)
    reset()

#主函数
def main():
    time.sleep(5)
    drawWelcome('杭州欢迎您','Welcome to Hangzhou')
    drawWelcome('欢迎乘坐机场快线','Welcome abroad Airport Express')
    drawSta('萧山机场','Xiaoshan Airport','1、7号线','Lines 1/7','magenta')
    drawSta('御道','Yudao','9号线','Line 9','brown')
    drawSta('火车东站','East Railway Sta','1、4、6号线','Lines 1/4/6','magenta')
    drawSta('池塘庙','Chitangmiao','南北线','Longitude Line','turquoise')
    drawSta('西湖文化广场','Westlake Cultural Square','1、3号线','Lines 1/3','magenta')
    drawSta('沈塘桥','Shentangqiao','2号线','Line 2','orange')
    drawSta('文三路','Wensan Rd','10号线','Line 10','#808000')
    drawSta('西溪湿地','Xixi Wetland Park','14号线','Line 14','purple')
    drawSta('阿里巴巴','Alibaba','南环线','Southloop Express','wheat')
    done()

main()
