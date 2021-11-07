import requests
from twilio.rest import Client
TWILIO_ACCOUNT_SID = 'hidden'
TWILIO_AUTH_TOKEN ='hidden'
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

# hourly forecast for next 48 hours for Denver
my_key ='hidden'
#my_key = os.environ.get("OWM_API_KEY")
my_lat = ''
my_long = ''
exclude = 'current,minutely,daily,alerts'
my_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
test_lat = '38.55'
test_long = '131.36'
parameters = {
    'appid': my_key,
    'exclude': exclude,
    'lat': test_lat,
    'lon': test_long,
    'units': 'imperial'
}
call = response = requests.get(my_endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()
twelve_hour_forcast = weather_data['hourly'][:12]
twelve_hour_condition_codes = []
wet_hours = []
moisture = False
for hour in twelve_hour_forcast:
    my_weather = hour['weather'][0]['id']
    if my_weather < 700:
        moisture = True
        hour_wet = hour['weather'][0]
        wet_info = hour_wet['main']
        wet_hours.append(wet_info)
        total_wet = len(wet_hours)
if moisture == True:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Don't forget your umbrella!  ☂️",
        from_='+17207039492',
        to= '13033785941'
    )

    print(message.status)
#
#
#
#
#   else:
    #print ('Enjoy the next two DRY days')





