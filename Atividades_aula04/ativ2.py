print("CÁLCULO DE AZULEJOS")
print()

comprimento = int(input("Digite o comprimento da cozinha (em metros): "))
largura = int(input("Digite a largura da cozinha (em metros): "))
altura = int(input("Digite a altura da cozinha (em metros): "))

area_total = 2 * (comprimento * altura) + 2 * (largura * altura)
caixas = (area_total * 10 + 14) // 15

print()
print("RESULTADO")
print(f"Área total: {area_total} m²")
print(f"Caixas necessárias: {caixas}")