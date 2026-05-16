#Fatorial de um número

#O programa deve pedir ao usuário para digitar um número inteiro positivo.

#O programa deve verificar se o número é válido (não negativo).

#O programa deve calcular o fatorial do número utilizando um loop while.

#O programa deve exibir o resultado na tela.

numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    print("Numero invalido!")
    numero = int(input("Digite um número inteiro positivo: "))
    
fatorial = 1
contador = numero

while contador >= 1:
    fatorial = fatorial * contador
    contador = contador - 1
    
print(f"O fatorial de {numero} é {fatorial}")
    