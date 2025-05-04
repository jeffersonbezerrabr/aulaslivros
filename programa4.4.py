#Programa 4.4: Cálculo da mensalidade de um plano de celular da operadora Tchau

plano = input("Qual é o seu plano de celular? ")

if plano == "falo pouco":
    minutos_no_plano = 100
    extra = 0.20
    preço = 50
    
if plano == "falo muito":
    minutos_no_plano = 500
    extra = 0.15
    preço = 99
    
if plano != "falo pouco" and plano != "falo muito":
    print("Não conheço esse plano")
    
if plano == "falo pouco" or plano == "falo muito":
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"preço do plano R${preço:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento R${suplemento:10.2f}")
    print(f"Total R${preço + suplemento:10.2f}")
