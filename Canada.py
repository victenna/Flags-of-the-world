import turtle
t=turtle.Turtle()
wn=turtle.Screen()
s = turtle.Shape("compound")

t.hideturtle()
t.up()
t.color('red')
poly1=((0,0),(-25,-45),(-50,-38),(-40,-110),(-75,-80),(-85,-98),(-125,-90),\
       (-112,-135),(-130,-142),(-62,-185),(-68,-220),(0,-210),\
       (68,-220),(62,-185),(130,-142),(112,-135),(125,-90),(85,-98),(75,-80),\
       (40,-110),(50,-38),(25,-45))
s.addcomponent(poly1,'red')
wn.register_shape('flag',s)
 
can_flag=turtle.Turtle(shape='flag')
can_flag.tilt(90)

can_flag.shapesize(0.6)

t2=turtle.Turtle()
t2.up()
t2.color('red','red')
def rectangle(X,Y,width,length):
    t2.goto(X,Y)
    t2.begin_fill()
    t2.down()
    for i in range (2):
        t2.fd(length)
        t2.right(90)
        t2.fd(width)
        t2.right(90)
    t2.end_fill()

rectangle(-190,50,230,90)
t2.up()
rectangle(100,50,230,90)
t2.hideturtle()
t2.up()
rectangle(-5,-100,80,10)


       

       

       
