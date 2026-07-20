# Altere o programa 6.11 de formaa a imprimir o menor elemento da lista

# Programa 6.11: Verificação de maior valor

# L = [1, 7, 2, 4]
# maxixo = L[0]
# for e in L:
#     if e > maxixo:
#         maxixo = e
# print(maxixo)

L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)
