#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia.
#Pergunte a quantidade de kWh consumida e o tipo de instalação.
#R para residencial
#I para industrias
#C para comercios
#Calcule o preço a pagar.

instalação = input("Qual o tipo de instalação? R = Residencia, I = Industria, C = Comercios: ")
print()

valido = True
preco = 0
kwm = int(input("Quantos kWh foi consumido? "))

if instalação == "R" or instalação == "r":
    if kwm <= 500:
        preco = 0.40  
    else:
        preco = 0.65

elif instalação == "I" or instalação == "i":
    if kwm <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif instalação == "C" or instalação == "c":
    if kwm <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    valido = False
if not valido:
    print("Tipo de instalação não encontrado")

else:
    total = preco * kwm
    print(f"Total a pagar é: R${total:5.2f}")
