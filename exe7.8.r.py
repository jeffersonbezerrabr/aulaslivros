# Exercício 7.8 - Página 209

# Escreva um programa para exibir todas as palavras de uma frase. 
# Considere que uma palavra termina com um espaço em branco 
# ou quando a string terminar. 
# Exemplo: “O rato roeu a roupa” deve imprimir 5.

frase = input("Digite uma frase: ")

separado = frase.split()

for palavra in separado:
    print(palavra)

print(len(separado))
