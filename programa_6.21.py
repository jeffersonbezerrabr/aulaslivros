# Programa 6.21: Obtenção do preço com um dicionário - Página 163

tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão": 1.50
}

while True:
    produto = input("Digite o nome do produto, Fim para terminar: ").title()
    if produto == "Fim":
        break
    elif produto in tabela:
        print(f"Preço: {tabela['produto']:5.2f}")
    else:
        print(f"{produto} não encontrado!")
