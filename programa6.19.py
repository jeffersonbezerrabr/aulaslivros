#Programa 6.19 - Criação e impressão de lista de compras

compras = []

while True:
    produto = input("Produto: ").title()
    if produto == "Sair":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for c in compras:
    print(f"{c[0]:20s} x {c[1]:5d} {c[2]:5.2f} {c[1] * c[2]:6.2f}")
    soma += c[1] * c[2]
print(f"Total: {soma:7.2f}")