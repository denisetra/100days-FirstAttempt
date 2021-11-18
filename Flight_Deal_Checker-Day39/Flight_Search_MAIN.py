import data_manager,flight_search

#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
sheet_data = data_manager.DataManager().read_sheety()
my_prices = sheet_data['prices']
my_iata = ''
for location in my_prices:
    iata_code = location['iataCode']
    city_row_id = location['id']
    lowest_price = location['lowestPrice']
    city = location['city']
    if len(iata_code) < 1:
        my_iata = flight_search.FlightSearch().get_destination_code(city)
        location['iataCode'] = my_iata
        print (f'Checking {my_iata}')
        update_iata = data_manager.DataManager().update_iata(my_iata,city_row_id)

    loc_price_data = flight_search.FlightSearch().get_flights(my_iata)
    loc_price = loc_price_data[0]
    loc_data = loc_price_data[1]
    if loc_price < lowest_price:
        update_price = data_manager.DataManager().update_price(loc_price,city_row_id)
        my_message = data_manager.DataManager().send_SMS_alert(loc_data)


