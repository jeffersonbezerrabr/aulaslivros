# Exercício - 6.8 - Página 167
# Modifique o primeiro exemplo(Programa 6.9) de forma a reaizar a mesma tarefa, mas sem utilizar a variável achou.
# Dica: observe a consição de saída do while

# L = [15, 7, 27, 39]


# while True:
#     try:
#         p = int(input("Digite o valor a procurar: "))
#         break
    
#     except ValueError:
#         print("Digite um valor númerico")
#         continue

# achou = False

# x = 0

# while x < len(L):
#     if L[x] == p:
#         achou = True
#         break
#     x += 1

# if achou:
#     print(f"{p} encontrado na posição {x}")

# else:
#     print(f"{p} não encontrado")

L = [15, 7, 27, 39]


while True:
    try:
        p = int(input("Digite o valor a procurar: "))
        break
    
    except ValueError:
        print("Digite um valor númerico")
        continue

x = 0

while x < len(L):
    if L[x] == p:
        print(f"{p} encontrado na posição {x}")
        break
    
    x += 1
else:
    print(f"{p} não encontrado")
