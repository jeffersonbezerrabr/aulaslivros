# Programa 8.1: Pesquise em uma lista - Página 226

def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return f"{e} está na posição {x}"
    return None

L = [10, 20, 25, 30]

print(pesquise(L, 25))
print(pesquise(L, 27))

def soma(L):
    total = 0
    for c in L:
        total += c
    return total

def media(L):
    return soma(L) / len(L)

print(soma(L))
print(media(L))
