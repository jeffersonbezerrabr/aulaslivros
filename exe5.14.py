#Exercício 5.14 - Página 145

#Escreva um programa que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero).
#No final da execução, exiba a quantidade de números digitados,
#assim como a soma e a média aritimética.

x = 0
soma = 0

while True:
    n = int(input("Digite um número inteiro. Quando quiser encerrar, digite 0(zero): "))
    if n == 0:
        break
    soma += n
    x += 1
print(f"Quantidade de números digitados foi {x}")
print(f"a soma dos valores é: {soma}")
print(f"A média é {soma / x:5.2f}")
   

    