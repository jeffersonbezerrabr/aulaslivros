# Programa 6.14: Lendo e imprimindo uma lista de compras - Página 174

compras = []

while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    compras.append(produto)
    
for c in compras:
    print(c)
