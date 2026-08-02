"""Exercício 07-04: - Página 207

Escreva um programa que leia uma string e imprima quantas vezes 
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x"""

sequencia = input("Digite a string: ")

contador = {}

# for letra in sequencia:
#     contador[letra] = contador.get(letra, 0) + 1
    
# for chave, valor in contador.items():
#     print(f"{chave}: {valor}x")
    
for letra in sequencia:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

for c,v in contador.items():
    print(f"{c}: {v}x")
        