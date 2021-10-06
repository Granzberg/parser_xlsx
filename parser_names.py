import requests
import json

BASE_URL = 'https://dmsu.gov.ua/services'


def getting_translation():
    headers = {
        'referer': '{}/services.html'.format(BASE_URL)
    }
    payload = {
        'name': 'Андрій',
        'surname': 'Шишов',
        #'argument': translate,
    }
    r = requests.post(
        '{}/transliteration.html'.format(BASE_URL),
        json=payload,
        #headers=headers
    )
    r.raise_for_status()
    return r.text

print(getting_translation())

# https://coderoad.ru/48847881/Python-3-%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%84%D0%BE%D1%80%D0%BC%D1%8B-%D1%81-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%BC-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0-%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D1%82-%D1%82%D1%83-%D0%B6%D0%B5-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%83-HTML

# https://ru.stackoverflow.com/questions/1136050/%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0-%D1%81-%D1%81%D0%B0%D0%B9%D1%82%D0%B0-python