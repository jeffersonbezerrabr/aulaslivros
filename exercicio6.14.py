#Exercício 6.14 - Página 173

#Modifique o programa 6.13 de forma a mostrar quantos ingressos
#foram vendidos em cada sala. Utilize uma lista do mesmo tamanho
#da quantidade de salas e utilize seus elementos para contar
#quantos ingressos foram vendidos em cada sala.
#Imprima na tela o total das vendas no fim do programa.


'''#Programa 6.13 - Controle da utilização de salas de um cinema - Página 172

lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 Sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):"))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
            
print("Utilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")'''
    
lugares_vagos = [10, 2, 1, 3, 0]
ingressos = [0, 0, 0, 0, 0]
while True:
    sala = int(input("Sala (0 Sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):"))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            ingressos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")
            
print("Utilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
    
print()
print("Vendas dos ingressos")
for si, vi, in enumerate(ingressos):
    print(f"Sala {si +1} - {vi} ingresso(s) vendido(s)")
print(f"Quantidade de ingressos vendidos: {sum(ingressos)}")