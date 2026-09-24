#SETS:

# numeros_pares = {
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292,
#     202
# }
# # print(numero_pares,type(numero_pares))
# numeros_impares = {111,111,112,291,291,205}
# print(numeros_pares.intersection(numeros_impares))
# numeros_pares.remove(205)
# print(numeros_pares)

#DICIONÁRIOS:

produtos = {"maçã":5.99,"laranja":4.79}
#print(produtos,(type(produtos)))
print(produtos.items())
print(produtos.keys())
print(produtos.values)
print(produtos.get("laranja"))
produtos2=produtos.copy()
print(produtos2)
# produtos2.pop("maçã")
produtos2["maça"]=7.99
print(produtos2)
###
achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)