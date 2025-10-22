# Exercício 7.1 - Página 206

# Escreva um programa que leia duas strings. Verifique se a segunda
# ocorre dentro da primeira e imprima a posição de incio.

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")


posicao = primeira.find(segunda)

if segunda in primeira:
    print(f"{segunda} encontrado na posição {posicao} de {primeira}")
else:
    print(f"{segunda} não encontrado!")
    