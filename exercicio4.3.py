# Exercício 4.3 - Página 123

# Escreva um programa que leia três números e que imprima o maior e o menor.

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

maior = a
if b > a and b > c:
    maior = b

if c > a and c >= b:
    maior = c
    
menor = a

if b < c and b < a:
    menor = b
    
if c <= b and c < a:
    menor = c
    
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
