#6.9 - Usando o for - Página 167

L = [8, 9, 15]
for e in L:
    print(e)
print()    
#Pesquisa usando for

L = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar: "))
for e in L:
    if e == p:
        print("Elemento encontrato!")
        break
else:
    print("Elemento nã oencontrado.")

