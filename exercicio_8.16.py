# Exercício 08-16 - Página 256

"""Modifique o jogo do alienígena (Programa 8.23). 
Crie uma variável que represente a vida do jogador, começando com 100. 
A partida termina quando você encontrar o alienígena ou quando a vida acabar (<=0). 
A cada erro, diminua a vida por um valor aleatório entre 5 e 20, representando um ataque do alienígena. 
Você pode retirar a parte do jogo que limita o número de tentativas e deixar apenas a vida 
do jogador ou do alienígena decidirem quando a partida termina. Exiba a vida do jogador antes de perguntar a próxima árvore."""

import random

VIDA_JOGADOR = 100
arvore = random.randint(1,100)

print("Um alienígina está escondido atrás de uma árvore")
print("Cada árvore foi númerada de 1 a 100.")
print("Você começa com 100 de vida.")
print("A cada erro, você leva um dano do alienígena que varia entre 5 e 20")
print("Você precisa descobrir onde o alienígina se esconde")
print("Antes que sua vida chegue a 0.")

while VIDA_JOGADOR >= 0:
    valor_dano = random.randint(5,20)
    try:
        palpite = int(input(f"Qual árvore o alienígina está? Vida Atual: {VIDA_JOGADOR}: "))
        if palpite < 1 or palpite > 100:
            print("O valor informado precisa estar entre 1 e 100")
        else:
            if palpite == arvore:
                print(f"Você acertou! Veja quanto estava de vida: {VIDA_JOGADOR}")
                break
            
            elif palpite > arvore:
                print(f"Muito alto! - {valor_dano} de vida")
                VIDA_JOGADOR -= valor_dano
            
            else:
                print(f"Muito baixo! - {valor_dano} de vida")
                VIDA_JOGADOR -= valor_dano
    except ValueError:
        print("Precisa digitar um valor inteiro!")
else:
    print(f"Sua vida chegou a 0 =(")
    print("Você perdeu!")
