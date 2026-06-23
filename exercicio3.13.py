# Exercício 3.13 - Página 113

# Escreva um programa que converta uma temperatura digitada em Cº em Fº.
# A fórmula para essa conversão é:

"""
F = (9XC) / 5 + 32
"""

while True:
    try:
        temp = float(input("Digite uma temperatura em Cº: "))
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break
convertido = (9 * temp) / 5 + 32

print(F"{temp}º convertido para F é: {convertido}")

