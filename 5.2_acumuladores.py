# 5.2 - Acumuladores - Página 142

# n = 1
# soma = 0

# while n <= 10:
#     x = int(input(f"Digite o {n}º número: "))
#     soma += x
#     n += 1
    
# print(f"Soma: {soma}")

x = 0
soma = 0

while x < 5:
    n = int(input(f"Digite o {x+1}º número: "))
    soma += n
    x += 1

print(f"Média: {soma / x:.2f}")