print("="*50)
print("CADASTRO DE CANDIDATOS - 12 PESSOAS")
print("="*50)

# Contador de candidatos cadastrados
cadastrados = 0

for candidato in range(1, 13):
    print(f"\n--- CANDIDATO {candidato} ---")
    
    # Entrada do ano de nascimento
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    
    # Calculando a idade (considerando ano atual 2026)
    idade = 2026 - ano_nascimento
    
    # Verificando se é menor de 18 anos
    if idade < 18:
        print(f"❌ Candidato menor de 18 anos ({idade} anos). Não pode participar!")
        print("Cadastro interrompido para este candidato.")
        continue  # Pula para o próximo candidato
    
    # Se chegou aqui, é maior de 18 anos
    print(f"✅ Candidato tem {idade} anos. Pode participar!")
    
    # Coleta dos demais dados
    nome = input("Digite o nome completo: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    endereco = input("Digite o endereço: ")
    
    # Exibe confirmação
    print(f"\n📋 Candidato {candidato} cadastrado com sucesso!")
    print(f"   Nome: {nome}")
    print(f"   Telefone: {telefone}")
    print(f"   E-mail: {email}")
    
    cadastrados += 1

# Estatísticas finais
print("\n" + "="*50)
print("RELATÓRIO FINAL")
print("="*50)
print(f"Total de candidatos avaliados: 12")
print(f"Candidatos cadastrados (maiores de 18): {cadastrados}")
print(f"Candidatos descartados (menores de 18): {12 - cadastrados}")
print("="*50)