resultados = []

for i in range(1, 6):
    print(f"\nAluno {i}")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    media = (n1 + n2 + n3) / 3
    
    if media >= 7:
        status = "Aprovado"
    elif media >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"
    
    resultados.append(f"Aluno {i} - {status} (Média: {media:.1f})")
    print(f"Média: {media:.1f} - {status}")

print("\nRESULTADOS:")
for r in resultados:
    print(status)