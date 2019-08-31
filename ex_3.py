import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('Witcher_Quotes', 'w'))


result = requests.get('https://wiedzmin.pl/wiedzmin-ksiazka/wiedzmin-cytaty/ostatnie-zyczenie-cytaty')
src = result.content  
soup = BeautifulSoup(src, 'lxml')
quotes = []
for ul_tag in soup.find_all('ul') :
    li = ul_tag.find('li')
    quotes.append(li.text)
print(quotes[8:])
