# Modifique o programa 6.2 para ler 7 notas em vez de 5

notas = []
soma = 0
x = 0

while x < 7:
    try:
        nota = float(input(f"Digite a nota {x +1}: "))
        if nota >= 0:
            notas.append(nota)
            soma += notas[x]
            x += 1
        elif nota < 0:
            print("Precisa digitar um valor maior ou igual a 0")
    except ValueError:
        print("Precisa digitar um número")

x = 0

while x < 7:
    print(f"Nota {x +1}: {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma / x:5.2f}")
