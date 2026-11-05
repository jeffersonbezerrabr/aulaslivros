import math

print(math.ceil(4.2), math.floor(4.2))

print(math.ceil(4.9), math.floor(4.9))

print(math.ceil(-4.9), math.floor(-4.9))

print()

# ceil e floor são equivalentes às operações de teto e solo da matemática, mas em inglês.
# Veja que ceil é o teto e traz o número para o proximo inteiro maior que o número passado.
# Já o floor, é o solo e tem o comportamento inverso, retornando o valor do primeiro inteiro menor.

# Se você precisa arrendondar um número, utilize a função round, que é uma função básica do Python,
# não precisa de qualquer import para utilizá-la.


# print(round(4.2))
a = round(4.2)
print(round(4.2))

b = round(4.9)
print(b)

c = round(-4.9)
print(c)

d = round(-4,2)
print(d)

print()

# round pode receber um parâmetro opcional que indica quantas digitos arredondar após o ponto.

e = round(4.2556, 2)
print(e)

f = round(4.2556, 3)
print(f)

print()

# Você pode usar a função trunc para remover a parte após o ponto:

print(math.trunc(8.192))
print()

# E abs para retornar o valor absoluto (sem sinal) de um número.

print(abs(3), abs(-4), abs(0))
print()

# Se você precisar separar a parte inteira e fracionária de um número, 
# pode utilizar outras funções e mesmo a operação de módulo:

print(5.34 % 1.0)
print()

# Veja que a parte fracionária não é 0.34, mas um número próximo. 
# Essa é uma característica de números em ponto flutuante.

# Usando modf, você obtém uma tupla com as duas partes:

print(math.modf(5.34))
print()

# Outra função útil é divmod que retorna o resultado da divisão e o resto(divisão e módulo):

print(divmod(10, 3))

print(divmod(5.34, 1))
print()

# Python também tem várias funções trigonométricas, como seno(math.sin),
# cosseno(math.cos) e tangente(math.tan). Todas elas trabalham com radianos
# e não com graus. Lembre-se: pi radiano é igual a 180 graus.

print(math.degrees(math.pi))
print()

# A função degress converte um valor em radianos para graus.
# math.pi é a constante do pi.

print(math.pi)
print()

# Inversamente, a função radians converte de graus para radianos.

print(math.radians(180))
print(math.radians(90))
print(math.radians(45))
print()

print(math.sin(math.radians(30)))

print(math.cos(math.radians(30)))

print(math.tan(math.radians(30)))

print(math.cos(math.pi))