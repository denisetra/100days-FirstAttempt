import requests
from bs4 import BeautifulSoup
co_homefinder_link = 'https://denver.coloradohomefinder.com/results-gallery/?city=3121&maxprice=600000&minbeds=1&minprice=200000&status=A'

#scrape w/BS4 price, address, url of place

def get_home_data():

    home_data = requests.get(co_homefinder_link)
    home_html = home_data.text
    soup = BeautifulSoup(home_html,'html.parser')
    listings_dict = {}
    all_listings = soup.find_all(class_='bt-listing-teaser')
    for item in all_listings:
        item_address = item.get('data-address')
        item_price = ((item.find(class_='listing-card__price pb-4').text).split())[0]
        item_link = item.find('a', href=True)
        my_item = item_link.get('href')

        listings_dict[item_address]= [my_item,item_price]

    return listings_dict
