#Programa 6.14 - Lendo e imprimindo uma lista de compras - Página 174

compras = []
while True:
    produto = input("Produto: ").title()
    if produto == "Fim":
        break
    compras.append(produto)
for compra in compras:
    print()
    print(compra)
    