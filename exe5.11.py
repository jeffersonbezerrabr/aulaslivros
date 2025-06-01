#Exercício 5.11 - Página 143

#Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança.
#Exiba os valores mês a mês para os 24 primeiros meses.
#Escreva o total ganho com juros no periodo.

x = 1

dep_ini = float(input("Qual o valor do depósito inicial? "))  # Alterado para float, pois pode ter valores com casas decimais
juros = float(input("Qual a taxa de juros mensal (em %)? "))  # Alterado para float e com % explícito
taxa_juros = juros / 100  # Dividir por 100 para converter em porcentagem
total_ganho_juros = 0  # Para armazenar o total ganho com juros

# Inicialização do saldo com o valor do depósito inicial
saldo = dep_ini

# Loop para os 24 meses
while x <= 24:
    # Exibe o saldo de cada mês
    print(f"Mês {x}: {saldo:5.2f}")
    
    # Calcula os juros do mês e atualiza o saldo
    juros_mes = saldo * taxa_juros
    saldo = saldo + juros_mes
    
    # Acumula o total ganho com juros
    total_ganho_juros = total_ganho_juros + juros_mes
    
    # Avança para o próximo mês
    x = x + 1

# Exibe o total ganho com juros ao final de 24 meses
print(f"Total ganho com juros ao longo dos 24 meses: {total_ganho_juros:5.2f}")


'''x = 1

dep_ini = int(input("Qual o valor do deposito inicial? "))
juros = int(input("Qual a taxa de juros? "))
taxa_juros = juros / 30
total = dep_ini


while x <= 24:
    print(f"Mês {x}: {dep_ini:5.2f}")
    dep_ini = dep_ini + (dep_ini * taxa_juros)
    total = total + dep_ini
    x = x + 1
    
print(f"Total ao longo dos 24 meses: {total / 24:5.2f}")'''