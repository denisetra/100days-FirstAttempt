import random
import pandas as pd
import datetime as dt
import smtplib, ssl
my_gmail = 'denise.coding@gmail.com'
my_pwd = 'fillmein'
print ('***\n***\nWhen running script, replace password in file\n***\n***')
context = ssl.create_default_context()

def send_gmail():
    with smtplib.SMTP('smtp.gmail.com',port=587) as gmail:
        gmail.starttls(context=context)
        gmail.login(my_gmail, my_pwd)
        gmail.sendmail(
        my_gmail,
        birth_email,
        msg=f'Subject:Happy Birthday! \n\n{final_letter}'
    )
my_email = 'denise.coding@yahoo.com'
yahoo_pwd = 'qjrmfjsxdaztszvv'
letters_location = 'D:\\100_Days_of_Code\\Day32-Email_SMTP\\birthday-wisher-extrahard-start\\letter_templates\\'
letter_list = ['letter_1.txt','letter_2.txt','letter_3.txt']
my_letter = random.choice(letter_list)
birthdays_df = pd.read_csv('D:\\100_Days_of_Code\\Day32-Email_SMTP\\birthday-wisher-extrahard-start\\birthdays.csv')
now = dt.datetime.now()
my_year = now.year
my_month = now.month
my_day = now.day

for index,row in birthdays_df.iterrows():
    if my_month == row['month'] and my_day == row['day']:
        birth_name = row['name']
        birth_email = row['email']

with open((letters_location+my_letter),'r') as readme:
    the_letter = readme.readlines()

new_letter = []
for entry in the_letter:
    if '[NAME]' in entry:
        new_header = entry.replace('[NAME]',birth_name)
        new_letter.append(new_header)
    else:
        new_letter.append(entry)
letter = f'{my_month}_{my_day}_{birth_name}_birthday-wishes.txt'
final_letter = ''.join(new_letter)

## not strictly needed for the assignment, but I like it.
with open(letter,'w') as writeme:
    for linz in new_letter:
        writeme.write(linz)

send_gmail()