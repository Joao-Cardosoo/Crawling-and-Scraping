'''
import json
#ler o arquivo JSON
data = json.load(open(file='lotr.json', mode='r'))
print(data)

#Transformar em um dicionário
data_json = json.dumps(data, indent=4, ensure_ascii=False)
print(data_json)
'''
from Web_Crawling import crawl_website
import json
URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'
conteudo = crawl_website(url=URL)
print(conteudo)
print(type(conteudo))

data = json.loads(conteudo)
print(data)
cdi = float(data['taxa'].replace(',', '.'))
print(type(data))
print(cdi)

data_json = json.dumps(conteudo, indent=4, ensure_ascii=False)
print(data_json)
print(type(data_json))