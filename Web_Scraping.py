from bs4 import BeautifulSoup
pagina = BeautifulSoup(open('lotr.html', mode='r'), 'html.parser')
filmes_li = pagina.find_all('li')
print(filmes_li)
print(list(set(map(lambda filmes_li: type(filmes_li), filmes_li))))

filmes = []
for filme_li in filmes_li:
    filme = filme_li.get_text()
    ano = int(filme.split(sep=':')[0].strip())
    titulo = ':'.join(filme.split(sep=':')[1:]).strip()
    filmes.append({'ano': ano, 'titulo': titulo})
    for filme in filmes:
        print(filme)
