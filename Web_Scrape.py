from Web_Crawling import crawl_website
from bs4 import BeautifulSoup
import csv
import requests
URL = 'https://github.com/trending'
conteudo = crawl_website(url=URL)
pagina = BeautifulSoup(conteudo, 'html.parser')
conteudo_extraido = []
for linha in pagina.find_all('article'):
  textos_coluna = list()

  for coluna in linha.find_all('a'):
    texto_coluna = coluna.get_text().strip().split('\n')
    if texto_coluna != ['Sponsor'] and texto_coluna != ['https://cloud.qdrant.io/'] :
      textos_coluna += texto_coluna
  for coluna in linha.find_all('span'):
    texto_coluna = coluna.get_text().strip().split('\n')
    textos_coluna += texto_coluna

  linha = []
  linha.append(textos_coluna[3].strip())

  for i in range(4,6):
    linha.append(textos_coluna[i])
  linha.insert(-2,(textos_coluna[-1].split(sep=' ')[0]))

  if textos_coluna[-3] == textos_coluna[1]:
    linha.insert(1,'')
  else:
    linha.insert(1, textos_coluna[-3])
  conteudo_extraido.append(linha)
with open('github.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv, delimiter=';')
    writer.writerow(['ranking', 'project', 'language', 'stars', 'stars_today', 'forks'])
    writer.writerows(conteudo_extraido)
print(conteudo_extraido)


