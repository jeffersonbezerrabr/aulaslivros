#6.11 enumerate - Página 170

L = [5, 9 ,13]
x = 0
for e in L:
    print(f"[{x}] {e}")
    x +=1
print()

L = [5, 9, 13]
for x, e in enumerate(L):
    print(f"[{x}] {e}")
print()

L = [5, 9, 13]
for z in enumerate(L):
    x, e = z
    print(f"[{x}] {e}")
    print(z)