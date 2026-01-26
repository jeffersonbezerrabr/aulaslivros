# Exercício - 6.12 - Altere o programa 6.11 de forma a imprimir o menor elemento da lista.

L = [1, 7, 2, 4, 0]

minimo = L[0]

for c in L:
    if c < minimo:
        minimo = c
        
print(minimo)

print(f"O maior valor é {max(L)}")
print(f"O menor valor é {min(L)}")