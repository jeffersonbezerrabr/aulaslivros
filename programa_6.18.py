# Programa 6.18: Impressão de compras - Página 175

produto1 = ["Maçã", 10, 0.30]
produto2 = ["Pêra", 5, 0.75]
produto3 = ["Kiwi", 4, 0.98]

compras = [produto1, produto2, produto3]

for c in compras:
    print(f"Produto: {c[0]}")
    print(f"Quantidade: {c[1]}")
    print(f"Valor: R$ {c[2]:5.2f}\n")
