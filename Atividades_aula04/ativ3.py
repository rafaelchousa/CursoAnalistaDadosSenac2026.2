# Entrada de dados
odometro_inicio = int(input("Digite a marcação do odômetro no início do dia (km): "))
odometro_final = int(input("Digite a marcação do odômetro no final do dia (km): "))
litros_gastos = int(input("Digite o número de litros de combustível gasto: "))
valor_recebido = int(input("Digite o valor total recebido dos passageiros (R$): "))

# Cálculos
distancia = odometro_final - odometro_inicio
consumo = distancia / litros_gastos  
custo = litros_gastos * 6.15  
lucro = valor_recebido - custo

# Resultados
print("\n--- RESULTADOS ---")
print(f"Distância: {distancia} km")
print(f"Consumo: {consumo:.2f} km/L")
print(f"Custo combustível: R$ {custo:.2f}")
print(f"Lucro líquido: R$ {lucro:.2f}")