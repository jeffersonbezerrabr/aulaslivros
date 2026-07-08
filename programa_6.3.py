# Programa 6.3: Apresentação de números - Página 155

numeros = []

x = 0

while x < 5:
    numeros.append(int(input(f"Número {x + 1}: ")))
    x += 1
    
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    elif escolhido >= len(numeros):
        print("Precisa escolher de 1 a 5")
        continue
    elif escolhido < 0:
        print("Precisa escolher de 1 a 5")
        continue
    print(f"Você escolheu o número {numeros[escolhido - 1]}")
    
