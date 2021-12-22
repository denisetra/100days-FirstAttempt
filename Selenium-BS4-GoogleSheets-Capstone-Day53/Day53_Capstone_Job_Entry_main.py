from real_estate_search import get_home_data
from google_form import fill_out_form
#listings={'27 Folsom Street Boulder, CO 80304': ['https://denver.coloradohomefinder.com/homes/2727-Folsom-Street/Boulder/CO/80304/120361001/', '$420,000']}

def main():
    listings=get_home_data()
    fill_out_form(listings)






main()
