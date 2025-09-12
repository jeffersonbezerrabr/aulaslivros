#Exercício 6.6 - Página 164

#Modifique o programa para trabalhar com duas filas.
#Para facilitar seu trabalho,
#considere o comando A para atendimento da fila 1;
#e B, para atendimento da fila 2.;
#O mesmo para a chegada de clientes:
#F para fila 1; e G para fila 2.

'''Passos do programa:

- Criar duas filas
- Comando A para atender clientes da fila 1
- Comando B para atender clientes da fila 2
- F para adicionar clientes a fila 1
- G para adicionar clientes a fila 2
'''

fila1 = []
fila2= []

c1 = 1
c2 = 1

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1")
    print(f"\nExistem {len(fila2)} clientes na fila 2.")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente a fila 1.")
    print("Digite G para adicionar um cliente a fila 2.")
    print("Digite A para atender um cliente da fila 1.")
    print("Digite B para atender um cliente da fila 2.")
    print("Digite S para encerrar o programa.")
    operacao = str(input("Digite um comando: ")).lower()
    
    if operacao == "f":
        fila1.append(c1)
        print(f"Cliente {c1} adicionado a fila 1")
        c1 += 1
    elif operacao == "g":
        fila2.append(c2)
        print(f"Cliente {c2} adicionado a fila 2")
        c2 += 1
    elif operacao == "a":
        if len(fila1) > 0:
            atendido1 = fila1.pop(0)
            print(f"Cliente {atendido1} atendido na fila 1")
        else:
            print("Fila 1 vazia.")
    elif operacao == "b":
        if len(fila2) > 0:
            atendido2 = fila2.pop(0)
            print(f"Cliente {atendido2} atendido na fila 2.")
        else:
            print("Fila 2 vazia.")
    elif operacao == "s":
        print("Encerrando o programa...")
        break
    else:
        print("Comando inválido! Use F, G, A, B ou S")
        