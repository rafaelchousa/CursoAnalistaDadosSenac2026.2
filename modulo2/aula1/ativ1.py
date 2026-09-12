import pandas as pd

transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')

# Separar compras e vendas
compras = transacoes[transacoes['operacao'] == 'compra']['preco']
vendas = transacoes[transacoes['operacao'] == 'venda']['preco']

print("=== COMPRA ===")
print(f"Máximo: R$ {compras.max():,.2f}")
print(f"Mínimo: R$ {compras.min():,.2f}")

print("\n=== VENDA ===")
print(f"Máximo: R$ {vendas.max():,.2f}")
print(f"Mínimo: R$ {vendas.min():,.2f}")