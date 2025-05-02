#Exercício 4.4 - Página 123

#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
#Para salários superiores a R$ 1250, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.

#Recebe o valor do salário do usuário.
salario = float(input("Digite o valor do seu salário: "))

#Verifica se o salário é maior que 1250, caso seja, executa o primeiro bloco.
if salario > 1250:
    
    #Calcula os 10% do salário
    valor_porcentagem = (salario * 0.10)
    
    #Calcula o salário + os 10%
    salario_corrigido = salario + valor_porcentagem
    
    #Exibe na tela o valor do aumento e o salario corrigido.
    print(f"Seu salário aumentou R${valor_porcentagem:5.2f}. Totalizando R${salario_corrigido:5.2f}")

#Verifica se o salário é menor ou igual a 1250, caso seja, executa o segundo bloco    
if salario <= 1250:
    
    #calcula os 15% do salário
    valor_porcentagem = (salario * 0.15)
    
    #Calcula o salário + os 15%
    salario_corrigido = salario + valor_porcentagem
    
    #Exibe na tela o valor do aumento e o salario corrigido.
    print(f"Seu salário aumentou R${valor_porcentagem:5.2f}. Totalizando R${salario_corrigido:5.2f}")
    