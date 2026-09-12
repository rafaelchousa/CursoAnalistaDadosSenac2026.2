### AUL 01 ###
#print ("sextou! (com feriado)")

import pandas as pd #alias 'pd'
import openpyxl 
# import numpy as np #alias 'np'

# print(type(numeros_impares))

# serie_impares = pd.Series(numeros_impares)
# print(serie_impares)
# print(type(serie_impares))

# print(serie_impares.sum())
# print(serie_impares.mean())
# print(serie_impares.min())
# print(serie_impares.max())
# print(len(serie_impares))
# print(serie_impares.describe())
# print(serie_impares[serie_impares>50])

# serie2_impares = pd.Series(
#     numeros_impares,
#       index=['a','b','c','d','e','f','g'])
# print(serie2_impares)

# ###  LEITURA ARQUIVOS XLSX


# leitura_invest = pd.read_excel("base_invest.xlsx", sheet_name=1)
# # print(leitura_invest)

Filmes= {
    'nome':["Lagoa Azul","Agente secreto","Gênio Indomavel","A Freira","Brinquedo Assassino","Top Gun"],
    'categoria':["Romance","Ação","Drama","Terror","Comédia","Aventura"],
    'ano':["1980","2025","1997","2022","1995","1986"],
    'faturamento':[6.5,4,5.5,3,9,1]
}

indices = ['A','B','C','D','E','F']

tabela_filmes = pd.DataFrame(Filmes,index=indices)

print(tabela_filmes)
# print(type(tabela_filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))

print(tabela_filmes.loc['E'])
print('-'*20)
print(tabela_filmes.iloc[1:4])
print(tabela_filmes.loc['B':'E'])
print('-'*20)
consulta1 = tabela_filmes.query("faturamento == 5.5")
print(consulta1)                               

