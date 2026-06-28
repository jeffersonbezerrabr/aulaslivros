# Exercćicio 4.2 - Página 121

# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

while True:
    try:
        velocidade = float(input("Informe a velocidade do seu carro: "))
        if velocidade < 0:
            print("Velocidade não pode ser negativa!")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Multa a pagar de R$ {multa:5.2f}")

else:
    print("Não tem multa para pagar")
