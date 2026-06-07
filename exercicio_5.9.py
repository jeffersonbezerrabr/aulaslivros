# Exercício 5.9 - Página 141

# Escreva um programa que leia dois números. Imprima a dvisão inteira do primeiro pelo segundo,
# assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado
# Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que
# podemos retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

while True:
    try:
        dividendo = int(input("Dividendo: "))
        if dividendo <= 0:
            print("Valor precisa ser positivo")
            continue
        break
    except ValueError:
        print("Precisa digitar um valor númerico.")

while True:
    try:
        divisor = int(input("Divisor: "))
        if divisor <= 0:
            print("Valor precisa ser positivo")
            continue
        break
    except ValueError:
        print("Precisa digitar um valor númerico.")
        
quociente = 0
x = dividendo

while x >= divisor:
    x -= divisor
    quociente += 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")
