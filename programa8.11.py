# Programa 8.11: Página 237 
# Função soma com parâmetros obrigatorios e opcionais 

def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s

print(soma(2, 3))

print(soma(3, 4, True))

print(soma(5, 8, False))
