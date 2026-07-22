# Exercício 6.13 - Página 171

# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
# Faça um programa que imprima aa menor e a maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = menor = T[0]
total = 0

for c in T:
    if c < menor:
        menor = c
    if c > maior:
        maior = c
    total += c
    
media = total / len(T)

print(f"Maior Temperatura: {maior}")
print(f"Menor Temperatura: {menor}")
print(f"Média: {media}")

