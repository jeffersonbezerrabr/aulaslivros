# Exercício 5.11 - Página 143

# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

while True:
    try:
        deposito = float(input("Digite o deposito inicial: "))
        if deposito <= 0:
            print("Deposito precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Valor digitado precisa ser númerico!")
        continue
    
while True:
    try:
        taxa_juros = float(input("Informe a taxa de juros: "))
        if taxa_juros <= 0:
            print("Taxa de juros precisa ser maior que 0")
            continue
        break
    except ValueError:
        print("Taxa de juros precisa ser númerico!")
        
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa_juros / 100))
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes += 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}.")