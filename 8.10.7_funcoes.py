
while True:
    try:
        v = int(input("Digite um número inteiro (0 para sair): "))
        if v == 0:
            break
    except Exception:
        print("Valor inválido! Tente novamente")
    else:
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executado sempre, mesmo com 'break'")
