# Além de dicionários, listas e geradores, também podemos criar conjuntos(sets) 
# utilizando uma sintaxe similar. A sintaxe é muito parecida com a de dict comprehensions.
# Veja que o valor retornado antes do for não é no formato chave: valor, 
# mas um valor único, como bas list comprehensions.

print({x for x in [9, 2, 1, 3, 6, 9] if x % 3 == 0})

# Veja que percorremos a lista com números e a filtramos, escolhendo no if
# apenas os elementos múltiplos de 3. Lembre-se de que conjuntos não admitem
# elementos repetidos, mas que também não têm uma ordem predefinida, como lista.