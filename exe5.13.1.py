#5.3 - Página 144 e 145
#Interrompendo a repetição

s = 0
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    if v == 0:
        break
    s = s + v
print(s)
