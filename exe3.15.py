# Exercício da página 114

print("Expectativa de vida de um fumante")
print()

#Pergunta ao usuário quantos cigarros e há quanto tempo fuma
cigarros = int(input("Quantos cigarros você fuma por dia? "))
print()
tempo_fumando = int(input("Há quantos anos você fuma? "))

#Calcula o valor total de cigarros fumados
total_cigarros = cigarros * tempo_fumando * 365

#Calcula o valor total de minutos perdidos
minutos_perdidos = total_cigarros * 10

#Converte os minutos em dias
tempo_dias = minutos_perdidos / 1440

#Exibe o resultado
print(f"Você perderá aproximadamente {tempo_dias:.2f} dias de vida!")
