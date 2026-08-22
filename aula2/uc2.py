

# #declarando uma variável
# idade= 30 #numero inteiro = INT
# nome= "maria" #texto= STRING
# preco= 19.99 #decimal = FLOAT

# print(idade)

#Desafio1:
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Determinar ordem
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f"{num1}, {num2}, {num3}")
    else:
        print(f"{num1}, {num3}, {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f"{num2}, {num1}, {num3}")
    else:
        print(f"{num2}, {num3}, {num1}")
else:
    if num1 <= num2:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num3}, {num2}, {num1}")


# algoritmo  BOLETIM Desafio2:
nota1 = 2
nota2 = 4

media= (nota1 + nota2)/2
print ("a média final é",media,)

#algoritmo CALCULADORA:
numero1 =9
numero2 =18
soma = (numero1+numero2)
subtracao=(numero2-numero1)
divisao=(numero2/numero1)
multiplicacao= (numero2*numero1)
print("a soma total é",soma,)
print("a subtração total é",subtracao,)
print("a divisão total é",divisao,)
print("a multiplicação total é",multiplicacao,)

