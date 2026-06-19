# Exercício 3.8 - Página 113

# Escreva um programa que leia um valor em metros e o exiba convertido em milimetros.

try:
    n = float(input("Informe o valor em metros a ser convertido: "))
    if n < 0:
        print("Precisa digitar um valor positivo!")
        exit()

except ValueError:
    print("Precisa digitar um valor númerico")
    exit()
    
convertido = n * 1000

print(f"{n} metro(s) convertido em milimetros: {convertido}")