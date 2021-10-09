from turtle import Turtle

frame = Turtle()

def outside_frame():
    frame.penup()
    frame.hideturtle()
    frame.speed("fastest")
    frame.color("yellow")
    frame.goto(-295,290)
    frame.pendown()
    frame.setheading(0)
    frame.forward(580)
    frame.right(90)
    frame.forward(580)
    frame.right(90)
    frame.forward(580)
    frame.right(90)
    frame.forward(580)

    # middle line
    #frame.penup()
    #frame.goto(0,290)
    #frame.pendown()
    #frame.right(180)
    #frame.forward(580)

    # frame.penup()
    # frame.color("cyan")
    # frame.goto(290,250)
    # frame.shape("circle")
    # frame.shapesize(.5,.5,1)
    #
    # frame.stamp()
    # frame.goto(240,200)
    # frame.write("(x=290,y=250)",move=False,align="left",font=("Arial",12,"normal"))
    # frame.goto(-350,250)
    # frame.stamp()
    # frame.goto(-370,200)
    # frame.write("(x-350,y=250)",move=False,align="Left",font=("Arial",12,"normal"))

    # frame.goto(-350,-250)
    # frame.stamp()
    # frame.goto(-370,-220)
    # frame.write("(x-350,y=-250)",move=False,align="Left",font=("Arial",12,"normal"))
    #
    # frame.goto(290,-250)
    # frame.stamp()
    # frame.goto(240,-220)
    # frame.write("(x350,y=-250)",move=False,align="Left",font=("Arial",12,"normal"))


