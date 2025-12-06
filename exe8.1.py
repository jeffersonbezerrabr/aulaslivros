# Exercício 8.1 - Página 225

# Escreva uma função que retorne o maior de dois números.

# Valores esperados:


#maximo(5, 6) == 6 
#maximo(2, 1) == 2 
#maximo(7, 7) == 7

def maximo(a, b):
        if a >= b:
            return a
        else:
            return b
            
print(maximo(5, 6))
print(maximo(2, 1))
print(maximo(7, 7))

