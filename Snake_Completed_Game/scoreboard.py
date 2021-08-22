from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:   {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=("courier", 40, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()









##keep track of score and display on board.
#dont forget to clear every time it changes.
#turtle.write & turtle.clear.
