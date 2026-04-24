# Exercício 7.1 - Página 206

# Escreva um programa que leia duas strings. Verifique se a segunda
# ocorre dentro da primeira e imprima a posição de incio.

p_01 = input("Digite uma frase: ")
p_02 = input("Digite outra frase: ")

posicao = p_01.find(p_02)

if p_02 in p_01:
    print(f"{p_02} encontrada na posição {posicao} de {p_01}")

else:
    print(f"{p_02} não encontrada!")

