# Programa 8.23: Jogo do alienígina

import random

TENTATIVAS = 0

arvore = random.randint(1,100)

print("Um alienígina está escondido atrás de uma árvore")
print("Cada árvore foi númerada de 1 a 100.")
print("Você tem 3 tentativas para advinhar em que árvore")
print("o alienígina se esconde.")

while TENTATIVAS < 3:
    try:
        palpite = int(input(f"Qual árvore o alienígina está? Tentativa: {TENTATIVAS + 1}: "))
        if palpite < 1 or palpite > 100:
            print("Você precisa informar entre 1 e 100!")
        else:
            if palpite == arvore:
                print(f"Você acertou na {TENTATIVAS + 1}ª tentativa!")
                break
            elif palpite > arvore:
                print("Muito alto")
                TENTATIVAS += 1
            else:
                print("Muito baixo")
                TENTATIVAS +=1
    except ValueError:
        print("Precisa digitar umn número inteiro.")
else:
    print("Você não conseguiu acertar.")
    print(f"O alienígina estava na árvore {arvore}")

    