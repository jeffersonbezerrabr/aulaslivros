#Programa 4.9: Categoria x preço, usando elif

categoria = int(input("Digite a categoria de produto: "))

if categoria == 1:
    preço = 10

elif categoria == 2:
    preço = 18

elif categoria == 3:
    preço = 23

elif categoria == 4:
    preço = 26
    
elif categoria == 5:
    preço =31
    
else:
    print("Categoria invalida, digite um valor entre 1 e 5!")
    preço = 0
print(f"O preço do produto é: R${preço:6.2f}")
