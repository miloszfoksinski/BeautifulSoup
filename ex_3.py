import requests
from bs4 import BeautifulSoup

# import pandas

page = requests.get('https://pogoda.interia.pl/')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
cities_blocks = soup.find(class_='weather-index')
cities = cities_blocks.find_all('a')

# print(cities[0].string.strip())
temperatures = cities_blocks.find_all('span')
print(temperatures[0].string)

citiesnames = [ city.find('a').get_text() for city in cities]
#city = cities.find('a')
#print(city.text)

