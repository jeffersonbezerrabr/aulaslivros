#Modifique o programa 6.6 usando for. Explique porque
#nem todos os while podem ser transformados em for.

'''#Programa 6.6 - Página 160 - Adição de elementos à lista

L = []
while True:
    n = int(input("Digite um número(0 para sair): "))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1'''
    
L = []
while True:
    n = int(input("Digite um número(0 para sair): "))
    if n == 0:
        break
    L.append(n)
    
for l in L:
    print(l)
    
#Resposta: Para que os valores sejam inseridos em L e encerrado quando
#digitado 0, precisamos de um while com a condição True.