#Programa 6.21.py - Obtenção do preço com um dicionário - Página 183

tabela = {"Alface": 0.45,
        "Batata": 1.20,
        "Tomate": 2.30,
        "Feijão": 1.50}
while True:
    produto = input("Digite o nome do produto, fim para terminar: ").title()
    if produto == "Fim":
        break
    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")
    else:
        print("Produto não encontrado!")
        