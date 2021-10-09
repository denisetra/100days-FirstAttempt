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
        self.high_score = self.retrieve_high_score()
        self.update_scoreboard()



    def retrieve_high_score(self):
        with open ('highscore.txt', 'r') as file:
            data = file.read()
            data = int(data)
            return data
        file.close()

    def update_high_score(self):
        with open('highscore.txt','w') as writeme:
            w_score = str(self.high_score)
            writeme.write(w_score)
        writeme.close()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:   {self.score}    High-Score: {self.high_score}", align = ALIGNMENT, font = FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()









##keep track of score and display on board.
#dont forget to clear every time it changes.
#turtle.write & turtle.clear.
