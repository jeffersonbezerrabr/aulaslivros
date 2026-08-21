# Programa 8.9: Exemplo de validação sem usar uma função - Página 234

while True:
    try:
        v = int(input("Digite um valor entre 0 e 5: "))
        if v < 0 or v > 5:
            print("Valor inválido.")
        else:
            print("Obrigado!")
            break
    except ValueError:
        print("Digite um valor inteiro!")
