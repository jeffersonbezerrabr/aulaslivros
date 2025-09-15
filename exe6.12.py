#Exercício 6.12 - Página 171
#Altere o programa 6.11 de forma a imprimir o menor elemento da lista

'''#Programa 6.11 - Verificação do maior valor

L = [1, 7, 2, 4]
maximo = L[0]
for e in L:
    if e > maximo:
        maximo = e
print(maximo)'''


L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)
