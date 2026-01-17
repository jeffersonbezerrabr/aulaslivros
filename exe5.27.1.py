# Exercício 5.27 - Verificador de Palíndromos (versão simplificada)

n = int(input("Informe um número: "))
original = n  # Guarda o valor original
invertido = 0

# Se for negativo, transforma em positivo para verificação
if n < 0:
    n = -n  # Remove o sinal negativo

# Inverte o número
while n > 0:
    ultimo_digito = n % 10
    invertido = (invertido * 10) + ultimo_digito
    n = n // 10
    
# Verifica se é palíndromo
if original == invertido or original == -invertido:
    print(f"{original} é palíndromo!")
else:
    print(f"{original} não é palíndromo!")