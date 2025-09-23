# Modifique o programa 6.13 de forma a perguntar o número de salas disponiveis no cinema, 
# assim como a quantidade de lugares em cada uma das salas

#Programa 6.13 - Controle da utilização de salas de um cinema - Página 172

lugares_vagos = [10, 2, 1, 3, 0]
vendas = [0, 0, 0, 0, 0]
salas_disponiveis = []
while True:
    q01 = input("Deseja saber quais salas estão disponíveis? [S]im ou [N]ão: ").upper()
    if q01 == "S":
        for c, cc in enumerate(lugares_vagos):
            if cc > 0:
                salas_disponiveis.append(cc)
                print(f"Sala {c} disponivel")
    sala = int(input("Qual sala (0 Sai): "))
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
            vendas[sala -1] += lugares
            print(f"{lugares} lugares vendidos")
            
print("Utilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
print("=x="*15)
for s,v in enumerate(vendas):
    print(f"Foram vendidos {v} ingressos na sala {s+1}")
    
print("=x="*15)

print(f"total de ingressos vendidos: {sum(vendas)}")
    
