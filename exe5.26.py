#Exercício 05.26 - Página 149

#Escreva um programa que calcule o resto da divisão inteira entre dois números.
#Utilize apenas as operações de soma e subtração para calcular o resultado.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if b == 0:
    print("Divisão por zero é invalida")

elif a < b:
    print(f"O resto da divisão é {a}")
    
while a >= b:
    a = a - b

print(f"O resto da divisão é {a}")