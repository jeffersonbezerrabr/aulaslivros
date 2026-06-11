# Exercício 5.13 - Página 144

# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
# Pergunte também o valor mensal que será pago. 
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

while True:
    try:
        divida = float(input("Informe o valor da dívida: "))
        if divida < 0:
            print("Dívida não pode ser negativa")
            continue
        elif divida == 0:
            print("Você não deve nada!")
            exit()
        break
    except ValueError:
        print("Precisa digitar um valor numérico!")

while True:
    try:
        juros = float(input("Informe o juro mensal (%): "))
        if juros < 0:
            print("Juro não pode ser negativo!")
            continue
        break
    except ValueError:
        print("Juro precisa ser numérico!")
        
while True:
    try:
        valor_pago_mensal = float(input("Informe o valor que será pago mensalmente: "))
        if valor_pago_mensal <= 0:
            print("Pagamento deve ser maior que zero!")
            continue
        break
    except ValueError:
        print("Valor precisa ser numérico!")

mes = 0
saldo = divida
total_pago = 0
total_juros = 0

while saldo > 0:
    juros_mes = saldo * (juros / 100)
    saldo += juros_mes
    total_juros += juros_mes

    if valor_pago_mensal <= juros_mes:
        print("A dívida nunca será quitada com esse valor mensal!")
        break

    pagamento = min(valor_pago_mensal, saldo)
    saldo -= pagamento
    total_pago += pagamento
    mes += 1

if saldo <= 0:
    print(f"Você pagou a dívida em {mes} meses")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros: R$ {total_juros:.2f}")

    