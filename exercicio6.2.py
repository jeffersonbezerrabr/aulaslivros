# Exercício 6.2 - Página 161: Faça um programa que leia duas listas
# e gere uma terceira com os elementos das duas primeiras.

l01 = []
l02 = []

while True:
    n = input("Digite um valor para a primeira lista (0 para sair): ").strip()
    if n == "":
        print("Precisa digitar algo")
        continue
    try:
        f_n = float(n)
        if f_n == 0:
            break
        elif "." not in n:
            l01.append(int(n))
            print("Adicionado int com sucesso na lista 01")
        else:
            l01.append(float(n))
            print("Adicionado float com sucesso na lista 01")
    except ValueError:
        l01.append(n)
        print("Adicionado string com sucesso na lista 01")

while True:
    n2 = input("Digite um valor para a segunda lista (0 para sair): ").strip()
    if n2 == "":
        print("Precisa digitar algo!")
        continue
    try:
        f_n2 = float(n2)
        if f_n2 == 0:
            break
        
        elif "." not in n2:
            l02.append(int(n2))
            print("Adicionado int com sucesso na lista 02")
            
        else:
            l02.append(float(n2))
            print("Adicionado float com sucesso na lista 02")
            
    except ValueError:
        l02.append(n2)
        print("Adicionado string com sucesso na lista 02")
            
        
l03 = l01 + l02

print("Terceira lista gerada com os elementos das listas 01 e 02\n")

print(l03)            

