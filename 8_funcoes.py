
def soma(a, b):
    return (a + b)
    
print(soma(2, 9))
print(soma(7, 8))
print(soma(10, 15))

def eh_par(x):
    return x % 2 == 0

print(eh_par(2))
print(eh_par(3))
print(eh_par(10))


def par_ou_impar(x):
    if eh_par(x):
        return "Par"
    else:
        return "Impar"
    
print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(10))

