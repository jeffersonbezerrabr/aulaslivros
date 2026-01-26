#Exercício 6.13 - Página 171

#A lista de temperatura de Mons, na Bélgica, foi armazenada
#na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
#Faça um programa que imprima a menor e a maior temperatura,
#assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]
maximo = T[0]
minimo = T[0]
media = sum(T) / len(T)
for temp in T:
    if temp > maximo:
        maximo = temp
    if temp < minimo:
        minimo = temp
print(f"A menor temperatura é {minimo}\n")
print(f"A maior temperatura é {maximo}\n")
print(f"A média é {media}")
