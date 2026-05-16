#Exercício DeepSeek - 27-03-2025

#Exercício: Adivinhe o Número (versão iniciante)

import random

numero_secreto = random.randint(1,20)
tentativas = 0

print("Tente adivinhar o número de 1 a 20. Você tem 5 chances.")

while True:
    chute = int(input("Chute um número: "))
    tentativas += 1
    
    if chute < numero_secreto:
        print("Tente um número maior")
        
    elif chute > numero_secreto:
        print("Tente um número menor")
        
    else:
        print(f"Parabéns, você acertou em {tentativas} tentativas")
        break
    
    if tentativas >=5:
        print(f"Fim de jogo! O número era {numero_secreto}")
        break