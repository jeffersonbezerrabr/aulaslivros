#Escreva um programa que leia doi números e que pergunte
#qual operação você deseja realizar.
#Você deve poder calcular soma(+), subtração(-), multiplicação(*) e divisão(/).
#Exiba o resultado da operação solicitada.

print("Para usar a calculadora, escolha uma das operações abaixo:")
print()
print("Soma (+)")
print("Subtração (-)")
print("Multiplicação(*)")
print("Divisão(/)")

operação = input("Qual operação deseja realizar? ")
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if operação == "+":
    total = n1 + n2

elif operação == "-":
    total = n1 - n2
    
elif operação == "*":
    total = n1 * n2

elif operação == "/":
    total = n1 / n2
    
print(f"O resultado é: {total:2.0f}")
