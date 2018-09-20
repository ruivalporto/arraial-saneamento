# -*- coding: utf-8 -*-

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

from googlesearch import search
# Script de Mario Vilas (https://github.com/MarioVilas/googlesearch)
# baseado no BeautifulSoup para obter URL's dos resultados de pesquisas
# no Google. Atenção: como o script não passa pela API oficial do Google,
# pesquisas muito extensas em intervalos muito curtos de tempo podem ser
# temporariamente bloqueadas (erro 503). Uma estratégia é dividir
# palavras_chave e sites_de_noticias em partes menores e executar o script
# com uma de cada vez. Aparentemente, diminuir numero_de_resultados não
# é muito eficaz.

def pesquisa_google(termo, site, qtd):
	r = []
	s = str("site:" + site + " \"" + termo + "\" \"Arraial do Cabo\"")
	for url in search(s, stop = qtd):
		r.append(url)
	return r

### PARÂMETROS
palavras_chave = [
	"saneamento",
	"esgoto",
	"agua potavel",
	"lixo"
]
sites_de_noticias = [
	# do RJ e do Brasil
	"globo.com",
	"jb.com.br",
	# da Regiao dos Lagos
	"ashama.com.br",
	"rc24h.com.br",
	"folhadoslagos.com",
	"jornaldesabado.net",
	# de Arraial do Cabo
	"camara.arraial.rj.gov.br"
]
numero_de_resultados = 5
nome_do_arquivo_de_saida = 'noticias_url.txt'

### SCRIPT
noticias_url = []
for t in palavras_chave:
	for j in sites_de_noticias:
		noticias_url += pesquisa_google(t, j, numero_de_resultados)
		
with open(nome_do_arquivo_de_saida, 'w') as f:
    for i in noticias_url:
        f.write("%s\n" % i)