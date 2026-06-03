# Programa 4.7 - Conta de telefone com três faixas de preço - Página 126

minutos = int(input("Quantos minutos você utilizou esse mês: "))

if minutos < 200:
    preco = 0.20

elif minutos < 400:
    preco = 0.18
    
else:
    preco = 0.15

print(f"Você vai pagar este mês: R$ {minutos * preco:6.2f}")