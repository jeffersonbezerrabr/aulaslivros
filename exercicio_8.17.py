# Exercício 08-17 - Página 256

"""Melhore o programa do exercício anterior perguntando ao jogador o nível de dificuldade desejado. 
No modo fácil, a vida começa com 100 e o alienígena pode causar entre 5 e 20 de dano, como anteriormente. 
No modo médio, a vida começa com 80 e o alienígena pode causar danos entre 10 e 25. 
Já no modo difícil, a vida começa com 75 e o alienígena causa danos entre 20 e 30. 
Adicione mensagens e caracteres para deixar o jogo mais divertido."""

import random

print("🎮 Bem-vindo ao Caça Alienígenas! 👽")
print("\nEscolha o nível de dificuldade:")
print("1 - Fácil   (❤️  100 HP | 💥 Dano: 5-20)")
print("2 - Médio   (❤️   80 HP | 💥 Dano: 10-25)")
print("3 - Difícil (❤️   75 HP | 💥 Dano: 20-30)")

while True:
    try:
        nivel = int(input("\nDigite o número do nível (1-3): "))
        if nivel in [1, 2, 3]:
            break
        print("❌ Opção inválida! Escolha 1, 2 ou 3.")
    except ValueError:
        print("Precisa digitar um valor inteiro!")
        
if nivel == 1:
    vida_jogador = 100
    dano_min, dano_max = 5, 20
    
elif nivel == 2:
    vida_jogador = 80
    dano_min, dano_max = 10, 25

else:
    vida_jogador = 75
    dano_min, dano_max = 20, 30
    
arvore = random.randint(1, 100)
print("\n🌳 Um alienígena está escondido atrás de uma árvore!")
print("🔢 Cada árvore foi numerada de 1 a 100.")
print("❗ Você tem que adivinhar em que árvore o alienígena se esconde.")
print("⚠️  Cuidado! O alienígena vai te atacar a cada tentativa errada!\n")

while vida_jogador > 0:
    print(f"❤️  Pontos de vida: {vida_jogador}")
    try:
        palpite = int(input("🎯 Escolha uma árvore [1-100]: "))
        if palpite < 1 or palpite > 100:
            print("Precisa digitar entre 1 e 100")
            
        elif palpite == arvore:
            print("\n🎉 PARABÉNS! Você acertou! O alienígena foi encontrado! 🎊")
            break
        
        elif palpite > arvore:
            print("⬇️  Muito alto! Tente um número menor.")
            
        else:
            print("⬆️  Muito baixo! Tente um número maior.")
        
        dano = random.randint(dano_min, dano_max)
        vida_jogador -= dano
        print(f"💥 O alienígena te atacou! Dano: {dano}\n")
    
    except ValueError:
        print("Precisa digitar um valor inteiro.")

else:
    print("\n💀 Game Over! Você não conseguiu sobreviver.")
    print(f"👽 O alienígena estava na árvore {arvore}.")
