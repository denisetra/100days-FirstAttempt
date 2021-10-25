import requests
from datetime import datetime
import my_email_credentials
import smtplib, ssl


my_email = my_email_credentials.my_gmail
email_pwd = my_email_credentials.my_gmail_password
my_yahoo = my_email_credentials.my_yahoo_id
my_smtp = my_email_credentials.gmail_smtp
message = 'LOOK UP!!!'

iss_url = "http://api.open-notify.org/iss-now.json"
MY_LAT = 39.734227  ## Downtown Denver
MY_LONG = -104.998187 ## Downtown Denver
#MY_LAT = 45.9 #testing
#MY_LONG = 152.3 #testing
within_range = False
my_location = (MY_LAT,MY_LONG)
parameters = {"lat": MY_LAT,"lng": MY_LONG,"formatted": 0,}

def overnight():
    my_day_api = f'https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}'
    response = requests.get(my_day_api, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = (int(data["results"]["sunrise"].split("T")[1].split('+')[0].split(':')[0])-6)
    sunset_hour = (int(data["results"]["sunset"].split('T')[1].split('+')[0].split(':')[0])-6)
    if sunrise_hour < 0:
        sunrise_hour = sunrise_hour +24
    if sunset_hour < 0:
        sunset_hour = sunset_hour + 24
    print (f'Sunrise hour: {sunrise_hour}, Sunset hour: {sunset_hour} for my_location')
    time_now = datetime.now()
    my_hour = time_now.hour

    if sunrise_hour <= my_hour <= sunset_hour:
        print('Its currently too bright to see the ISS')
    else:
        if within_range == True:
            send_lookup_email()
            print('Sending email telling you to look up')

def send_lookup_email():
    context = ssl.create_default_context()
    with smtplib.SMTP(my_smtp, port=587) as gmail:
        gmail.starttls(context=context)
        gmail.login(my_email, email_pwd)
        gmail.sendmail(
            my_email,
            my_yahoo,
            msg=f'Subject:Where is the ISS?\n\n{message}'
        )

def is_iss_overhead():
    global within_range
    response = requests.get(url=iss_url)
    response.raise_for_status()
    data = response.json()


    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_lat_high = iss_latitude + 5
    iss_lat_low = iss_latitude -5
    iss_long_high = iss_longitude + 5
    iss_long_low = iss_longitude - 5
    iss_position=(iss_latitude,iss_longitude)
    if iss_lat_high > MY_LAT > iss_lat_low and iss_long_high > MY_LONG > iss_long_low:
        within_range = True
        print ('Satelite overhead, checking time of day')
        overnight()
    else:
        print (f'ISS is currently at: {iss_position} location.')
        print (f'My location is: ({MY_LAT},{MY_LONG})')
        print ('ISS is not within range, but still checking time of day')
        overnight()

is_iss_overhead()
#TODO
# BONUS: run the code every 60 seconds.



