# Exercício 7.7 - Página 207

# Escreva um programa que peça ao usuário que digite uma frase
# e imprima quantas vogais ela contém. 
# Não considere maiúsculas e minúsculas como diferentes. 
# 
# Exemplo: uma frase como “A casa” deve imprimir três “as”.

vogais = "aeiou"
frase = input("Digite uma frase: ").lower().strip()
contador = {}

for f in frase:
    if f in vogais:
        if f in contador:
            contador[f] += 1
        else:
            contador[f] = 1

for letra, quantidade in contador.items():
    print (f'Quantidade de {letra.upper()} é {quantidade }')