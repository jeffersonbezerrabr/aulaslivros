#Exercício - 6.21 - Página 199

#Escreva um programa que compare duas listas. 
# Utilizando operações com conjuntos, imprima.

# Os valores comnus às listas
# Os valores que só existem na primeira
# Os valores que existem apenas na segunda
# Uma lista com os elementos não repetidos das duas listas
# A primeira lista sem os elementos repetidos da segunda.

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
B = [3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19]

conjunto_A = set(A)
conjunto_B = set(B)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B

print("Valores comuns às duas listas:", conjunto_A & conjunto_B)
print("Valores que só existem na primeira:", conjunto_A - conjunto_B)
print("Valores que só existem na segunda:", conjunto_B - conjunto_A)

# Conjuntos suportam o operador ^ que realiza a subtração simétrica.
# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
# A ^ B = A - B | B - A

print("Elementos não repetidos nas duas listas:", conjunto_A ^ conjunto_B)

# Repetido:
print("Primeira lista, sem os elementos repetidos na segunda:", conjunto_A - conjunto_B)