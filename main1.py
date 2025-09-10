from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nome_lista = bs.find_all('span', {'class': 'green'})
for name in nome_lista:
    print(name.get_text())
