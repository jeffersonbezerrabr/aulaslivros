#Faça um programa que percoraa duas listas e gere
#uma terceira sen elementos repetidos.

Lista_01 =[]
Lista_02 = []
Unicos = []

while True:
    n01 = (input("Digite os números da primeira lista(Q para sair): "))
    if n01 == "Q" or n01 == "q":
        break
    Lista_01.append(int(n01))
while True:
    n02 = (input("Digite os números da segunda lista(Q para sair): "))
    if n02 == "Q" or n02 == "q":
        break
    Lista_02.append(int(n02))
    
x = 0

while x < len(Lista_01):
    if Lista_01[x] not in Lista_02 and Lista_01[x] not in Unicos:
        Unicos.append(Lista_01[x])
    x = x + 1

x = 0

while x < len(Lista_02):
    if Lista_02[x] not in Lista_01 and Lista_02[x] not in Unicos:
        Unicos.append(Lista_02[x])
    x = x + 1
        
print(f"Lista 01: {Lista_01}")
print(f"Lista 02: {Lista_02}")
print(f"Lista 03 sem repetir os valores: {Unicos}")

