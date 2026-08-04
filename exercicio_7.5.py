"""Exercício 07-05: - Página 207

Escreva um programa que leia duas strings e gere uma terceira, 
na qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA"""

primeira = "AATTGGAA"
segunda = "TG"
terceira = ""

for letra in primeira:
    if letra not in segunda:
        terceira += letra
        
if terceira == "":
    print("Todos os caracteres foram removidos.")
else:
    print(f"Os caracteres {segunda} foram removidos de {primeira}, gerando: {terceira}")