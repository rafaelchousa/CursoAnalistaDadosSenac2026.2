# for i in range (-102,-1,2):
#     print(i+0,500)

#WHILE
# somador= int(input("Registro:"))
# controle= 0

# while controle <= 30:
#     controle=controle+somador
#     somador = int(input("Registro:"))

# print("Oficina lotada!")
# print("Quantidade:"  ,controle)
# O range(5) gera os números 0, 1, 2, 3, 4 (5 repetições)
# for i in range(5):
      
 # i representa o número atual da repetição (0, 1, 2...)

acertou = 0
while acertou <= 5:
    print(f"Número {acertou + 1} de 5:")
    num = float(input("Digite um número: "))
 
    dobro = num * 2
    triplo = num * 3
    quádruplo = num * 4
 
    print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
print("Entrada inválida. Tente novamente.")
num=float(input("Digite um número:"))
acertou = acertou+1




    