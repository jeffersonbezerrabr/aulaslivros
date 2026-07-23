# Exercício 6.16 - Página 179
# O que acontece quando uma lista já está ordenada? 
# Rastreie o programa 6.20, mas com a lista L = [1, 2, 3, 4, 5]

# Resposta:
# Se a lista já estiver ordenada, nenhum elemento é maior que o elemento seguinte.
# Desta forma, após a primeira verificação de todos os elementos,
# o loop interno é interrompido pela condição de (9).

L = [1, 2, 3, 4, 5]

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


