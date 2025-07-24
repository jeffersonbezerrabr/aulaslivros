#Faça um programa que percora duas listas e gere
#uma terceira sen elementos repetidos.

L01 = []
L02 = []
L03 = []

while True:
    n01 = input("Digite os elementos da lista 01(S para sair): ")
    if n01.upper() == "S":
        break
    L01.append(int(n01))
    
while True:
    n02 = input("Digite os elementos da lista 02(S para sair): ")
    if n02.upper() == "S":
        break
    L02.append(int(n02))

x = 0
    
while x < len(L01):
    if L01[x] not in L02 and L01[x] not in L03:
        L03.append(L01[x])
    x += 1
    
x = 0

while x < len(L02):
    if L02[x] not in L01 and L02[x] not in L03:
        L03.append(L02[x])
    x += 1
        

print(f"\nElementos da lista 01: {L01}")
print(f"\nElementos da lista 02: {L02}")
print(f"\nElementos que não se repetem entre as listas 01 e 02:")
print(L03)
