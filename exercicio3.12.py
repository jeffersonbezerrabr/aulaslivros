# Exercício 3.12 - Página 113

# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

while True:
    try:
        distancia = float(input("Informe a distância da viagem: "))
        if distancia <= 0:
            print("Distancia precisa ser maior que zero!")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

while True:
    try:
        velocidade = int(input("Informe a velocidade média: "))
        if velocidade <= 0:
            print("Velocidade precisa ser maior que 0!")
            continue
    except ValueError:
        print("Precisa informar um valor númerico!")
        continue
    break


tempo = distancia / velocidade

horas = int(tempo)
minutos = int((tempo - horas) * 60)

print("A viagem terá uma duração média de ", end="")

if horas > 0:
    print(f"{horas} horas", end="")
    if minutos > 0:
        print(f" e {minutos} minutos")
    else:
        print()
else:
    print(f"{minutos} minutos")
