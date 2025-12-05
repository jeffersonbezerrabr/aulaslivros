#Exercício 6.8 - Página 167

#Modifique o primeiro exemplo(Programa 6.9) de forma a realizar
#a mesma tarefa, mas sem utilizar a variável "achou".
#Dica: Observe a condição de saída do while.

'''L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = False
x = 0

while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f"{p} achado na posição {x + 1}")
else:
    print(f"{p} não encontrado")'''
    
L = [15, 7, 27, 39]

p = int(input("Digite o valor a procurar: "))
x = 0

while x < len(L):
    if L[x] == p:
        break
    x += 1

if x < len(L):
    print(f"{p} achado na posição {x + 1}")

else:
    print(f"{p} não encontrado.")