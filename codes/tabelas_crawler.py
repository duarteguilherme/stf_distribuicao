import pandas as pd
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

class Tabelas:
    def __init__(self):
        pass
    def download(self, dados):
        site = dados.site
        print(site)
        banco = MongoClient().stf.desde_barbosa
        pagina = requests.get(site)
        pagina = BeautifulSoup(pagina.text, 'html.parser')
        resultado_lista = pagina.find(attrs={"class":"resultadoLista"})
        tabela = resultado_lista.find_all('tr')[1:]
        for j in tabela:
            td = j.find_all('td')
            dados_postados = {}
            dados_postados['dia'] = int(dados.diaAtual)
            dados_postados['mes'] = int(dados.mesAtual)
            dados_postados['ano'] = int(dados.anoAtual)
            dados_postados['ministro'] = td[0].get_text()
            dados_postados['distribuido'] = td[1].get_text()
            dados_postados['redistribuido'] = td[2].get_text() 
            dados_postados['total'] = td[3].get_text() 
            print(dados_postados)
#            banco.insert_one(dados_postados)
    def download2(self, dados):
        site = dados.site
        print(site)
        banco = MongoClient().stf.distribuicao_c
        pagina = requests.get(site)
        pagina = BeautifulSoup(pagina.text, 'html.parser')
        a_s = pagina.find_all('table', attrs={'class':'comum'})
        for j in a_s:
            ah = j.find_all('a')
            if len(ah) == 1:
#                print(ah)
                dados_postados = {}
                dados_postados['dia'] = int(dados.diaAtual)
                dados_postados['mes'] = int(dados.mesAtual)
                dados_postados['ano'] = int(dados.anoAtual)
                dados_postados['link'] = ah[0]['href']
                try:
                    dados_postados['tipo_distribuicao'] = j.find('span').text 
                except:
                    dados_postados['tipo_distribuicao'] = ""
                dados_postados['acao'] = ah[0].text
#                print(j)
                for v in j.find_all('tr'):
#                    print(v)
                    if 'Relator' in v.text:
                        dados_postados['relator'] = v.text
                print(dados_postados)
                banco.insert_one(dados_postados)
#            dados_postados['ministro'] = td[0].get_text()
#            dados_postados['distribuido'] = td[1].get_text()
#            dados_postados['redistribuido'] = td[2].get_text() 
#            dados_postados['total'] = td[3].get_text() 
#            print(dados_postados)
                
crawler = Tabelas()


sites = pd.read_csv('sites.csv')
n_linhas = sites.count()[0]


#crawler.download2(sites.ix[i-1])
for i in range(n_linhas):
    crawler.download2(sites.ix[i])
    
