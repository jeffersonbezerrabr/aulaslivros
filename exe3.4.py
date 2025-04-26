salarioimposto = 1200

print("Vamos descobrir se você precisa pagar imposto?")

salario = int(input("Qual o seu salário? "))
if salario >= salarioimposto:
    print("Você precisa declarar imposto!")
else:
    print("Você não precisa declarar imposto!")
    