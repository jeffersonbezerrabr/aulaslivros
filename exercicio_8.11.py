# Exercício 8.11 - Página 236

# Escreva uma função para validar uma variável string. Essa função
# recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e
# mínimo, e falso, caso contrário.

def validar_string(texto, minimo, maximo):
    while True:
        t = input(texto)
        if len(t) < minimo or len(t) > maximo:
            return False
        else:
            return True
            
print(validar_string("Digite um texto entre 0 e 10 caracteres: ", 0, 10))

# também pode ser feito assim:

def validar_string2(texto, minimo, maximo):
    while True:
        if len(texto) < minimo or len(texto) > maximo:
            return False
        else:
            return True
            
print(validar_string2("bola", 0, 10))
