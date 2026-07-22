# A lista de temperatura de Mons, na Bélgica, foi armazenada na lista: 
# T = [-10, -8, 0, 1, 2, 5, -2, -4]
# Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]

maior = menor = T[0]
soma = 0

for c in T:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    soma += c
    
media = soma / len(T)

print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Média: {media}")
