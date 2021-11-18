print('')
import FlightDeals_authorizations
import requests
from twilio.rest import Client
TWILIO_ACCOUNT_SID = FlightDeals_authorizations.TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = FlightDeals_authorizations.TWILIO_AUTH_TOKEN
SHEETY_TOKEN = FlightDeals_authorizations.SHEETY_TOKEN
SHEETY_URL = 'https://api.sheety.co/f6301e01d2bbf65409260452818ab619/deniseFlightDeals/prices'
sheety_headers = SHEETY_TOKEN

class DataManager:      #This class is responsible for talking to the Google Sheet.
    def __init__(self):  #super().__init__()
        pass

    def read_sheety(self):
        my_data = requests.get(SHEETY_URL,headers=sheety_headers)
        sheety_data = my_data.json()
        print (sheety_data)
        # use this for testing to avoid 200 requests/month limit
        #sheety_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                                  #{'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 3}]}

        return (sheety_data)

    def update_iata(self, iata_code, city_row):
        new_data = {'price': {'iataCode': iata_code}}
        update_sheety = requests.put(url=f'{SHEETY_URL}/{city_row}', json=new_data, headers=sheety_headers)
        #print(update_sheety.content)
        #print(update_sheety.status_code)

    def update_price(self,f_price,city_row):
        new_price = {'price':{'lowestPrice':f_price}}
        update_sheety_price = requests.put(url=f'{SHEETY_URL}/{city_row}', json=new_price, headers=sheety_headers)
        print (f'Price updated for row: {city_row}')

    #flight_data = [r_city_to,r_airline,r_departure_date,r_departure_time]
    def send_SMS_alert(self,flight_data):
        client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=(f'LOW_FLIGHT_PRICE_ALERT!\nFlight found to: {flight_data[0]}\n'
                  f'Leaves: {flight_data[2]}, at: {flight_data[3]},\n'
                  f'on the airline: {flight_data[1]}'),
            from_='+17207039492',
            to='13033785941'
        )
        print (message.status)