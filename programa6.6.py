#Programa 6.6 - Página 160 - Adição de elementos à lista

L = []
while True:
    n = int(input("Digite um número(0 para sair): "))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1
    