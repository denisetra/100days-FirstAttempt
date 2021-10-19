from tkinter import *
import pandas as pd
import random
global my_title, my_word
#from time import time
BACKGROUND_COLOR = "#B1DDC6"
PAD = 50
RIGHT = 'right.png'
WRONG = 'wrong.png'
TIMER = 3000 #milliseconds

# ----------------------- Read in Dictionary ------------------------ #
try:
    word_file = pd.read_csv('words_to_learn.csv',encoding='utf-8')
except FileNotFoundError:
    word_file = pd.read_csv('french_words.csv')
word_df = pd.DataFrame(word_file)
to_learn = word_df.to_dict(orient='records')
print (f'Length of to_learn:{len(to_learn)}')

# ------------------------ Back of card ----------------------------- #
def card_back():
    print(english_word)
    canvas.itemconfig(canvas_image, image=canvas_back_image)
    canvas.itemconfig(card_title, text='English',fill='white')
    canvas.itemconfig(card_word, text=english_word,fill='white')

# ------------------------ UI SETUP ----------------------------------#
window = Tk()
window.title('Flashy')
window.config(padx=PAD,pady=PAD,bg=BACKGROUND_COLOR)

# ---------------------- Front of card ------------------------------- #
canvas = Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file='card_front.png')
canvas_back_image = PhotoImage(file='card_back.png')
canvas_image = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400,150,text='',font=('Ariel',40,'italic'))
canvas.grid(row=0,column=0,columnspan=2)
card_word = canvas.create_text(400,263,text='',font=('Ariel',60,'bold'))
flip_timer = window.after(3000,card_back)


# ------------------------ Generate Random word --------------------- #
def generate_word():
    global english_word, flip_timer,french_word,current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    english_word = current_card['English']
    canvas.itemconfig(card_title,text="French",fill='black')
    canvas.itemconfig(card_word,text=french_word,fill='black')
    flip_timer = window.after(3000, card_back)
# ----------------------- Remove from list & save new list ---------- #
def remove_list():
    to_learn.remove(current_card)
    print (f'Length of list still to learn: {len(to_learn)}')
    save_df = pd.DataFrame.from_dict(to_learn)
    save_df.to_csv('words_to_learn.csv',index=False)

    generate_word()
# ----------------------------- --------------------------------------- #

## Buttons
right_image = PhotoImage(file=RIGHT)
right_button = Button(image=right_image,highlightthickness=0,command=remove_list)
right_button.grid(row=1,column=1)

wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(image=wrong_image,highlightthickness=0,command=generate_word)
wrong_button.grid(row=1,column=0)

generate_word()







window.mainloop()