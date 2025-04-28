#Exercicio da página 114

print("Localiza")
print()
#Recebe os quiloemtros percorridos do usuário
km_percorrido = int(input("Quantos KM percorreu com o carro? "))
print()

#Recebe quantos dias o usuário ficou com o carro
dias = int(input("Quantos dias ficou com o carro? "))

#Multiplica a quilometragem informada pelo valor cobrado por quilometro
valor_km = km_percorrido * 0.15

#Multiplica os dias pelo valor do dia
valor_dias = dias * 60

#Soma o valor calculado das quilometragem pelo valor calculado dos dias
total = valor_km + valor_dias

#Exibe o resultado
print(f"O valor total a pagar é R$ {total:5.2f}")
