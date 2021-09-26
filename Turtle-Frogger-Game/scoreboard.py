from turtle import Turtle
from typing import Tuple

MY_FONT = ["Courier", 24, "normal"]

class Scoreboard:
    def __init__(self):
        self.score = Turtle()
        self.over = Turtle()
        self.score_level = 1
        self.score.color("white")
        self.game_level()

    def game_level(self):
        self.score.clear()
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(-270, 250 )

    def increase_score(self):
        self.score.clear()
        self.score_level += 1

    def display_score(self):
        my_score = (f"Level: {self.score_level}")
        self.score.write(my_score, False, align = "Left", font = MY_FONT )

    def game_over(self):
        self.over.penup()
        self.over.color("white")
        self.over.hideturtle()
        self.over.goto(0,0)
        new_font = ["Courier", 34, "bold"]
        self.over.write("GAME OVER ! ", False, align = "Center", font = new_font)

