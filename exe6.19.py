#Altere o programa 6.22 de forma a solicitar ao usuário
#o produto e a quantidade vendida.
#Verifique se o nome do produto digitado existe no dicionário,
#e só então efetue a baixa em estoque.

#Programa 6.22: Exemplo de dicionário com estoque e operações de venda

estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}

total = 0
print("Vendas:\n")

while True:
    venda = input("Qual produto deseja comprar (ou 'fim' para sair): ")
    
    # Verifica se quer sair
    if venda == 'fim':
        break
    
    # Verifica se o produto existe
    if venda in estoque:
        qntd = int(input("Quantos deseja levar: "))
        
        # Verifica se tem estoque suficiente
        if qntd <= estoque[venda][0]:
            preco = estoque[venda][1]
            custo = preco * qntd
            print(f"{venda:12s}: {qntd:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[venda][0] -= qntd
            total += custo
        else:
            print(f"Estoque insuficiente! Temos apenas {estoque[venda][0]} unidades.")
    else:
        print("Produto não encontrado! Digite um destes:")
        print(", ".join(estoque.keys()))

print(f"\nCusto total: {total:21.2f}")
print("\nEstoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")