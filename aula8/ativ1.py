def calcular_imc (peso,altura):
    return peso/(altura*altura)

def obter_classificacao(imc):
    if imc < 18.5:
        classificacao = "Abaixo do peso🤔"
    elif imc < 25:
        classificacao = "Peso normal👍"
    elif imc < 30:
        classificacao = "Sobrepeso👎"
    else:
        classificacao = "Obesidade😢"
    return classificacao

n = int(input("Quantas pessoas?"))
for i in range(n):
    peso = (float(input("Peso: ")))
    altura = (float(input("Altura: ")))
    imc = calcular_imc(peso,altura)
    print(imc, obter_classificacao(imc))

