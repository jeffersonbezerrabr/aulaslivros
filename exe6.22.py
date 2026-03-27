#Exercício 6.22 - Página 199
# Escreva um programa que compare duas listas.
# Considere a primeira lista como a versão inicial
#e a segunda como a versão após alterações.
#Utilizando operações com conjuntos, seu programa
#deverá imprimir a lista de modificações
#entre essas duas versões, listando:

# Os elementos que não mudaram
# Os novos elementos
# Os elementos que foram removidos

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
B = [3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19]

conjunto_a = set(A)
conjunto_b = set(B)

print("Elementos que não mudaram:", conjunto_a & conjunto_b)
print("Os novos elementos:", conjunto_b - conjunto_a)
print("Elementos que foram removidos:", conjunto_a - conjunto_b)
