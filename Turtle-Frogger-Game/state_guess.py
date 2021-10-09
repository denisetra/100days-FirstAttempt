import turtle as Turtle
import pandas as pd


state_data = pd.read_csv('50_states.csv')

class State(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('black')
        self.hideturtle()


    def user_answers(self):
        self.correct_answers = 999
        self.total_states = 50

        self.textinput(f"{self.correct_answers} / {self.total_states} States Correct ")


        self.state_info = (state_data[state_data.state == answer_state])



    def guess_state(num_correct):
        my_title = (f'{num_correct}/50 States correct')
        answer_state = (screen.textinput(title = my_title, prompt="What's another state's name?").title())
        print (answer_state)
        if answer_state not in state_data:
            pass
        state_info = (state_data[state_data.state == answer_state])
        state_x = int(state_info.x)
        state_y = int(state_info.y)
        statename.penup()
        statename.pencolor('black')
        statename.goto(state_x,state_y)
        statename.pendown()
        statename.write(answer_state, move=False, align='Center', font = ('Arial', 8, 'normal'))
        num_correct += 1

