# Exercício 8.14 - Página 253

# Altere o programa 8.22 de forma que o usuário tenha três chances de acertar o número.
# O programa termina se o usuário acertar ou errar três vezes.

import random

ACERTOU = False

n = random.randint(1, 10)
tentativas = 3

while ACERTOU == False:
    try:
        
        q = int(input(f"Digite um número entre 1 e 10: "))
    
        if  n != q:
            print("Você errou")
            tentativas -= 1
            if tentativas > 0:
                print(f"Você ainda tem {tentativas} tentativas\n")
    
        if n == q:
            ACERTOU = True
            tentativas -= 1
            print("Você acertou!\n")
            
    
        elif tentativas == 0:
            print("Tentativas esgotaram.")
            print("Mais sorte na proxima vez")
            break
                 
    except ValueError:
        print("Digite um número inteiro")
            

            
