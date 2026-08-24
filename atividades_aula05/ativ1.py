# Inicializando contadores
aprovados = 0
reprovados = 0
recuperacao = 0

# Laço para 10 alunos
for aluno in range(1, 11):
    print(f"\n--- Aluno {aluno} ---")
    
    # Entrada das notas
    n1 = int(input("Digite a nota da primeira avaliação: "))
    n2 = int(input("Digite a nota da segunda avaliação: "))
    optativa = int(input("Digite a nota da avaliação optativa (-1 se não fez): "))
    
    # Verificando se o aluno fez a optativa
    if optativa != -1:
        # Encontrando a menor nota entre N1 e N2
        if n1 < n2:
            n1 = optativa
        else:
            n2 = optativa
    
    # Calculando a média
    media = (n1 + n2) / 2
    
    # Verificando a situação do aluno
    if media >= 6.0:
        situacao = "Aprovado ✅"
        aprovados += 1
    elif media < 3.0:
        situacao = "Reprovado ❌"
        reprovados += 1
    else:
        situacao = "Recuperação 📚"
        recuperacao += 1
    
    # Exibindo o resultado do aluno
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")

# Estatísticas finais
print("\n" + "="*40)
print("RELATÓRIO FINAL")
print("="*40)
print(f"Total de alunos: 10")
print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
print("="*40)