# Programa8.14: Configuração de funções com funções - Página 241

def imprime_lista(L, fimpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def imprime_elemento(e):
    print(f"valor: {e}")
    
def par(x):
    return x % 2 == 0

def impar(x):
    return not par(x)

L = [1, 7, 9, 2, 11, 0]

imprime_lista(L,imprime_elemento, par)
imprime_lista(L,imprime_elemento, impar)
