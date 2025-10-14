#Escreva um programa que gere um dicionário, em que cada
#chave seja um caractere, e seu valor seja o número desse caractere
#encontrado em uma frase lida.

#Exemplo: O rato -> {"O":1, "r":1, "a":1, "t":1, "o":1}

# L = {}

# frase = input("Digite uma frase: ")

# for letra in frase:
#     if letra in L:
#         L[letra] += 1
#     else:
#         L[letra] = 1

    
# print(L)

d = {}

frase = input("Digite uma frase: ")

for letra in frase:
    d[letra] = d.get(letra, 0) + 1
    
print(d)
