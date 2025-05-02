#Exercício 4.6 - Página 126

#Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km
#Por viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia = int(input("Qual a distância da viagem em km? "))

if distancia <= 200:
    valor_km = distancia * 0.50
    print(f"Para uma corrida de {distancia} km, o valor é R${valor_km:5.2f}")

else:
    valor_km = distancia * 0.45
    print(f"Para uma corrida de {distancia} km, o valor é R${valor_km:5.2f}")
    