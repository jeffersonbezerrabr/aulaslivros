# Inicializa a tabuada e o número
tabuada = 1

operador = input("O que deseja fazer? (+, -, *, /): ")

if operador == "+":
    while tabuada <= 10:
        numero = 1  # Garantir que o número comece de 1 para cada tabuada
        while numero <= 10:
            print(f"{tabuada} + {numero} = {tabuada + numero}")
            numero += 1
        tabuada += 1  # Avançar para a próxima tabuada

elif operador == "-":
    tabuada = 10
    while tabuada >= 1:
        numero = 1  # Garantir que o número comece de 1 para cada tabuada
        while numero <= 10:
            print(f"{tabuada} - {numero} = {tabuada - numero}")
            numero += 1
        tabuada -= 1  # Avançar para a próxima tabuada

elif operador == "*":
    while tabuada <= 10:
        numero = 1  # Garantir que o número comece de 1 para cada tabuada
        while numero <= 10:
            print(f"{tabuada} * {numero} = {tabuada * numero}")
            numero += 1
        tabuada += 1  # Avançar para a próxima tabuada

elif operador == "/":
    while tabuada <= 10:
        numero = 1  # Garantir que o número comece de 1 para cada tabuada
        while numero <= 10:
            if numero == 0:
                print(f"{tabuada} / {numero} = Divisão por zero não permitida!")
            else:
                print(f"{tabuada} / {numero} = {tabuada / numero:5.4f}")
            numero += 1
        tabuada += 1  # Avançar para a próxima tabuada

else:
    print("Operador inválido! Por favor, escolha entre +, -, *, ou /.")
