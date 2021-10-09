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


