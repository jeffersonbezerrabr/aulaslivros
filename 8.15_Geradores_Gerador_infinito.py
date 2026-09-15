def gerador_de_numeros():
    i = 0
    while True:
        yield i
        i += 1

for x in gerador_de_numeros():
    print(x)
