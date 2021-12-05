from bs4 import BeautifulSoup
import requests
from send_email import send_gmail

PRODUCT_URL = 'https://smile.amazon.com/Stack-100-Compostable-Paper-Plates/dp/B07MQG9H6R/ref=sxts_rp_s1_0?cv_ct_cx=paper+plates&keywords=paper+plates&pd_rd_i=B07MQG9H6R&pd_rd_r=20a1184c-5565-43aa-a5ed-b6b152ab5e6e&pd_rd_w=FNwZd&pd_rd_wg=Ng8HZ&pf_rd_p=29dcfc78-5030-4047-b3bb-fd095cf7aa8a&pf_rd_r=K8ERFDAZND04365R02F6&psc=1&qid=1638555831&sr=1-1-f0029781-b79b-4b60-9cb0-eeda4dea34d6'
HEADERS = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.20 Safari/537.36'
}
ITEM_NAME ='Paper_Plates, Compostable'
def check_price():
    data = (requests.get(PRODUCT_URL,headers=HEADERS)).text
    soup = BeautifulSoup(data,'lxml')

    price = soup.find_all(class_='a-price a-text-price a-size-medium')
    for thing in price:
        my_price = thing.find_all(class_='a-offscreen')
        the_price = float((my_price[0].getText()).split('$')[1])
        return the_price



current_price = check_price()
if current_price < 20.75:
    sending_mail = send_gmail(current_price,ITEM_NAME)

