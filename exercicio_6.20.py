# Exercício 06-20.b:

# Escreva um programa que gere um dicionário, em que cada chave seja um caractere, 
# e seu valor seja o número desse caractere encontrado em uma frase lida.
# Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

# frase = input("Escreva uma palavra: ")

# dicio = {}

# for letra in frase:
#     dicio[letra] = dicio.get(letra, 0) + 1

# print(dicio)

frase = input("Digite uma frase para contar as letras:")
d = {}
for letra in frase:
    if letra in d:
        d[letra] += 1
    else:
        d[letra] = 1
print(d)
