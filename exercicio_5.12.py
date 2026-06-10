# Exercício 5.12 - Página 143

# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no inicio de cada mês, 
# e você deve considerá-lo para o cálculo de juros do mês seguinte.

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
        
while True:
    try:
        deposito_mensal = float(input("Informe quanto irá depositar mensalmente: "))
        if deposito_mensal <= 0:
            print("Deposito mensal precisa ser maior que 0")
            continue
        break
    except ValueError:
        print("Deposito mensal precisa ser númerico!")
        
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa_juros / 100)) + deposito_mensal
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes += 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}.")