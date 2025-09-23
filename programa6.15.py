#Programa 6.15 - Impressão de uma lista de strings, letra a letra

L = ["Maças", "Peras", "Kiwis"]

for i in L:
    for letra in i:
        print(letra)
        if letra == i[-1]:
            print()
