import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/newauto/marka-jaguar/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/92.0.4515.159 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='proposition_link')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': item.find('span', class_='link').get('href'),
        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        #print('ok')
    else:
        print('Error')


parse()
