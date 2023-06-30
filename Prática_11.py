import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/chart/top/'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
  resposta = requests.get(URL, headers=headers)
  resposta.raise_for_status()
  conteudo = resposta.text
except HTTPError as exc:
  print(exc)
  conteudo = None



