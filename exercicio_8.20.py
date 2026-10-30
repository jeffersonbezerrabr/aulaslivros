# Exercício 08-20:

# Escreva um generator capaz de gerar uma sequência com o fatorial de 1 até n, 
# em que n é passado como parâmetro para o gerador.

def gerador_fatorial(n):
    p = 1
    for v in range(1, n + 1):
        p *= v
        yield p
        
# Exemplo de uso:
# Gerar fatoriais de 1 a 5
for n, fatorial in enumerate(gerador_fatorial(5), 1):
    print(f"{n}! = {fatorial}")