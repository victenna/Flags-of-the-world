import turtle
import time
t=turtle.Turtle()

wn=turtle.Screen()
wn.setup(900,800)
t.speed(0)
t.hideturtle()
x=-200
y=200
t.up()
t.goto(x,y)

def red_line (Y):
    t.up()
    t.sety(Y)
    
    t.down()
    t.color('red')
    t.begin_fill()
    for i in range (2):
        
        t.fd(440)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()

Y=100
for i in range(7):
    red_line(Y)
    Y=Y-40

t.up()
t.goto(-200,120)
t.down()
def rectangle():
    t.color('blue','blue')
    t.begin_fill()
    for m in range (2):
        t.fd(200)
        t.right(90)
        t.fd(140)
        t.right(90)
    t.end_fill()
    
rectangle()   
    
def star(size,x,y):
    t.up()
    t.setx(x)
    t.sety(y)
    t.down()
    t.color('white','white')
    t.begin_fill()

    for i in range (5):
        t.fd(size)
        t.right(144)
    t.end_fill()


q1=0
m1=0

#------------------------
for m in range(31):
    star(8,-190+m1*35,110-30*q1)
    m1=m%6
    q1=int(m/6)
#-------------------------------------
q2=0
m2=0

for n in range(21):
    star(8,-170+m2*33,95-30*q2)
    m2=n%5
    q2=int(n/5)
    
  
