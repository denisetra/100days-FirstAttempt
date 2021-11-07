STOCK = "CMCSA"
COMPANY_NAME = "Comcast Corporation"
company_short = "Comcast"
from stock_queries import stock_data
from get_stock_news import get_news
import send_sms_stock_news

def main():
    stock_info = stock_data()
    my_news = get_news(STOCK,company_short)
    percent_changed = stock_info[0]
    start_day = stock_info[1]
    end_day = stock_info[2]
    if percent_changed > 0.99:
        alert_text = 'The stock did great today!'
        my_sms = send_sms_stock_news.send_sms(my_news,alert_text,percent_changed)
    if percent_changed < -0.99:
        alert_text = 'The stock did poorly today!'
        my_sms = send_sms_stock_news.send_sms(my_news,alert_text,percent_changed)



    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    #Optional: Format the SMS message like this:
    # """
    # Comcast: 🔺2%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (CMCSA)?.
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    # or
    # "TSLA: 🔻5%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (CMCSA)?.
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    # """
    #

main()