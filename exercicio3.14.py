# Exercício 3.14 - Página 114

# Escreva um programa que pergunte a quantidade e Km percorrido por
# um carro alugado pelo usuário, assim como a quantidade de dias 
# pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
# e R$ 0,15 por Km rodado.

while True:
    try:
      km_percorrido = float(input("Quantos Km foram percorridos: "))
      if km_percorrido < 0:
          print("O valor precisa ser maior/igual a zero.")
          continue
    except ValueError:
        print("Valor precisa ser númerico!")
        continue
    break

while True:
    try:
        dias = int(input("Quantos dias ficou com o carro: "))
        if dias < 0:
            print("Valor não pode ser negativo!")
            continue
    except ValueError:
        print("Valor precisa ser númerico!")
        continue
    break

valor_dias = dias * 60
valor_km = km_percorrido * 0.15

total = valor_dias + valor_km

print(f"Valor total a pagar: R$ {total:5.2f}")
