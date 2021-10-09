from turtle import Turtle

## This is the turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.shapesize(1,1,1)
        self.setheading(90)
        self.penup()
        self.go_to_start()


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False






    def up(self):
        self.forward(MOVE_DISTANCE)

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x,self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x,self.ycor())
