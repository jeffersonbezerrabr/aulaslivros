#Faça um programa que leia duas listas e que gere
#uma terceira lista com os elementos das duas primeiras.

L01 = []
L02 = []

while True:
    n1 = input("Digite valores para a primeira lista(S para passar para a segunda lista): ")
    if n1 == "s" or n1 == "S":
        break
    L01.append(int(n1))
    
while True:
    n2 = input("Digite os valores para a segunda lista(S para sair): ")
    if n2 == "S" or n2 == "s":
        break
    L02.append(int(n2))


L03 = L01 + L02
print(f"a união dos elementos da lista 1 e da lista 2 é {L03}")