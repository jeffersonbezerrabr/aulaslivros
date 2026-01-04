#Programa 6.10 - Transformação de range em uma lista

L = list(range(100,1100,50))
print(L)

# Enumerate

# L1 = [5, 9, 13]

# for x, e in enumerate(L1):
#     print(f"[{x}] {e}")
    
L2 = [5, 9, 13]

for z in enumerate(L2):
    x, e = z
    print(f"[{x}] {e}")
    print(z)
