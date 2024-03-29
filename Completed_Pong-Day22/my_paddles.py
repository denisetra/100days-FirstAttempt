from turtle import Turtle

class Paddles(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setpos(position)
        self.shapesize(stretch_wid=5,stretch_len=1,outline=None)
        self.color("white")



    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
