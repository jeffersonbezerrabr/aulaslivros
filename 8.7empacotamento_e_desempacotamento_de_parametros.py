
# def soma(a, b):
#     print(a + b)
    
# L = [2, 3]

# soma(*L)

def barra(n=10, c="*"):
    print(c * n)
    
L = [[5, "-"], [10, "*"], [5], [6, "."]]

for e in L:
    barra(*e)
