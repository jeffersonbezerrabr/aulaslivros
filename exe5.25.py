#Exercício 5.25 - Página 149

#Escreva um programa que calcule a raiz quadrada de um número.
#Utilize o metodo de Newton para obter um resultado aproximado.
#Sendo n o número a obter a raiz quadrada, considere a base b=2.
#Calcule p usando a fórmula p=(b(n/b))/2.
#Agora, calcule o quadrado de p. A cada passo,
#faça b=p e recalcule p usando a formula apresentada.
#Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

# Pede ao usuário um número (ex.: 9)
numero = float(input("Digite um número: "))

# Começa com um "chute" inicial para a raiz (b = 2)
b = 2

# Enquanto a diferença entre o número e o quadrado do chute for maior que 0.00001:
while abs(numero - (b * b)) > 0.00001:
    
    # Método de Newton: calcula um novo chute (p) mais preciso
    p = (b + (numero / b)) / 2
    
    # Atualiza o chute (b) para o valor mais preciso (p)
    b = p
    
    # Mostra o resultado aproximado a cada passo (opcional, só para visualizar)
    print(f"A raiz quadrada de {numero} é aproximadamente {p:8.4f}")