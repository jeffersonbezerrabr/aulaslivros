# Exercício 8.1 - Página 225

# Escreva uma função que retone o maior de dois números.

"""
Valores esperados:
maximo(5, 6) == 6
maximo(2, 1) == 2
maximo(7, 7) == 7
"""

def maximo(a, b):
    return(max(a,b))

# print(maximo(5, 6))
# print(maximo(2, 1))
# print(maximo(7, 7))

def maximo2(a, b):
    if a >= b:
        return a
    return b

print(maximo2(10,11))
print(maximo2(12,11))
