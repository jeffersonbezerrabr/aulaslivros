# Exercício 7.4 - Página 207

# Escreva um programa que leia uma string e imprima 
# quantas vezes cada caractere aparece nessa string.

#String: TTAAC
#Resultado:
#T: 2x
#A: 2x
#C: 1x

texto = input("Digite uma frase: ")

contador = {}

for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1
    
for chave, valor in contador.items():
    print(f"{chave}: {valor}x")
