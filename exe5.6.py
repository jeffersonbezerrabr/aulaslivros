#Exercício 5.6 - Página 141

#Altere o programa anterior para exibir os resultados no mesmo formato
#de uma tabuada de multiplicação 2x1 = 2, 2x2 = 4,...

#Exercício anterior:

#n = int(input("Tabuada de: "))
#x = 1
#while x <= 10:
#    print(f"{n} + {x} = {n + x}")
#    x = x + 1

#Altere o programa anterior para exibir os resultados no mesmo formato
#de uma tabuada de multiplicação 2x1 = 2, 2x2 = 4,...
    
n = int(input("Tabuada de multiplicação de: "))
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x * 1 + 1
    