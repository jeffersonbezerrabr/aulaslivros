# Programa 8.22: Adivinhando o número - Página 253

from random import randint

def sorteio():
    n = randint(1, 10)
    while True:
        try:
            x = int(input("Escolha um número entre 1 e 10: "))
            if x < 1 or x > 10:
                print("precisa digitar entre 1 e 10!")
            else:
                if x == n:
                    print("Parabens, você acertou!")
                    break
                else:
                    print("Você errou! Tente novamente.")
        except ValueError:
            print(f"Precisa digitar um valor inteiro!")
            
sorteio()