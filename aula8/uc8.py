import time

# 1. DEFINIÇÃO da função
def dar_boas_vindas():
    print("-"*40)
    print("  Bem-vindo ao nosso aplicativo! 😀")
    print("-"*40)

# 2. CHAMADA da função
# O código abaixo só será executado se você "chamar" a função pelo nome:

print("Início do programa.")
print('Por favor, aguarde...')
time.sleep(2)  # Simula uma pausa
dar_boas_vindas()  # <-- Isso executa o código dentro da função
print("Meio do programa.")
dar_boas_vindas()  # <-- Podemos chamar de novo!
print("Fim do programa.")
# 'nome_da_pessoa' é um PARÂMETRO.
# É uma variável que só existe dentro da função.
def boas_vindas_personalizado(nome_da_pessoa):
    print("-"*40)
    print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)! 😀")
    print("-"*40)

