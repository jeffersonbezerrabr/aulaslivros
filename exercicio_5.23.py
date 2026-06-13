# Exercicio 5.23 - Página 148

# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

while True:
    try:
        numero = int(input("Digite um número: "))

        if numero <= 1:
            print("0 e 1 não são primos")
            break

        if numero == 2:
            print("2 é primo")
            break

        if numero % 2 == 0:
            print(f"{numero} não é primo")
            break

        primo = True

        for c in range(3, numero, 2):
            if numero % c == 0:
                primo = False
                break

        if primo:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo")

        break

    except ValueError:
        print("Digite um número inteiro!")