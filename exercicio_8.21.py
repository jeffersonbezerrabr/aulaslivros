# Exercício 08-21:

# Escreva uma função que gere os números como a função range do Python. 
# Essa função recebe três parâmetros e seu comportamento muda 
# se passarmos um, dois ou três parâmetros. Chame-a de faixa.

# Exemplos:

"""
list(faixa(1))
[0, 1]
list(faixa(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(faixa(0, 10, 2))
[0, 2, 4, 6, 8, 10]
"""

# Você deve ter percebido que, diferente de range, a função faixa considera o fim do intervalo fechado, 
# ou seja, o último número faz parte da faixa.

def faixa(inicio, fim=None, passo=1):
    if fim is None:
        inicio, fim = 0, inicio
        
    atual = inicio
    while atual <= fim:
        yield atual
        atual += passo
        
# Casos de teste
print(list(faixa(1)))  # [0, 1]
print(list(faixa(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(faixa(0, 10, 2)))  # [0, 2, 4, 6, 8, 10]
