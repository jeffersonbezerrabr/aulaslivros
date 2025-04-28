#Exercicio da página 113

preço = int(input("Qual o preço do produto: "))
desconto = int(input("Quantos porcentos de desconto: "))
desconto_aplicado = desconto * preço / 100
preço_desconto = preço - desconto_aplicado
print(f"O desconto é de R$: {desconto_aplicado:5.2f}")
print(f"Valor do produto com o desconto: R$ {preço_desconto:5.2f}")
