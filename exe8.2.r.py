# Exercício 8.2 - Página 225

# Escreva uma função que receba dois números e retorne 
# True se o primeiro número for multiplo do segundo.

# Valores esperados:

# multiplo(8, 4) == True
# multiplo(7, 3) == True
# multiplo(5, 5) == True

def multiplo(a, b):
    return a % b == 0
        
print(multiplo(8, 4))
print(multiplo(7, 3))
print(multiplo(5, 5))
