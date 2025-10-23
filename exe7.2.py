# Exercício 7.2 - Página 206

# Escreva um programa que leia duas strings e gere uma tereira
# com os caracteres comuns às duas strings lidas.

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ''

for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra
 
if terceira == '':
    print("Caracteres comuns não encontrados")
else:        
    print(f"Caracteres em comum: {terceira}")

