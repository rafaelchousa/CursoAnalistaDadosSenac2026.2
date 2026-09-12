import pandas as pd

transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
participantes = pd.read_excel('base_invest.xlsx', sheet_name='Participante')

# Calcular o valor de cada transação
transacoes['valor_total'] = transacoes['quantidade'] * transacoes['preco']

# Juntar com o nome do participante
transacoes = transacoes.merge(participantes, on='id_participante', how='left')

# Agrupar por participante e somar
total = transacoes.groupby(['id_participante', 'nome_participante'])['valor_total'].sum()

print(total)