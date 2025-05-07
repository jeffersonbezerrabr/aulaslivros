#Programa 4.6: Lê dois valores e imprime qual é o maior com else - Página 125

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print(f"O primeiro valor é maior: {a}")
    
elif a == b:
    print(f"Os valores são iguais: {a and b}")
    
else:
    print(f"O segundo valor é maior: {b}")
