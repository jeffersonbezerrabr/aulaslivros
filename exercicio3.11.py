# Exercício 3.11 - Página 113

# Faça um programa que solicite o preço de uma mercadoria e o percentual
# de desconto. Exiba o valor do descanso e o preço a pagar.

while True:
    try:
        valor = (float(input("Informe o valor do produto: ")))
        if valor <= 0:
            print("Valor precisa ser maior que 0")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

while True:
    try:
        desconto = int(input("Informe o percentual do desconto: "))
        if desconto < 0:
            print("Desconto não pode ser negativo!")
            continue
        elif desconto == 0:
            break
    except ValueError:
        print("Desconto precisa ser um valor inteiro!")
        continue
    break

valor_desconto = valor * (desconto / 100)
valor_pagar = valor - valor_desconto

print(f"O valor do desconto é de R$ {valor_desconto}")
print(f"Valor total a ser pago é R$ {valor_pagar}")