#Exercício  5.8 - Página 141

#Escreva um programa que leia dois números.
#Imprima o resultado da multiplicação do primeiro pelo segundo.
#Utilize apenas os operadores de somar e subtração para calcular o resultado.
#Lembre-se de que podemos entender a multiplicação de dois números como
#somas sucessivas de um deles. Assim:
# 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

print("Multiplicação entre dois números.")
print()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
total = 0
x = 0

while x < n2:
    total = total + n1
    x = x + 1
    
print(total)