# Exercício 8.5 - Página 229

# Reescreva a função do programa 8.1 de forma a utilizar os 
# métodos de pesquisa em lista, vistos no Capítulo 7.

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    
L = [10, 20, 25, 30]

print(pesquise(L, 25))
print(pesquise(L, 27))
