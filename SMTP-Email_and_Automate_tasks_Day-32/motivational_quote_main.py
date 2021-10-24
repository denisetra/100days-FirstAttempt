import datetime as dt
import random
import smtplib, ssl

my_gmail = 'denise.coding@gmail.com'
my_yahoo = 'denise.coding@yahoo.com'
my_pwd = 'fillmein'
yahoo_pwd = 'fillmein'
my_title = "Today's Quote of the Day"
print ('When running the code, add the correct password')

context = ssl.create_default_context()

def send_gmail():
    with smtplib.SMTP('smtp.gmail.com', port=587) as gmail:
        gmail.starttls(context=context)
        gmail.login(my_gmail, my_pwd)
        gmail.sendmail(
            my_gmail,
            my_yahoo,
            msg=f'Subject:{my_title} \n\n{my_quote}'

        )

days_of_week = {'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
now = dt.datetime.now()
today_date = now.day
today_wkday = now.isoweekday()
with open ('D:\\100_Days_of_Code\\Day32-Email_SMTP\\Birthday Wisher (Day 32) start\\quotes.txt','r') as readme:
    quotes = readme.readlines()

my_quote = random.choice(quotes)

if today_wkday == 6:
    send_gmail()
    print ('Email sent, program complete.')
else:
    print ('No mail sent today')


