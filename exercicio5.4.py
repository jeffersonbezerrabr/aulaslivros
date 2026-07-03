# Modifique o programa anterior para imprimir de 1 até o 
# número digitado pelo usuário, mas, dessa vez, apenas os números impares.

x = 0

while True:
    try:
        fim = int(input("Digite o último número a imprimir: "))
        if fim < 0:
            print("Precisa digitar um valor maior que zero!")
            continue
        break
    except ValueError:
        print("Precisa digitar um valor númerico positivo")
        continue
    
while x <= fim:
    if x % 2 == 1:
        print(x)
    x += 1