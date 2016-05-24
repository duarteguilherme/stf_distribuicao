import pandas as pd
import requests
from bs4 import BeautifulSoup

class Tabelas(self):
    def __init__(self):
        pass



sites = pd.read_csv('sites.csv')
n_linhas = sites.count()[0]

for i in range(n_linhas):
    crawler.download(sites.ix[i].site)
    
