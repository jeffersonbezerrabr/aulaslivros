# 8.14_list_comprehensions - Página 260 e 261

L = [x for x in range(10)]

print(L)

# Podemos também usar list comprehensions com outras listas:

Z = [x * 2 for x in [0, 1, 2, 3]]

print(Z)

# Podemos usar list comprehensions para criar listas mais complexas, 
# por exemplo, nas quais cada elemento é uma tupla.

Y = [(x, x * 2) for x in [1, 2, 3]]

print(Y)
