#Exercício 6.5 - Página 164

#Altere o programa 6.7 de forma a poder trabalhar com vários
#comandos digitados de uma só vez. Atualmente, apenas um comando
#pode ser inserido por vez. Altere-o de forma a considerar
#operação com uma string.

#Exemplo: FFFAAAS significaria três chamadas de novos clientes,
#três atendimentos e, finalmente, a saída do programa.

'''#Programa 6.7 - Página 163 - Simulação de uma fila de banco

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f'Fila atual: {fila}')
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S): ")
    if operacao == "A" or operacao == "a":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print(f"Fila vazia! Ninguém para atender.")
    elif operacao == "F" or operacao =="f":
        ultimo += 1 #Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S" or operacao == "s":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")'''
        
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite vários comandos de uma vez (F, A ou S):")
    print("Exemplo: FFFAAAS - 3 novos, 3 atendimentos, sair")
    
    comandos = input("Operações: ").lower()
    i = 0  # Começamos pelo primeiro caractere
    
    while i < len(comandos):  # Enquanto houver comandos para processar
        operacao = comandos[i]
        
        if operacao == "a":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "f":
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} adicionado")
        elif operacao == "s":
            print("Encerrando o programa...")
            exit()
        else:
            print(f"Comando inválido: {operacao}. Use apenas F, A ou S!")
        
        i += 1  # Vamos para o próximo comando
    
    # Se chegou aqui é porque processou todos os comandos
    # O loop principal continua...