def ehpar(n):
    try:
        return n % 2
    finally:
        print("Executado antes de retornar")
        
try:
    print(2,ehpar(2))
    print("A",ehpar("A"))
except Exception:
    print("Algo de errado aconteceu")
