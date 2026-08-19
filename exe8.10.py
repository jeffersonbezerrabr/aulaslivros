# Exercício 8.10 - Página 234
# Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    

# def gerar_sequencia_recursiva(n_termos):
#     sequencia = []
#     for i in range(n_termos):
#         sequencia.append(fibonacci(i))
#     return sequencia

# print(gerar_sequencia_recursiva(1))


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b
        
        
# fib(4)


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def recursivo_fibo(n):
    for i in range(n):
        print(fibo(i), end=" ")
    
recursivo_fibo(10)