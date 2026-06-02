# Exercício 5.7 - Página 141

# Modifique o programa anterior de forma que o usuário também 
# digite o inicio e o fim da tabuada, em vez de começar com 1 e 10.

while True:
    try:
        valor = int(input("Deseja ver a tabuada de quanto: "))
        if valor < 1:
            print("Valor informado precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Valor precisa ser númerico e positivo!")

while True:
    try:
        n1 = int(input("A tabuada vai iniciar em: "))
        if n1 < 1:
            print("Valor informado precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Valor precisa ser númerico e positivo!")
        
while True:
    try:
        n2 = int(input("A tabuada vai iniciar em: "))
        if n2 < 1:
            print("Valor informado precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Valor precisa ser númerico e positivo!")

x = n1

while x <= n2:
    print(f"{valor} x {x} = {valor * x}")
    x += 1