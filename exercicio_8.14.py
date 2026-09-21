# Exercício 8.14: Página 253
# Altere o programa 8.22 de forma que o usuário tenha três chances de acertar o número.
# O programa termina se o usuário acertar ou errar três vezes.

from random import randint

def sorteio():
    n = randint(1,10)
    tentativas = 3
    while tentativas > 0:
        try:
            x = int(input(f"Informe um número de 1 até 10. Você tem {tentativas} tentativas: "))
            if x < 0 or x > 10:
                print("O número precisa estar entre 1 e 10!")
            else:
                if x == n:
                    print("Parabéns, você acertou!")
                    break
                else:
                    if tentativas > 1:
                        tentativas -= 1
                        print(f"Você errou! Restam {tentativas} tentativas!")
                    else:
                        tentativas -= 1
                        print("Fim do jogo! Você perdeu.")
        except ValueError:
            print(f"Precisa digitar um número inteiro")
                    
sorteio()