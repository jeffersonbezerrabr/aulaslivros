#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

#Recebe a velocidade do carro do usuário
velocidade = int(input("Você passou no radar a quantos km/h: "))

#Valor cobrado a cada km acima de 80
multa = 5

#Calculo do valor por km acima de 80
valor_multa = (velocidade - 80) * multa

#Comparação e resultado
if velocidade <= 80:
    print("Você não foi multado")
else:
    print(f"Você foi multado em R$ {valor_multa:5.2f}")
