# Exercício 8.11 - Página 236

"""
Escreva um função para validar uma variável string. 
Essa função recebe como parâmetros a string, o minimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string estiver entre os valores de maximo
e minimo, e falso caso contrário.
"""

def validar_string(s, min, max):
    tamanho = len(s)
    return tamanho >= min and tamanho <= max
    
print(validar_string("python",0,10))
print(validar_string("", 1, 5))
print(validar_string("ABC", 2, 5))
print(validar_string("ABCEFG", 3, 5))
print(validar_string("ABCEFG", 1, 10))
