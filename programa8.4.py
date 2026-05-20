# Prograna 8.4: Outra forma de calcular o fatorial - Página 228

def fatorial(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat


print(fatorial(3))
print(fatorial(4))
