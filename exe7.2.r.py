# Exercício 7.2 - Página 206

# Escreva um programa que leia duas strings e gere uma tereira
# com os caracteres comuns às duas strings lidas.

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = set(primeira) & set(segunda)
resultado = ''.join(terceira)

print(f"Caracteres em comum: {resultado}")

