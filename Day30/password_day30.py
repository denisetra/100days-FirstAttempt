from tkinter import *
from datetime import date
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json, pandas


today = date.today()
print (today)
WIDTH = 200
HEIGHT = 200
PADDING = 50
SM_PAD = 5
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)  ## for some reasons, it is cutting off some of the characters
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pwd():

    site = website_entry.get()
    name = email_entry.get()
    password = password_entry.get()
    my_data = (f'{site},{name},{password},{today}\n')
    new_data = {
        site: {
            'email':name,
            'password':password
        }
    }
    if len(site) < 1 or len(name) < 1 or len(password) <1:
        messagebox.showerror('There are empty fields!\n Please fill all fields.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file) #<--reading old data
                data.update(new_data) #<--Updating data with new data
        except FileNotFoundError:
            data = new_data
            pass
        finally:
            with open('data.json','w') as data_file:
                json.dump(data, data_file, indent=4)  # <--Saving all data

                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
# --------------------------Search for Password ------------------------------------#
def find_password():
    try:
        with open('data.json', 'r') as data_file:
            my_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Checked for website',message="No Data File Found")

    else:
        my_website = website_entry.get()
        try:
            return_pwd = (my_data[my_website]['password'])
            messagebox.showinfo(title=my_website,message=(f'Email: {(my_data[my_website]["email"])}\nPassword: {return_pwd}'))
            pyperclip.copy(return_pwd)
        except KeyError:
            messagebox.showinfo(title="Checked file for website",message='No details for the website exist')




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('                           Password Manager')
window.config(padx=PADDING,pady=PADDING,bg='white')
window.minsize(width=440,height=440)

canvas = Canvas(width=200,height=200,highlightthickness=4,highlightbackground='white',bg='white')

logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_image)
canvas.grid(row=0,column=1)

##Website
web_label = Label(text='             Website: ')
web_label.grid(row=1,column=0,rowspan=2)
web_label.config(pady=SM_PAD)
##Website text entry box
website_entry = Entry(width=38)
website_entry.grid(row=1,column=1)
website_entry.focus()
## Search box
search_button = Button(text='Search',command=find_password,width=15)
search_button.grid(row=1,column=2)

##Email/UserName:
email_label = Label(text='Email/UserName: ')
email_label.grid(row=3,column=0)
email_label.config(pady=SM_PAD)
## Email text entry box
email_entry = Entry(width=56)
email_entry.grid(row=3,column=1,columnspan=2)
email_entry.insert(0,'denisetra@comcast.net')
## Password
password_label = Label(text='           Password:  ')
password_label.grid(row=4, column=0)
password_label.config(pady=SM_PAD)
## Password Text Entry box
password_entry = Entry(width=38)
password_entry.grid(row=4,column=1)
## Generate Password Button
generate_button = Button(text='Generate new pwd',command=generate)
generate_button.grid(row=4,column=2)
## Add space between Password and Add
blank_label= Label(width=1,text='',bg='white')
blank_label.grid(row=5,column=1,columnspan=2)
## Add button
add_pwd_button = Button(text='Store Password Information ',command=add_pwd,width=36)
add_pwd_button.grid(row=6,column=1,columnspan=2)





window.mainloop()
