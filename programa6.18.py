#Programa 6.18 - Impressão das compras

produto1 = ["Maça", 10, 0.30]
produto2 = ["Pera", 5, 0.75]
produto3 = ["Kiwi", 4, 0.98]

compras = [produto1, produto2, produto3]
for i in compras:
    print(f"\nProduto: {i[0]}")
    print(f"Quantidade: {i[1]}")
    print(f"Preço: {i[2]:5.2f}\n")
    # print(compras[1][2]) #[1] representa a primeira lista. [2] representa o indice 2
    