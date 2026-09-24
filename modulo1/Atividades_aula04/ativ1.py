#a potência da lâmpada utilizada
#as dimensões do cômodo
#Considere que a potência necessária é de 3 watts por metro quadrado e a cada 3m² existe um bocal para uma lâmpada

#dados
potencia=int(input("digite a potência:"))
largura=int(input("digite a largura:"))
comprimento=int(input("digite o comprimento:"))
#calculos
area= largura * comprimento
potencia_necessaria = area *3
quantidade= int(area/3)

print("Área do cômodo:", area, "m²")
print("Potência necessária:", potencia_necessaria, "watts")
print("Quantidade de lâmpadas:", quantidade)
