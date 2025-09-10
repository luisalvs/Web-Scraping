from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_titulo(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = get_titulo('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Título não exite')
else:
    print(title)
