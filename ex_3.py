import requests
from bs4 import BeautifulSoup

# import pandas

page = requests.get('https://pogoda.interia.pl/')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
cities = soup.find(class_='weather-index')
# print(cities)

