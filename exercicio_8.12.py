# Exercício 8.12 - Página 236

# Escreva uma função que receba uma string e uma lista.
# A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

def comparar(texto, lista):
    return texto in lista

L = ["AA", "AB", "AC", "AD"]
    
print(comparar("AA", L))
print(comparar("BB", L))
print(comparar("CC", L))
print(comparar("DD", L))
print(comparar("AD", L))
