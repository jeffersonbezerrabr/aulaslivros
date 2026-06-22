# Exercício 3.9 - Página 113

# Escreva um programa qur leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

while True:
    try:
        h = int(input("Infome as horas: "))
        if h < 0:
            print("Hora precisa ser positivo")
            continue
        m = int(input("Informe os minutos: "))
        if m < 0:
            print("Minutos precisa ser positivo")
            continue
        s = int(input("Informe os segundos: "))
        if s < 0:
            print("Segundos precisa ser positivo")
            continue
        break  
    except ValueError:
        print("Precisa informar valores númericos")
        continue

horas_convertido = h * 3600
minutos_convertido = m * 60

total_em_segundos = horas_convertido + minutos_convertido + s

print(f"{h} horas, {m} minutos e {s} segundos dá um total de {total_em_segundos} segundos")
