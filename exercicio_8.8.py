# Exercício 08-08: - Página 234

# Usando a função mdc definida no exercício anterior, defina uma função
# para calcular o menor múltiplo comum (M.M.C.) entre dois números.
# mmc(a, b) = |a × b| / mdc(a, b)
# Em que |a × b| pode ser escrito em Python como: abs(a * b).

def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
def mmc(a, b):
    return abs(a * b) // mdc(a, b)

print(f"MMC 10 e 5 -->  {mmc(10, 5)}")
print(f"MMC 32 e 24 --> {mmc(32, 24)}")
print(f"MMC 5 e 3 -->   {mmc(5, 3)}")