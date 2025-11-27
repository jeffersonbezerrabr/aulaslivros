#Faça um programa que leia duas listas e que gere
#uma terceira lista com os elementos das duas primeiras.

Lista_01 = []
Lista_02 = []

while True:
    n_l1 = int(input("Digite os números para a primeira lista(0 para passar para segunda lista): "))
    if n_l1 == 0:
        break
    Lista_01.append(n_l1)
while True:
    n_l2 = int(input("Digite os números da segunda lista(0 para sair): "))
    if n_l2 == 0:
        break
    Lista_02.append(n_l2)
Lista_03 = Lista_01 + Lista_02
print(f"Lista 01: {Lista_01}")
print(f"Lista 02: {Lista_02}")
print(f"Nova lista: {Lista_03}")
