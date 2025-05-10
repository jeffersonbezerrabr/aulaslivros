#Programa 4.10: Planos da tchau com elif

valido = True

plano = input("Qual é o seu plano de celular: ")

if plano == "falo pouco":
    minutos_no_plano = 100
    extra = 0.20
    preço = 50

elif plano == "falo muito" :
    minutos_no_plano = 500
    extra = 0.15
    preço = 99

else:
    valido = False

if not valido:
    print(f"Erro: Não conheço esse plano {plano}")

else:
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"preço do plano: R$:{preço:10.2f}")
    suplemento = 0
    
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    
    print(f"suplemento R${suplemento:10.2f}")
    print(f"Total R${preço + suplemento:10.2f}")
