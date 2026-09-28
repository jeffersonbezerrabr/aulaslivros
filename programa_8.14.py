# 8.6 Funções com parâmetro

"""
Um poderoso recurso do Python é permitir a passagem de funções como parâmetro.
Isso permite combinar várias funções para realizar uma tarefa.
Vejamos um exemplo.
"""

# Programa 8.14: Configuração de funções com funções

def imprime_lista(L, fimpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def imprime_elemento(e):
    print(f"Valor: {e}")
    
def eh_par(x):
    return x % 2 == 0

def eh_impar(x):
    return not eh_par(x)

L = [1, 7, 9, 2, 11, 0]

imprime_lista(L, imprime_elemento, eh_par)
#imprime_lista(L, imprime_elemento, eh_impar)
