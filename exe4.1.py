#exercício 4.1 página 120

#Comparador de dois números

#Recebe o primeiro valor do usuário
a = int(input("Primeiro valor: "))

#Recebe o segundo valor do usuário
b = int(input("Segundo valor: "))

#compara se a é maior que b. Se for, imprima essa resposta
if a > b:
    print("O primeiro valor é o maior")

#Compara se b é maior que a. Se for, imprima essa resposta    
if b > a:
    print("O segundo valor é maior")

#caso os valores sejam iguais, imprima esse resultado
else:
    print("Os valores são iguais")
    