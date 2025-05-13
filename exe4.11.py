#Escreva um programa para aprovar o emprestimo bancário para compra de uma casa.
#O programa deve perguntar o valor da casa a comprar,
#o salário e a quantidade de anos a pagar.
#O valor da prestação mensal não pode ser superior a 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar
#dividido pelo número de meses a pagar.

print("Verificador de emprestimo para compra de uma casa.")
print()
casa = int(input("Qual o valor da casa? "))
print()
salário = int(input("Qual o valor do seu salário? "))
print()
anos = int(input("Deseja pagar em quantos anos? "))
meses = anos * 12

valor_prestação = casa / meses

if valor_prestação > salário * 0.30:
    print("Emprestimo recusado")
    print(f"Valor da prestação é superior a 30% do salário. Valor da parcela: R${valor_prestação:5.2f}")
    
else:
    print("Emprestimo aprovado.")
    print(f"Valor da prestação é menor que 30% do salário. Valor da parcela: R${valor_prestação:5.2f}")
    