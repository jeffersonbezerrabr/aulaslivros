# Programa 8.8: Função recursiva de Fibonnaci com prints - Página 233

def fibonacci(n):
    print(f"Calculando fibonacci {n}")
    if n <= 1:
        print(f"    Fibonacci de {n} = {n}")
        return n
    else:
        print(f"    Fibonacci de {n} = Fibonacci {n - 1} + Fibonacci de {n - 2} = ...")
        resultado = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"    Fibonacci de {n} = Fibonacci {n - 1} + Fibonacci {n - 2} = {resultado}")
        return resultado
    
fibonacci(5)