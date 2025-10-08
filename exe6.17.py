#Exercício 6.17 - Página 179

#O que acontece quando dois valores são iguais?
#Rastreie o programa 6.20, mas com a lista L = [3, 3, 1, 5, 4]

#Programa 6.20

'''L = [7, 4, 3, 12, 8]
fim = 5 # Usamos a variável fim para marcar a qntd de elementos da lista.
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)'''
    
L = [3, 3, 1, 5, 4]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)
    
# Como utilizamos o método de bolhas, na primeira verificação, 3, 3 são 
# considerados como na ordem correta.
# Quanto verificamos o segundo 3 com 1, ocorre uma troca.
# O mesmo vai ocorrer com o primeiro 3, mas apenas na próxima repetição.
# Veja que o 1 subiu para a primeira posição
# como uma bolha de ar dentro d'água.