# Exercício 4.6 - Página 126

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km,
# e R$ 0,45 para viagens mais longas.

try:
    distancia = float(input("Informe a distância: "))
    if distancia < 0:
        print("Distância não pode ser negativa")
    else:
        if distancia <= 200:
            valor = distancia * 0.50
        
        else:
            valor = distancia * 0.45
            
        print(f"Valor a pagar: R$ {valor:5.2f}")
    
except ValueError:
    print("Valor precisa ser númerico")
    
