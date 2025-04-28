#Exercicio da página 113

print("Conversor de tempo em segundos")

dias = int(input("Informe os dias: "))
horas = int(input("Informe as horas: "))
segundos = int(input("Informe os segundos: "))
dias_segundos = dias * 86400
horas_segundos = horas * 3600
total = dias_segundos + horas_segundos + segundos
print(f"A conversão de: {dias} dias, {horas} horas e {segundos} segundos em segundos, é igual a {total} segundos")
