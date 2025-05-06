#Exercício 4.8 - Página 126

#Reescreva o programa 4.4 e calcule a conta da operadora Tchau
#usando o else.

plano = input("Qual o seu plano de celular: ")

if plano == "falo pouco":
    franquia = 100
    extra = 0.20
    preço = 50
    
if plano == "falo muito":
    franquia = 500
    extra = 0.15
    preço = 99

if plano != "falo pouco" and plano != "falo muito":
    print("Não conheço esse plano")
    
if plano == "falo pouco" or plano == "falo muito":
    minutos_extra = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do plano: R${preço:5.2f}")
    suplemento = 0
    if minutos_extra > franquia:
        suplemento = extra * (minutos_extra - franquia)
        print(f"Suplemento R${suplemento:10.2f}")
        print(f"Total R${preço + suplemento:10.2f}")
else:
    print("Você vai pagar:")
    print(f"Preço do plano: R${preço:5.2f}")
    
    