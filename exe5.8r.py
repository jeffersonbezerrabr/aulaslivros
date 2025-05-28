#Exercício  5.8 - Página 141

#Escreva um programa que leia dois números.
#Imprima o resultado da multiplicação do primeiro pelo segundo.
#Utilize apenas os operadores de somar e subtração para calcular o resultado.
#Lembre-se de que podemos entender a multiplicação de dois números como
#somas sucessivas de um deles. Assim:
# 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
total = 0
x = 0
while x < n2:
    total = total + n1
    x += 1
    
print(f"A multiplicação de {n1} por {n2} é igual a: {total}")