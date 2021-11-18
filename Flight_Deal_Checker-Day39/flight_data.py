class FlightData:  #This class is responsible for structuring the flight data.
    def __init__(self):
        super().__init__()



    def airport_codes(self):
        ## input = City names
        ## output = IATA airport codes
        ## locations API
        url = 'https://tequila-api.kiwi.com/'
        loc_query = 'locations/query'

