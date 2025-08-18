#Programa 6.8 - Pilha de pratos - Página 164

prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"\nExistem {len(pilha)} pratos na pilha.")
    print(f"Pilha atual {pilha}")
    print("Digite E para empilhar um novo prato.")
    print("ou D para desempilhar. S para sair.")
    operacao = str(input("Operação(E, D ou S): ")).lower()
    
    if operacao == "e":
        prato += 1
        pilha.append(prato)
        print(f"Prato {prato} adicionado à pilha.")  # Mostra o número do prato
    elif operacao == "d":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado.")
        else:
            print("Pilha vazia! Nenhum prato para lavar.")
    elif operacao == "s":
        print("Encerrando programa...")
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S")