# Exercício 3.7 - Página 113

# Faça um programa que peça dois números inteiros. 
# Imprima a soma desses dois números na tela.


while True:
    try:
        n1 = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Precisa digitar um número inteiro")
        continue
    try:
        n2 = int(input("Digite outro número inteiro: "))
    except ValueError:
        print("Precisa digitar um número inteiro")
        continue
    break

soma = n1 + n2

print(f"A soma de {n1} + {n2} é: {soma}")
