import requests
from bs4 import BeautifulSoup

URL = 'https://dmsu.gov.ua/services/transliteration.html'
BASE_URL = 'https://dmsu.gov.ua'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/92.0.4515.159 Safari/537.36', 'accept': '*/*'}

def getting_translation(name, surname):
    headers = {
        'referer': '{}/services.html'.format(BASE_URL)
    }
    payload = {
        'name': name,
        'surname': surname,
        #'argument': translate
    }
    r = requests.post(
        '{}/services/transliteration.html'.format(BASE_URL),
        data=payload,
       # headers=headers
    )
    r.raise_for_status()
    return r.text


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='card-container')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='bold-field').get_text(strip=True),
            #'title2': item.find('div', class_='bold-field').get_text(),
        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        #print('ok')
    else:
        print('Error')


getting_translation(surname='Шишов', name='я')

parse()
