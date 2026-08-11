# 8.7_empacotamento_e_desempacotamento_de_parametros - Página 241

"""
Outra flexibilidade da linguagem Python é passar parâmetros empacotados em uma lista.
Vejamos um exemplo:
"""

# def soma(a,b):
#     print(a + b)
    
# L = [2, 1]

# soma(*L)

def barra(n=10, c="*"):
    print(c * n)
    
L = [[5, "-"], [10, "*"], [5], [6, ","]]

for e in L:
    barra(*e)