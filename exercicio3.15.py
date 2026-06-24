# Exercício 3.15 - Página 114

# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, 
# e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

while True:
    try:
        cigarros_por_dia = int(input("Quantos cigarros você fuma por dia: "))
        if cigarros_por_dia < 0:
            print("Valor não pode ser negativo!")
            continue
    except ValueError:
        print("Valor precisa ser númerico!")
        continue
    break

while True:
    try:
        anos_fumando = float(input("Quantos anos que você já fuma: "))
        if anos_fumando < 0:
            print("Valor não pode ser negativo!")
            continue
    except ValueError:
        print("Valor precisa ser númerico!")
        continue
    break

redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10

redução_em_dias = redução_em_minutos / (24 * 60)
print(f"Redução do tempo de vida {redução_em_dias:8.2f} dias.")
