import smtplib, ssl,os
my_gmail = 'denise.coding@gmail.com'
my_yahoo = 'denise.coding@yahoo.com'
GMAIL_PWD = os.environ['GMAIL_PWD']
YAHOO_PWD = os.environ['YAHOO_PWD']

context = ssl.create_default_context()
def send_gmail(current_price,  ITEM_NAME):
    with smtplib.SMTP('smtp.gmail.com',port=587) as gmail:
        gmail.starttls(context=context)
        gmail.login(my_gmail, GMAIL_PWD)
        gmail.sendmail(
        my_gmail,
        my_yahoo,
        msg=f'Subject:Amazon Price ALERT! \n\n The price for {ITEM_NAME} has fallen below $20.75.  Current price is: ${round(current_price,2)}'
    )


