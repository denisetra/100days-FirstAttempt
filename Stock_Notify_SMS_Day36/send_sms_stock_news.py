up_ticker = '🔺'
down_ticker = '🔻'
import stock_program_auth_keys
from twilio.rest import Client
TWILIO_ACCOUNT_SID = stock_program_auth_keys.TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = stock_program_auth_keys.TWILIO_AUTH_TOKEN

# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (CMCSA)?.

def send_sms(article_list,alert_text,percent_changed):
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    if percent_changed > 0:
        my_icon = up_ticker
    elif percent_changed < 0:
        my_icon = down_ticker
    message = client.messages \
        .create(
        body=(f'{alert_text}\n{my_icon} {percent_changed} %\n {article_list}'),
        from_='+17207039492',
        to= '13033785941'
    )

    print(message.status)


