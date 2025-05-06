#Exercício 4.7 - Página 126

#Analise o programa 4.3. Faz sentido usar o else nesse programa?
#Data 09-03-2025 - Nessa data, pra mim não faz sentido usar else
#Retornar futuramente e fazer novamente o questionamento.

#Programa 4.3

salario = float(input("Digite o sálario para cálculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
    
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
    print(f"Salário: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}")

else:
    print(f"Salário: R${salario:6.2f} Sem imposto a pagar")