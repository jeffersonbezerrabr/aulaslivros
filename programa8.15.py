# Programa 8.15: Função soma com número indeterminado de parâmetros - Página 242

def soma(*args):
    s = 0
    for x in args:
        s += x
    return s

print(soma(1,2,3,4,5,6,7,8,9,10))
