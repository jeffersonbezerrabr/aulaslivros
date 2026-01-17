#Versão palindromo de palavras

palavra = input("Digite uma palavra: ")

inverso = palavra[::-1]

if inverso == palavra:
    print(f"{palavra} é palindromo!")
    
else:
    print(f"{palavra} não é palindromo!")