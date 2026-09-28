# 8.6 Funções com parâmetro

"""
Um poderoso recurso do Python é permitir a passagem de funções como parâmetro.
Isso permite combinar várias funções para realizar uma tarefa.
Vejamos um exemplo.
"""

# Programa 8.13: Funções como parâmetro - Página 240

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def imprime(a, b, foper):
    print(foper(a, b))
    
imprime(3, 4, soma)
imprime(10, 1, subtracao)
