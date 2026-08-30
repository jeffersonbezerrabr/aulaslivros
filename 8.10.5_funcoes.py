def ehpar(n):
    try:
        return n % 2
    except Exception:
        raise ValueError("Valor inválido")
        

print(ehpar(2))
print(ehpar([]))