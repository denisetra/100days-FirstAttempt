from bs4 import BeautifulSoup
import requests
URL ="https://www.imdb.com/chart/top/"
#  class uses a '.' dot    an id, use a pound "#"
move = requests.get(URL)
webpage_html = move.text

soup = BeautifulSoup(webpage_html, 'html.parser')
#print(soup.prettify())
#  class uses a '.' dot    an id, use a pound "#"
movie_list = {}
#print(soup.prettify())
all_movies = soup.find_all(class_="titleColumn")[:100]
for picture in all_movies:
    info = picture.getText()
    num = int(info.split()[0].split('.')[0])
    movie = info.split('\n')[2]
    movie = movie.lstrip()

    movie_list[num]= movie
print(movie_list)