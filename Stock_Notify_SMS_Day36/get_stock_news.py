import requests
import stock_program_auth_keys
import datetime as dt
from datetime import date
global article_list

today = date.today()
this_week = (today - dt.timedelta(14))

def get_news(STOCK,company_short):
    global article_list
    news_url = f'https://newsapi.org/v2/everything?qInTitle={company_short}&from={this_week}&to={today}sortBy=relevancy&pageSize=6&language=en&apiKey={stock_program_auth_keys.news_api}'
    news_returned = requests.get(news_url)
    news_data = news_returned.json()['articles']
    article_num = 1
    article_list = []
    for item in news_data:
        if article_num <= 4:
            article_num += 1
            article_dict = {}
            source = item['source']['name']
            author = item['author']
            title = item['title']
            article_url = item['url']
            article_date = item['publishedAt'].split('T')[0]
            article_dict['Source']=source
            article_dict['Author']=author
            article_dict['title']=title
            article_dict['Article_URL']=article_url
            article_dict['Article_Date']=article_date
            article_dict['**']='*******************'
            article_list.append(article_dict)
    return article_list
