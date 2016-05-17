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
from multiprocessing import Pool
#import socks
#import socket
#import subprocess

#socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
#socket.socket = socks.socksocket

dist_sites = MongoClient().stf.dist_sites

data_inicial = datetime.date(year=2006, month=1, day=1)
lista_datas = [ data_inicial + datetime.timedelta(days=x) for x in range(3790)]


def recolhe_site_dia(dia):
    print(dia)
    dados = {'diaAtual':dia.day,
             'mesAtual':dia.month,
             'anoAtual':dia.year
    }
    for i in range(500):
        try:           
            pagina = requests.post('http://www.stf.jus.br/portal/ataDistribuicao/listaAtaDia.asp',
                           data=dados)
            break
        except:
            continue
    if re.search('Não há atas de distribuição para esta data', pagina.text):
        dados['site'] = 'N'  
    else:
        dados['site']=pagina.text.split('<a href="&#xA;')[1].split('">Ata')[0]
        dados['site']=dados['site'].replace('\t','').replace('&amp;','&').replace(' ','')
        dados['site'] = 'http://www.stf.jus.br/portal/ataDistribuicao/' + dados['site']
    print(dados)
    dist_sites.insert(dados)

p = Pool(10)
p.map(recolhe_site_dia, lista_datas)

#v = 0
#for i in lista_datas:
#    if ( v % 40 == 0 ):
#        subprocess.Popen("sudo /etc/init.d/tor reload".split())
#    recolhe_site_dia(i)
#    v += 1

