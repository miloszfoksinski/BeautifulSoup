import requests
from bs4 import Beautifulsoup

result = requests.get("https://www.google.pl/")

#print(result.status_code) Sprawdzenie czy strona jest dostępna
#print(result.headers) Sprawdzenie nagłówków HTTP

src = result.content #przypisanie zawartości strony do zmiennej
#print(src)

soup = Beautifulsoup(src,'lxml') #Tworzymy obiekt Beautifulsoup oparty na zmiennej źródłowej src
links = soup.find_all('a')#Szukamy akpitów <a>, rezultatem będzie lista
print(links)

for link in links:
  if "About" in link.text :
    print(link)
    print(link.attrs['href'])

