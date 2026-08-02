"""Exercício 07-02: - Página 206

Escreva um programa que leia duas strings e gere uma terceira 
com os caracteres comuns às duas strings lidas.

1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, 
mas deve conter todas as letras comuns a ambas."""

#Modelo 1

# primeira = "AAACTBF"
# segunda = "CBT"

# conjunto1 = set(primeira)
# conjunto2 = set(segunda)

# resultado = conjunto1 & conjunto2
# junto = "".join(resultado)
# print(junto)

primeira = "AAACTBF"
segunda = "CBT"

terceira = ""
for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra
        
if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print(f"Caracteres em comum: {terceira}")