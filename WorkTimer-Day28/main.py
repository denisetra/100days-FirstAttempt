from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#00e600"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .2
SHORT_BREAK_MIN = .2
LONG_BREAK_MIN = .3
reps = 0
checkmark = '🗹'
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_countdown():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text=' WORK_TIMER  ')
    global my_checks
    check_label.config(text='')



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,my_reps
    reps += 1
    my_reps = reps
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text=' WORK_TIMER  ',fg=GREEN)
    elif reps < 7 and reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text=' SHORT_BREAK ',fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text=' LONG_BREAK ',fg=RED)
        my_reps = 8
        reps = 0

    print (f'Reps: {reps}')
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = round(math.floor(count/60),2)
    count_sec = math.floor(count % 60)
    print (count_sec)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(100,count_down,count - 1)
    else:
        start_timer()
        num_checks = my_reps / 2
        my_checks = ''
        for num in range(math.floor(num_checks)):
            my_checks += checkmark
            check_label.config(text=my_checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('                                            My Tomato Timer')
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) #<-hlthick is to get rid of whate border

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(114,130, text= '00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

timer_label = Label(text=' WORK_TIMER  ', font=(FONT_NAME,40,'bold'))
timer_label.grid(column=1,row=0)
timer_label.config(padx=5,pady=20,fg=GREEN,bg=YELLOW,highlightthickness=0)

start_button = Button(text='Start',command=start_timer)
start_button.grid(column=0,row=2)
start_button.config(padx=10,pady=0)

reset_button = Button(text='Reset',command=reset_countdown)
reset_button.grid(column=2,row=2)
reset_button.config(padx=1,pady=0)

check_label = Label(font=(FONT_NAME,20))
check_label.config(padx=0,pady=20,fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)


boxmark = '#U25A1.gif'


window.mainloop()
