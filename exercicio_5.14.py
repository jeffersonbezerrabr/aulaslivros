# Exercício 5.14 - Página 145

# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, 
# assim como a soma e a média aritimética.


x = 0
total = 0


while True:
    try:
        n = int(input("Digite um número a ser somado, 0(zero) para sair: "))
        if n == 0:
            break
        total += n
        x += 1
    except ValueError:
        print("Precisa digitar um número inteiro!")

media = total / x
        
print(f"\nQuantidade de números digitados: {x}")
print(f"Total somado: {total}")
print(f"Média: {media:.2f}")
        