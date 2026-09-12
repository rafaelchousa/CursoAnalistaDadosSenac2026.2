import pandas as pd

transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
ativos = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

# Juntar para trazer o CNPJ
transacoes = transacoes.merge(ativos, on='id_ativo', how='left')

# Encontrar a linha com o maior preço
indice_max = transacoes['preco'].idxmax()
linha = transacoes.loc[indice_max]

print(f"Ativo: {linha['nome_ativo']} (id {linha['id_ativo']})")
print(f"CNPJ: {linha['cnpj']}")
print(f"Preço: R$ {linha['preco']:,.2f}")