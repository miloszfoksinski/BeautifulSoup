import requests
from bs4 import BeautifulSoup

result = requests.get('https://wiedzmin.pl/wiedzmin-ksiazka/wiedzmin-cytaty/ostatnie-zyczenie-cytaty')
src = result.content  
soup = BeautifulSoup(src, 'lxml')
quotes = soup.find_all('ul')
