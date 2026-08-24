# Exceções - Página 244,245, 246

nomes = ["Ana", "Carlos", "Maria"]

# Existem vários tipos de exceç]ao em Python> O tipo raiz chama-se "Exception".
# Você pode tratar o tipo "Exception" que cobre todos os erros comuns do Python.

for tentativas in range(len(nomes)):
    try:
        i = int(input("Digite o índice quer imprimir: "))
        print(nomes[i])
    except Exception as e:
        print(f"Algo de errado aconteceu: {e}")


