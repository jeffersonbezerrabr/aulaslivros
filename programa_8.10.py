#Programa 8.10: Validação de inteiro usando função - Página 235

def faixa_int(pergunta, minimo, maximo):
    while True:
        try:
            v = int(input(pergunta))
            if v < minimo or v > maximo:
                print(f"Valor invalido. Digite um valor entre {minimo} e {maximo}")
            else:
                return v
        except ValueError:
            print("Digite um número inteiro")

print(faixa_int("Digite um número entre 0 e 10: ", 0, 10))
