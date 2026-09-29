# 8.8_desempacotamento_de_parametros - Página 242

"""
Podemos criar funções que recebem um número indeterminado de parâmetros
utilizando listas de parâmetros.
"""

# Programa 8.15: Função soma coim número indeterminado de parâmetros - Página 242

def soma(*args):
    s = 0
    for x in args:
        s += x
    return s

print(soma(1,2))
print(soma(2))
print(soma(5, 6, 7, 8))
print(soma(9, 10, 20, 30, 40))
print(soma())
