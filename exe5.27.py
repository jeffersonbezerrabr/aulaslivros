#Exercício 5.27 - Página 149

#Escreva um programa que verifique se um número é palíndromo.
#Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
#Exemplos: 454, 10501
     
n = int(input("Informe um número: "))
original = n
invertido = 0

while n > 0:
    ultimo_digito = n % 10
    invertido = (invertido * 10) + ultimo_digito
    n = n // 10
    
if original == invertido:
    print(f"{original} é palindromo!")
else:
    print(f"{original} não é palindromo!")
    
    
    
"""n = int(input("Digite um número: "))  # Ex: 121
original = n  # Guarda o valor original (121)
invertido = 0  # Aqui vamos construir o número invertido

while n > 0:
    ultimo_digito = n % 10  # Pega o último dígito de n (1 → 2 → 1)
    invertido = (invertido * 10) + ultimo_digito  # Empilha os dígitos (0 → 1 → 12 → 121)
    n = n // 10  # Remove o último dígito (121 → 12 → 1 → 0)

if original == invertido:
    print(f"{original} é palíndromo!")  # 121 == 121
else:
    print(f"{original} não é palíndromo!")"""