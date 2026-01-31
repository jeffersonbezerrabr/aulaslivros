# Programa 8.2: Como não escrever uma função - Página 227

# def soma(L):
#     total = 0
#     x = 0
    
#     while x < 5:
#         total += L[x]
#         x += 1
#     return total

# Forma correta feita por mim:

# def soma(L):
#     total = 0
#     x = 0
    
#     while x < len(L):
#         total += L[x]
#         x += 1
#     return total

# Forma correta feita por mim(2):

def soma(L):
    total = 0
    
    for c in L:
        total += c
    return total


L = [1, 7, 2, 9, 15]

print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))


