'''
import requests
from requests.exceptions import HTTPError
print(requests.__version__)

#método
resposta = requests.get('http://www.google.com')
print(resposta.status_code)

#Verificar código
conteudo = None
URL = 'http://www.google.com'

try:
    resposta = requests.get(URL)
    resposta.raise_for_status()
except HTTPError as exc:
    print(exc)
else:
    conteudo = resposta.text
print(conteudo)
'''

# "Web Crawl - sites fornecem um arquivo chamado robots.txt para informar como um web crawler pode interajir com a página"
import requests
from requests.exceptions import HTTPError


def crawl_website(url: str) -> str:
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        params = dict(lang='en-US,en;q=0.5')

        resposta = requests.get(url, headers=headers, params=params)

        resposta.raise_for_status()

    except HTTPError as exc:

        print(exc)

    else:

        return resposta.text
'''
URL = 'https://en.wikipedia.org/robots.txt'
conteudo = crawl_website(url=URL)
print(conteudo)
'''

'''
URL = 'https://en.wikipedia.org/wiki/Web_crawler'
conteudo = crawl_website(url=URL)
print(conteudo)
'''