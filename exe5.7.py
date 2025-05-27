#Exercício 5.7 - Página 141

#Modifique o programa anterior de forma que o usuário também
#digite o inicio e o fim da tabuada, em vez de começar com 1 e 10.

#Programa anterior:

'''n = int(input("Tabuada de multiplicação de: "))
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x * 1 + 1'''

n = int(input("Tabuada de multiplicação de: "))
n2 = int(input("Deseja multiplicar até quanto? "))

x = 1
while x <= n2:
    print(f"{n} x {x} = {n * x}")
    x = x * 1 + 1
    