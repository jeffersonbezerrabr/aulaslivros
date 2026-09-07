# Programa 8.11: Função seoma com parâmetros obrigatorios e opcionais - Página 237

# Os parametros opcionais eles devem sempre vir no final

def soma(a, b, imprime = False):
    s = a + b
    if imprime:
        print(s)
    return s

soma(2, 3)

soma(3, 4, True)

soma(5, 8, False)

soma(5, 8, True)

# Se vierem no inicio, cria-se uma definição inválida

# def soma2 (imprime=True, a, b):
#     s = a + b
#     if imprime:
#         print(s)
#     return s

# soma2(True, 2, 3)