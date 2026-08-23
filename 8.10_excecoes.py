# Exceções - Página 244,245, 246

nomes = ["Ana", "Carlos", "Maria"]
        
for tentativas in range(len(nomes)):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    except IndexError:
        print("Valor inválido, digite de 0 a 2")
        
        

