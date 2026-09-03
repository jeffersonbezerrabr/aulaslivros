# Exercício 8.12 - Página 236

# Escreva uma função que receba uma string e uma lista. A função deve comparar
# a string passada com os elementos da lista, também passada como parâmetro.
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

def verificar_string_e_lista(s, lista):
    return s in lista
 
print(verificar_string_e_lista("Python", [1,2,"Python",4,5]))
