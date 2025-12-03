#Faça um programa que percora duas listas e gere
#uma terceira sen elementos repetidos.

l01 = []
l02 = []
x = y = 1

while True:
    n1 = input(f"Digite os elementos da LISTA 01 ou [P] para pular para segunda lista:\n{x}º: ").lower()
    if n1 == "p":
        break
    elif n1.isdigit():
        n1_int = int(n1)
        l01.append(n1_int)
        x +=1
    else:
        print("Você precisa digitar um valor inteiro ou [P] para segunda lista.\n")


while True:
    n2 = input(f"Digite os elementos da LISTA 02 ou [P] para parar:\n{y}º: ").lower()
    if n2 == "p":
        break
    elif n2.isdigit():
        n2_int = int(n2)
        l02.append(n2_int)
        y += 1
    else:
        print("Você precisa digitar um valor inteiro ou [P] para parar.\n")


s1 = set(l01)
s2 = set(l02)

l03 = s1 ^ s2



print(f"Elementos da LISTA 01: {l01}\n")
print(f"Elementos da LISTA 02: {l02}\n")
print(f"Elementos que não se repetem entre as LISTAS 01 e 02: {list(l03)}")
    