def gerador_fibonacci():
    p = 0
    s = 1
    while s < 10:
        yield s
        p, s = s, s + p
        
print([x for x in gerador_fibonacci()])
