import pandas as pd
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

class Tabelas:
    def __init__(self):
        pass
    def download(self, dados):
        site = dados.site
        banco = MongoClient().stf.distribuicao_c
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
            banco.insert_one(dados_postados)
                
crawler = Tabelas()


sites = pd.read_csv('sites.csv')
n_linhas = sites.count()[0]

for i in range(n_linhas):
    crawler.download(sites.ix[i])
    
