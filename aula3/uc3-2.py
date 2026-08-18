# x = 15
# y = 20
# print("x é maior que y?", x > y)
# print("x é igual a y?", x == y)

#1

# tem_carteira = True
# idade = 18
# tem_carro = False
# pode_dirigir = idade >= 18 and tem_carteira
# print("Pode dirigir?", pode_dirigir)
# print("Pode dirigir e tem carro?", pode_dirigir and tem_carro)

#2
 
# cnh = True
# bebidinha = False

# posso_dirigir = cnh and bebidinha
# print(posso_dirigir)

# busaum = True
# trenzin =True

# venho_pra_aula = busaum or trenzin
# print("Venho pra aula?" ,venho_pra_aula) 

#3

locomocao = input("Diga qual sua locomacao")
choveu = True

if choveu and locomocao== "moto" :
    resultado = "Tô todo molhado :("
elif not choveu and locomocao== "moto":
     resultado="tô seco:)"
else:   
      resultado="tô seco:)"

print(resultado)      
