# Exercício 6.12 - Página 171

# Altere o Programa 6.11 de forma a imprimir o menor elemento da lista

L = [1, 7, 2, 4]
minimo = L[0]
for c in L:
    if c < minimo:
        minimo = c
        
print(minimo)