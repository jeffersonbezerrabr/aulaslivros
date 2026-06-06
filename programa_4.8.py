# Programa 4.8 - Categoria x preço - Página 127

while True:
    try:
        categoria = int(input("Digite a categoria do produto: "))
        if categoria <= 0 or categoria > 5:
            print("Valores válidos [1,2,3,4,5]")
            continue
        if categoria == 1:
            preco = 10
        elif categoria == 2:
            preco = 18
        elif categoria == 3:
            preco = 23
        elif categoria == 4:
            preco = 26
        else:
            preco = 31
    except ValueError:
        print("Precisa digitar um valor númerico [1,2,3,4,5]")
        continue
    break

print(f"O preço do produto é: R$ {preco:5.2f}")
