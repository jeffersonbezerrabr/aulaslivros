#Exercício 6.10 - Página 167

#Modifique o programa do Ecercício 6.9 de forma a pesquisar
#p e v em toda a lista e informando ao usuário a posição
#onde p e a posição onde v foram encontrados.

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))

x = 0
i = 0

while x < len(L):
    if L[x] == p:
        break
    x += 1
    
if x < len(L):
    print(f"{p} foi encontrado na posição {x + 1}!")
    
else:
    print(f"{p} não foi encontrado!")
    
while i < len(L):
    if L[i] == v:
        break
    i += 1
    
if i < len(L):
    print(f"{v} foi encontrado na posição {i + 1}!")

else:
    print(f"{v} não foi encontrado!")
    
if x < i:
    print(f"{p} foi encontrado primeiro na posição {x + 1}")
else:
    print(f"{v} foi encontrado primeiro na posição {i + 1}")