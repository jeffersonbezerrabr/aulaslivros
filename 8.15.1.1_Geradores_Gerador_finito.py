def gerador_fibonacci(fim):
    p = 0
    s = 1
    while s < fim:
        yield s
        p, s = s, s + p
        
print(list(x for x in gerador_fibonacci(30)))