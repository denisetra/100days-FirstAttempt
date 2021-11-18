import FlightDeals_authorizations
import requests
from datetime import datetime, timedelta

tequila_endpoint = 'https://tequila-api.kiwi.com/'
FLIGHT_API = FlightDeals_authorizations.KIWI_API_KEY
HEADER = {'apikey': FLIGHT_API}
my_today = datetime.now()
future_year = my_today.year
day = my_today.day
date_string = my_today.strftime('%d/%m/%Y')
future_month = (my_today.month + 6) % 12
if my_today.month > 5:
    future_year = (my_today.year + 1)
future_date = f'{day}/{future_month}/{future_year}'

## response header Content-Encoding: gzip



class FlightSearch(): #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_destination_code(self,city):
        #print (f'Checking: {city}')
        query_loc_endpoint = 'locations/query'
        destination_url = tequila_endpoint+query_loc_endpoint
        parameters = {
            'location_types': 'airport',
            'limit': 5,
            'active_only': True,
            'term': city

        }
        my_iata_codes = requests.get(url=destination_url, headers=HEADER, params=parameters)
        my_codes = my_iata_codes.json()
        #print(my_iata_codes.content)
        found_iata = my_codes['locations'][0]['id']
        return (found_iata)

    def get_flights(self,my_iata):
        flight_parameters = {'fly_from': 'LON',
                             'fly_to': my_iata,
                             'date_from': date_string,
                             'date_to': future_date,
                             'nights_in_dst_from': 7,
                             'nights_in_dst_to': 28,
                             'flight_type': 'round',
                             'adults': 1,
                             'curr': 'GBP',
                             'max_stopovers': 0,
                             'max_sector_stopovers': 0,
                             'vehicle_type': 'aircraft',
                             'limit': 1
                             }

        search_endpoint = 'v2/search'
        search_url = tequila_endpoint+search_endpoint
        my_flights_data = requests.get(url=search_url,headers=HEADER, params=flight_parameters)
        my_flights= my_flights_data.json()
        r_price = my_flights['data'][0]['price']
        r_departure_date = my_flights['data'][0]['local_departure'].split('T')[0]
        r_departure_time = my_flights['data'][0]['local_departure'].split('T')[1].split('.')[0]
        r_airline = my_flights['data'][0]['airlines'][0]
        r_city_to = my_flights['data'][0]['cityTo']
        flight_data = [r_city_to,r_airline,r_departure_date,r_departure_time]
        print (r_price)
        return (r_price,flight_data)