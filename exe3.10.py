#Exercicio da página 113

salario = int(input("Informe o seu salário: "))
porcentagem = int(input("Porcentagem do aumento: "))
aumento_valor = porcentagem * salario / 100
novo_salario = aumento_valor + salario
print(f"Aumento em R$ {aumento_valor:5.2f}")
print(f"Novo salário é R$ {novo_salario:5.2f}")
