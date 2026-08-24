
nomes = ["Ana", "Carlos", "Maria"]

# O mesmo bloco try pode conter várias delcarações de except. Além disso,
# o bloco try pode ter uma declaração finally. Ao declararmos um bloco com finally, estamos dizendo:
# execute esse bloco, mesmo que aconteça uma exceção com ou sem tratamento.

for tentativas in range(len(nomes)):
    try:
        i = int(input("Digite o índice quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    finally:
        print(f"Tentativa {tentativas + 1}")