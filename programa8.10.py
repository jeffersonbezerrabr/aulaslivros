# Progrma 8.10: Validação de inteiro usando função - Página 235

def faixa_int(minimo, maximo):
    while True:
        v = int(input(f"Digite um número entre {minimo} e {maximo}: "))
        if v < minimo or v > maximo:
            print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
        else:
            return v

print(faixa_int(5, 10))
