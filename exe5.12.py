#Exercício 5.12 - Página 143

#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
#Esse valor será depositado no inicio de cada mês,
#e você deve considera-lo para o calculo de juros do mês seguinte.

x = 2

dep_ini = float(input("Quanto será o deposito inicial? "))
juros = float(input("Qual a taxa de juros mensal (em %)? "))
taxa_juros = juros / 100
total_ganho_juros = 0

# Saldo inicial com o depósito inicial
saldo = dep_ini

# Loop para 24 meses
while x <= 24:
    dep_mensal = float(input(f"Valor do deposito do mês {x}? "))
    
    # Aplicar os juros sobre o saldo atual
    juros_mes = saldo * taxa_juros
    
    # Atualiza o saldo com os juros
    saldo = saldo + juros_mes
    
    # Adiciona o depósito mensal no saldo
    saldo = saldo + dep_mensal
    
    # Adiciona o valor dos juros ao total ganho com juros
    total_ganho_juros = total_ganho_juros + juros_mes
    
    # Mês seguinte
    x = x +1

# Exibir o total ganho com juros    
print(f"Total ganho com juros ao longo dos 24 meses: {total_ganho_juros:5.2f}")