import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('Witcher_Quotes.csv', 'w'))

pages = []
books = ['ostatnie-zyczenie', 'miecz-przeznaczenia', 'krew-elfow', 'czas-pogardy', 'cos-sie-konczy-cos-sie-zaczyna' ]
for i in range(0, 5):
    url = 'https://wiedzmin.pl/wiedzmin-ksiazka/wiedzmin-cytaty/' + books[i] + '-cytaty'
    pages.append(url)
for page in pages:

    result = requests.get(page)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    quotes = []
    for ul_tag in soup.find_all('ul'):
        li = ul_tag.find('li')
        quotes.append(li.text)
        f.writerow(li.text)
    print(quotes[8:])
