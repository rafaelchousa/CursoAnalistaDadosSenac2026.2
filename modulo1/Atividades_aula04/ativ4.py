codigo = int(input("Digite o código de origem do produto: "))

# Verificando a região
if codigo == 1:
    regiao = "Sul"
elif codigo == 2:
    regiao = "Norte"
elif codigo == 3:
    regiao = "Leste"
elif codigo == 4:
    regiao = "Oeste"
elif codigo == 5 or codigo == 6:
    regiao = "Nordeste"
elif 7 <= codigo <= 9:  # Intervalo de 7 a 9
    regiao = "Sudeste"
elif codigo == 10:
    regiao = "Centro-Oeste"
elif codigo == 11:
    regiao = "Noroeste"
else:
    regiao = "Importado"

print(f"Região de procedência: {regiao}")