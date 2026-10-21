print(list(filter(lambda a: a % 2 == 0, [5, 6, 9, 2, 10])))

# Assim como map e reduce, filter pode ser escrita de forma mais legível com comprehensions:

print([a for a in [5, 6, 9, 2, 10] if a % 2 == 0])