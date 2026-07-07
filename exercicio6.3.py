# Faça um programa que percorra duas listas e gere
# uma terceira sem elementos repetidos

l01 = []
l02 = []

while True:
    n = input("Informe os elementos da primeira lista (0 para sair): ").strip()
    if n == "":
        print("Precisa digitar algo")
        
    try:
        f_n =float(n)
        if f_n == 0:
            break
        elif "." in n:
            l01.append(float(n))
            print("float adicionado a lista 01")
        else:
            l01.append(int(n))
            print("int adicionado a lista 01")
    except ValueError:
        l01.append(n)
        print("string adicionado a lista 01")
        
while True:
    n2 = input("Informe os elementos da primeira lista (0 para sair): ").strip()
    if n2 == "":
        print("Precisa digitar algo")
        
    try:
        f_n2 =float(n2)
        if f_n2 == 0:
            break
        elif "." in n2:
            l02.append(float(n2))
            print("float adicionado a lista 02")
        else:
            l02.append(int(n2))
            print("int adicionado a lista 02")
    except ValueError:
        l02.append(n2)
        print("string adicionado a lista 02")
        
l03 = []

for c in l01:
    if c not in l02:
        l03.append(c)
for d in l02:
    if d not in l03:
        l03.append(d)
        
print(l03)