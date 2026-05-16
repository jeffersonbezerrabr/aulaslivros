#Exercício: Calculadora com Menu Interativo - 27-03-2025

#Enunciado:
#Crie um programa que funcione como uma calculadora simples com menu. O programa deve:

#    Exibir um menu com 5 opções:

#        1: Adição

#        2: Subtração

#        3: Multiplicação

#        4: Divisão

#        5: Sair

print("""
Menu:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
""")

while True:
    menu = int(input("Digite uma opção: "))
    if menu == 5:
        print("Até logo")
        break
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    if menu == 1:
        total = n1 + n2
        print(f"{n1} + {n2} = {total}")
    elif menu == 2:
        total = n1 - n2
        print(f"{n1} - {n2} = {total}")
    elif menu == 3:
        total = n1 * n2
        print(f"{n1} x {n2} = {total}")
    elif menu == 4:
        total = n1 / n2
        print(f"{n1} / {n2} = {total:0.1f}")
