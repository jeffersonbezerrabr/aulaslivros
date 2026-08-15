# Exercício 08-07: - Página 234

# Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois números a e b, em que a > b.
# Em que a-b|a/b| pode ser escrito em Python como: a & b

def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
print(f"MDC 10 e 5 -->  {mdc(10,5)}")
print(f"MDC 32 e 24 --> {mdc(32,24)}")
print(f"MDC 5 e 3 -->   {mdc(5,3)}")