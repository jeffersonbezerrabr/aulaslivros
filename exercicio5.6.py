# Altere o programa anterior para exibir os resultados no mesmo
# formato de uma tabuada de multiplicação: 2 x 1 = 2, 2 x 2 = 4

x = 1
while True:
    try:
        n = int(input("Tabuada de multiplicar de: "))
        if n < 1:
            print("Valor precisa ser positivo!")
            continue
        break
    except ValueError:
        print("Precisa digitar um valor númerico")

while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x += 1
