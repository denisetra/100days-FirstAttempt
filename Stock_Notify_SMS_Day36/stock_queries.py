import requests
import datetime as dt
from datetime import date
import stock_program_auth_keys
day_of_week = dt.datetime.today().weekday()
my_today = date.today()
def stock_data():

    if day_of_week == 6:
        start_day = my_today - (dt.timedelta(3))
        end_day = my_today - (dt.timedelta(2))
    elif day_of_week == 5:
        start_day = my_today - (dt.timedelta(2))
        end_day = my_today - (dt.timedelta(1))
    elif day_of_week == 0:
        start_day = my_today - (dt.timedelta(3))
        end_day = my_today
    else:
        start_day = my_today - (dt.timedelta(1))
        end_day = my_today
    start_day = str(start_day)
    end_day = str(end_day)
    apikey = stock_program_auth_keys.stock_apikey
    function = 'TIME_SERIES_DAILY'
    symbol = 'CMCSA'
    interval = '60min'
    my_url = 'https://www.alphavantage.co/'
    full_url = f'{my_url}query?function={function}&symbol={symbol}&interval={interval}&apikey={apikey}'

    r = requests.get(full_url)
    stock_data = r.json()
    stock_symbol = stock_data['Meta Data']['2. Symbol']
    daily_records = stock_data['Time Series (Daily)']
    print (stock_symbol,'\n',)
    start_records = daily_records[start_day]
    end_records = daily_records[end_day]
    start_open = float(start_records['1. open'])
    end_open = float(end_records['1. open'])
    change = end_open - start_open
    percent_changed = round(((change / start_open)*100),2)
    print (percent_changed, f'percent changed between {start_day} and {end_day}')
    return percent_changed, start_day, end_day
