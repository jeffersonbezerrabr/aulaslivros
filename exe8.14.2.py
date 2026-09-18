# Exercício 8.14 - Página 253

# Altere o programa 8.22 de forma que o usuário tenha três chances de acertar o número.
# O programa termina se o usuário acertar ou errar três vezes.

import random

v = random.randint(1, 10)
tentativas = 3
while tentativas != 0:
    try:
        q = int(input("Digite um número entre 1 e 10: "))
        
        if q == v:
            print("Você acertou. Parabéns!")
            exit()
        
        else:
            tentativas -= 1
            if tentativas > 0:
                print("Você errou")
                print(f"Restam {tentativas} Tentativas")
            
    except ValueError:
        print("Digite um número inteiro")

print("\nTentativas esgotadas")
print("\nVocê perdeu!")
print("\nMais sorte na proxima vez!")
