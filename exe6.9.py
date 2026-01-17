#Exercício 6.9 - Página 147

#Modifique o exemplo para pesquisar dois valores.
#em vez de apenas p, leia outro valor v que também será procurado.
#Na impressão, indique qual dos dois valores
#foi achado primeiro.

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))

x = 0
i = 0
while x < len(L):
    if L[x] == p:
        pp = x
        break
    x += 1
    
if x < len(L):
    print(f"{p} foi encontrado na posição {x + 1}")
    
else:
    print(f"{p} não encontrado")
    


while i < len(L):
    if L[i] == v:
        pv = i
        break
    i += 1
    
if i < len(L):
    print(f"{v} foi encontrado na posição {i + 1}")

else:
    print(f"{v} não foi encontrado.")
    
if pp < pv:
    print(f"{p} foi achado primeiro na posição {pp + 1}")

else:
    print(f"{v} foi achado primeiro na posição {pv + 1}")