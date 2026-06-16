# Exercício 3.11 - Página 113

# Faça um programa que solicite o preço de uma mercadoria e o 
# percentual de desconto. Exiba o valor do desconto e o preço a pagar.

while True:
    try:
        preco = float(input("Informe o valor do produto: "))
        if preco <= 0:
            print("Valor do produto precisa ser positivo!")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

while True:
    try:
        percentual_desconto = float(input("Informe o percentual do desconto: "))
        if percentual_desconto < 0:
            print("Percentual do desconto não pode ser negativo")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

valor_desconto = preco * (percentual_desconto / 100)
valor_a_pagar = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:5.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:5.2f}")
