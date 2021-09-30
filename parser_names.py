import requests
from requests.exceptions import HTTPError

# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#
#         # если ответ успешен, исключения задействованы не будут
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')

# response = requests.get('https://api.github.com/search/repositories',
#                         params={'q': 'requests+language:python'},
#                         headers={'Accept': 'application/vnd.github.v3.text-match+json'},)
#
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Text matches: {repository["text_matches"]}')  # Python 3.6+
#

r = requests.post('https://httpbin.org/post', data=[('key', 'value')])
print(r)
