# Exercício 7.7 - Página 207

# Escreva um programa que peça ao usuário que digite uma frase
# e imprima quantas vogais ela contém. 
# Não considere maiúsculas e minúsculas como diferentes. 
# 
# Exemplo: uma frase como “A casa” deve imprimir três “as”.

vogais = "aeiou"
frase = input("Digite uma frase: ").lower().strip()


for vogal in vogais:
    contador_vogais = frase.count(vogal)
    if contador_vogais > 0:
        print(f"{vogal} aparece {contador_vogais} vez(es)")