n1 = int(input("Digite a nota da primeira avaliação: "))
n2 = int(input("Digite a nota da segunda avaliação: "))
optativa = int(input("Digite a nota da avaliação optativa (-1 se não fez): "))

# Verificando se o aluno fez a optativa
if optativa != -1:
    # Encontrando a menor nota entre N1 e N2
    if n1 < n2:
        menor_nota = n1
    else:
        menor_nota = n2
    
    # Substituindo a menor nota pela optativa
    if n1 < n2:
        n1 = optativa  
    else:
        n2 = optativa  

# Calculando a média (média das duas notas)
media = (n1 + n2) / 2

if media >= 6.0:
    situacao = "Aprovado"
elif media < 3.0:
    situacao = "Reprovado"
else: 
    situacao = "Recuperação"

# Exibindo os resultados
print(f"\nNota 1: {n1:.1f}")
print(f"Nota 2: {n2:.1f}")
print(f"Média final: {media:.1f}")
print(f"Situação: {situacao}")