#Programa 6.12 - Cópia de elementos para outras listas - Página 172

valores = [9, 8, 7, 12, 0, 13, 21]
pares = []
impares = []

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"Pares: {pares}\n")
print(f"Impares: {impares}")
