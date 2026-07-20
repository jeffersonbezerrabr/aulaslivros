# Programa 6.9: Pesquisa Sequencial

L = [15, 7, 27, 39]


while True:
    try:
        p = int(input("Digite o valor a procurar: "))
        break
    
    except ValueError:
        print("Digite um valor númerico")
        continue

achou = False

x = 0

while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1

if achou:
    print(f"{p} encontrado na posição {x}")

else:
    print(f"{p} não encontrado")