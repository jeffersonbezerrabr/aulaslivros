# Exercício 6.9 - Página 167

# Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, 
# leia outro valor v que também será procurado.
# Na impressão, indique qual dos valores foi achado primeiro.

LISTA = [15, 7, 27, 39]

while True:
    try:
        p = int(input("Digite o valor a ser procurado: "))
        break
    except ValueError:
        print("Digite um valor númerico.")
        continue
    
while True:
    try:
        v = int(input("Digite o valor a ser procurado: "))
        break
    except ValueError:
        print("Digite um valor númerico.")
        continue

for l,c in enumerate(LISTA):
    if c == p:
        print(f"{p} encontrado primeiro na posição {l}")
        break
    if c == v:
        print(f"{v} encontrado primeiro na posição {l}")
        break
else:
    print("Valores não encontrados")
        