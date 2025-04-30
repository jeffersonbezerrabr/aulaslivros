#Exercício 4.3 - Página 123

#Escreva um programa que pergunte ao usuário 3 números e que imprima o maior e o menor

#Recebe o primeiro número do usuário
numero_1 = int(input("Digite um número: "))

#Recebe o segundo número do usuário
numero_2 = int(input("Digite o segundo número: "))

#Recebe o terceiro número do usuário
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"Maior {numero_1}")

if numero_2 > numero_1 and numero_2 > numero_3:
    print(f"Maior {numero_2}")

if numero_3 > numero_1 and numero_3 > numero_2:
    print(f"Maior {numero_3}")

if numero_1 < numero_2 and numero_1 < numero_3:
    print(f"Menor {numero_1}")

if numero_2 < numero_1 and numero_2 < numero_3:
    print(f"Menor {numero_2}")

if numero_3 < numero_1 and numero_3 < numero_2:
    print(f"Menor {numero_3}")
    