 
L = ["A", "b", "C", "d", "E"]

L.sort()

print(L)

L.sort(key=lambda k: k.lower())

print(L)
