#Exercício 6.13 - Página 171

#A lista de temperatura de Mons, na Bélgica, foi armazenada
#na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
#Faça um programa que imprima a menor e a maior temperatura,
#assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]
media = 0
maior = menor = T[0]

for c in T:
    if c > maior:
        maior = c
    if c < menor:
        menor = c

for m in T:
    media += m

     
print(f"A maior temperatura registrada foi {maior}\n")
print(f"A menor temperatura registrada foi {menor}\n")
print(f"A media foi {media / len(T)}")