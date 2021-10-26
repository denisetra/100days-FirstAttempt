from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
score = 0
check_mark = 'D:\\100_Days_of_Code\\Day-34_Trivia-Game\\quizzler-app-start\\images\\true.png'
x_mark ='D:\\100_Days_of_Code\\Day-34_Trivia-Game\\quizzler-app-start\\images\\false.png'

class Quiz_Interface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('                              Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(height=250,width=300,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50,padx=50)

        self.canvas_question = self.canvas.create_text(150,125,text='question_here',font=('Arial',20,'italic'),width=280)

        self.score_label = Label(text=(f'       Score: {score} '))
        self.score_label.grid(row=0,column=1)
        self.score_label.config(pady=20, padx=10,bg=THEME_COLOR,font=('Arial',18,'bold'),fg='white')

        self.check_image = PhotoImage(file=check_mark)
        self.true_button = Button(image=self.check_image,command=self.click_true, width=110,bg=THEME_COLOR,highlightthickness=0)
        self.true_button.grid(row=2,column=0,pady=10,padx=10)

        self.x_image = PhotoImage(file=x_mark)
        self.false_button = Button(image=self.x_image,command=self.click_false, width=110,bg=THEME_COLOR,highlightthickness=0)
        self.false_button.grid(row=2,column=1,pady=10,padx=10)

        self.get_next_question()

        self.window.mainloop()

    def click_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def click_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'          Score:  {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text = question_text)
        else:
            self.canvas.itemconfig(self.canvas_question,text='You have reached the end of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            print ('Game Over')
        self.canvas.config(bg='white')
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.configure(bg='green')

        else:
            self.canvas.configure(bg='red')

        self.window.after(1000,self.get_next_question)




