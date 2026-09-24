candidatos_validos = []

for i in range(1, 6):
    print(f"\n--- Candidato {i} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    if idade < 18:
        print("Candidato REJEITADO (menor de idade)")
    else:
        email = input("Email: ")
        candidato = {'nome': nome, 'email': email}
        candidatos_validos.append(candidato)
        print("Candidato APROVADO!")

print("\n" + "="*40)
print("CANDIDATOS VÁLIDOS:")
for c in candidatos_validos:
    print(f"Nome: {c['nome']} - Email: {c['email']}")