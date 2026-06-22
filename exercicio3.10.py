# Exercício 3.10 - Página 113

# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

while True:
    try:
        salario = float(input("Informe o valor do salário: "))
        if salario <= 0:
            print("Salário precisa ser maior que 0")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break
    
while True:
    try:
        aumento = float(input("Informe a porcentagem do aumento: "))
        if aumento < 0:
            print("Aumento não pode ser negativo")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

valor_aumento = salario * (aumento / 100)
novo_salario = salario + valor_aumento
    
print(f"Valor do aumento: R$ {valor_aumento:5.2f}")
print(f"Novo Salário: R$ {novo_salario:5.2f}")