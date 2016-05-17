# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:59:28 2016

@author: billgarden
"""

import requests
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient
import re

dist_sites = MongoClient().stf.dist_sites

data_inicial = datetime.date(year=2006, month=1, day=1)
lista_datas = [ data_inicial + datetime.timedelta(days=x) for x in range(3790)]
lista_datas[-1]


def recolhe_site_dia(dia):
    dados = {'diaAtual':dia.day,
             'mesAtual':dia.month,
             'anoAtual':dia.year
    }
    for i in range(500):
        try:           
            pagina = requests.post('http://www.stf.jus.br/portal/ataDistribuicao/listaAtaDia.asp',
                           data=dados)
        except:
            continue
    if re.search('Não há atas de distribuição para esta data', pagina.text):
        dados['site'] = 'N'  
    else:
        dados['site']=pagina.text.split('<a href="&#xA;')[1].split('">Ata')[0]
        dados['site']=dados['site'].replace('\t','').replace('&amp;','&').replace(' ','')
        dados['site'] = 'http://www.stf.jus.br/portal/ataDistribuicao/' + dados['site']
    print(dados)
    stf.dist_states(dados)
