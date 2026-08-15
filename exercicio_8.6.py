# Exercício 8.6 - Página 229

# Reescreva o programa 8.2 de forma a utilizar for em vez de while.

"""
def soma(L):
    total = 0
    x = 0
    while x < 5:
        total += L[x]
        x += 1
    return total

L = [1, 7, 2, 9, 15]
"""

def soma(L):
    total = 0
    for c in L:
        total += c
    return total

L = [1, 7, 2, 9, 15]

print(soma(L))
