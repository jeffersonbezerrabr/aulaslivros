# Programa 8.7: Função recursiva de Fibonacci - Página 233

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(6))

