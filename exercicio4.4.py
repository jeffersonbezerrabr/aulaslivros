# Exercício 4.4 - Página 123

# Escreva um programa que pergunte o salário do funcionário
# e calcule o valor do aumento. Para salários superiores a R$ 1250,
# calcule um aumento de 10%. Para os inferiores ou igual, de 15%.

try:
    salario = float(input("Informe o seu salário: "))
    if salario < 0:
        print("Salário não pode ser negativo!")
    else:
        if salario > 1250:
            aumento = salario * 0.10
        
        else:
            aumento = salario * 0.15
            
        print(f"Seu aumento foi de R$ {aumento:5.2f}")
        print(f"Salário após aumento: R$ {salario + aumento:5.2f}")
        
except ValueError:
    print("Valor informado precisa ser númerico")

