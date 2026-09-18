# Exercício 8.14 - Página 253

# Altere o programa 8.22 de forma que o usuário tenha três chances de acertar o número.
# O programa termina se o usuário acertar ou errar três vezes.

import random

n = random.randint(1, 10)
tentativas =3
for c in range(3):
    try:
        q = int(input("Digite um número entre 1 e 10: "))
        
        if n == q:
            print("Você acertou!")
            break
        
        if tentativas == 0:
            print("Acabaram as tentativas!")
            break
        
        elif n != q:
            tentativas -=1
            if tentativas > 0:
                print("Você errou")
                print(f"Você tem {tentativas} tentativas")
            else:
                print("Você perdeu!")
                print("Tentativas esgotadas!")
                print("Boa sorte na proxima!")
                  
    except ValueError:
        print("Digite um número inteiro")