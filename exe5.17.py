#Exercício 5.17 - Página 146

#O que acontece se digitarmos 0(zero) no valor a pagar.

#R: Ele retorna 0 cédulas de 50

#Programa 5.1 - Página 146 - Contagem de cédulas

# Solicita ao usuário que digite o valor a ser pago
valor = int(input("Digite o valor a pagar: "))

# Inicializa a variável para contar as cédulas usadas
cedulas = 0

# Inicializa a variável 'atual' com o valor da cédula de maior valor (50 reais)
atual = 50

# A variável 'apagar' recebe o valor que será pago, que começa igual ao valor digitado
apagar = valor

# Laço principal que vai continuar até o valor ser totalmente pago
while True:
    # Verifica se o valor atual da cédula é menor ou igual ao valor a ser pago
    if atual <= apagar:
        # Subtrai o valor da cédula do valor a pagar
        apagar -= atual
        # Incrementa a quantidade de cédulas usadas
        cedulas += 1
    else:
        # Se o valor da cédula for maior que o valor restante, imprime o número de cédulas usadas
        print(f"{cedulas} cédula(s) de R${atual}")
        
        # Verifica se o valor restante a pagar é zero, se sim, termina o programa
        if apagar == 0:
            break
        
        # Se não, altera para a próxima cédula de menor valor
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        
        # Reinicia a contagem de cédulas, pois estamos começando a contar cédulas de outro valor
        cedulas = 0