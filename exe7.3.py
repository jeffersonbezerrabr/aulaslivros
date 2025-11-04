# Exercício 7.3 - Página 207

# Escreva um programa que leia duas strings e gere uma terceira
# apenas com os caracteres que aparecem em uma delas.

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ''

for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira += letra

for letra in segunda:
    if letra not in primeira and letra not in terceira:
        terceira += letra

if terceira == '':
    print("Caracteres incomuns não encontrados.")

else:
    print(f"Caracteres incomuns: {terceira}")