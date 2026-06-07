# Exercício 5.8 - Página 141

# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

while True:
    try:
        n1 = int(input("n1: "))
        if n1 < 1:
            print("Valor informado precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Valor precisa ser númerico e positivo!")
        
while True:
    try:
        n2 = int(input("n2: "))
        if n2 < 1:
            print("Valor informado precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Valor precisa ser númerico e positivo!")
        
x = 1
total = n1

while x < n2:
    total += n1
    x += 1
    
print(total)