import turtle
import random
from math import*
from tkinter.simpledialog import*
##2019038059 윤태경##
instr=''
swidth,sheight=500,500
tx,ty=[0]*2
txsize=20
d=200
turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(swidth,sheight)
turtle.penup()
instr=askstring('문자열 입력','거북이 쓸 문자열을 입력')
angle=720/len(instr)
for ch in instr:
    
    radian=3.14*angle/180
    tx=d*cos(radian)
    ty=d*sin(radian)
    r=random.random();g=random.random();b=random.random()
    turtle.goto(tx,ty)
    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은고딕',txsize,'bold'))
    d-=200/len(instr)
    angle+=720/len(instr)
    
turtle.done()


    

