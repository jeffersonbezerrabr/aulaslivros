"""Exercício 06-21: - Página 199

Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• os valores comuns às duas listas
• os valores que só existem na primeira
• os valores que existem apenas na segunda
• uma lista com os elementos não repetidos das duas listas.
• a primeira lista sem os elementos repetidos na segunda"""

L1 = [1,2,3,4,5,6,7,8,9,10]

L2 = [1,2,3,5,7,8,9,12]

print(f"Os valores comuns às duas listas: {set(L1) & set(L2)}\n")

print(f"Os valores que só existem na primeira: {set(L1) - set(L2)}\n")

print(f"Os valores que existem apenas na segunda: {set(L2) - set(L1)}\n")

print(f"Uma lista com os elementos não repetidos das duas listas: {set(L1) ^ set(L2)}\n")

print(f"A primeira lista sem os elementos repetidos na segunda: {set(L1) - set(L2)}")
