# -*- coding: utf-8 -*-
#
# Script para obter os resultados da pesquisa Google por artigos e
# reportagens relacionadas ao saneamento básico em Arraial do Cabo em sites
# especificados.
#
# Sinta-se livre para utilizar, adaptar e criar a partir deste arquivo para
# fins não comerciais, atribuindo o devido crédito (CC BY-NC). 
#
# Rui Valporto, set 18
# https://github.com/ruivalporto
# https://ruivalporto.wordpress.com/
#

from bs4 import BeautifulSoup
import requests

### FUNÇÕES
def texto_de_url(url):
    noticia_html = requests.get(url).text
    soup = BeautifulSoup(noticia_html, 'html.parser')
    recorte = ""
	
	# Cada portal de notícias usa uma formatação diferente!
    site = url[:15]
    if site == "http://camara.a":
        try:
            recorte = soup.findAll('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif site == "http://g1.globo":
        try:
            recorte = soup.find('div', attrs={"class": "materia-conteudo entry-content clearfix"}).find_all('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif site == "http://jornalde":
        try:
            recorte = soup.find('div', attrs={"class": "td-post-content"}).find_all('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif (site == "http://rc24h.co") or (site == "http://www.rc24"):
        try:
            recorte = soup.find('div', attrs={"class": "news"}).findAll('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif site == "http://www.asha":
        try:
            recorte = soup.find('div', attrs={"class": "entry-content"}).find_all('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif site == "http://www.folh":
        try:
            recorte = soup.find('div', attrs={"class": "text-principal b-separador p-b-30"}).find_all('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif site == "http://www.jb.c":
        try:
            recorte = soup.find_all('p', attrs={"class": "texto"})
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    elif site == "http://oglobo.g":
        try:
            recorte = soup.find('div', attrs={"class": "corpo novo large-16 columns paywalled-content"}).find_all('p')
            print("Ok!")
        except Exception:
            print("Erro2 - " + url)
            pass
    else:
        print("Erro1 - " + url[:30])
        return ("ERROERROERRO1" + url)
    
    soup = BeautifulSoup(str(recorte), 'html.parser')
    return soup.get_text().replace(u'\xa0', u' ').replace('\u200b', u' ')

### PARÂMETROS
# Modo de importação
# 0: Carrega a lista de urls ignorando as duplicadas.
# 1: Carrega a lista de urls removendo as duplicadas.
modo_de_importacao = 0
nome_do_arquivo_de_entrada = 'noticias_url_set.txt'
nome_do_arquivo_de_saida = 'textos.txt'

### IMPORTAÇÃO
if modo_de_importacao == 0:
    with open(nome_do_arquivo_de_entrada) as a:
        print("Carregando url's ignorando as duplicadas...")
        noticias_url = a.read().splitlines()
elif modo_de_importacao == 1:
    with open(nome_do_arquivo_de_entrada) as a:
        print("Carregando url's removendo as duplicadas...")
        noticias_url = list(set(a.read().splitlines()))
else:
    print("Erro: modo de importação inválido!")
	
print("Total de %i url's carregadas!\n" % len(noticias_url))


with open(nome_do_arquivo_de_saida, 'w') as f:
    for i in range(len(noticias_url)):
        print("Lendo página %i de %i..." % ((i+1), len(noticias_url)))
        t = texto_de_url(noticias_url[i])
        f.write("%s\n" % t)        