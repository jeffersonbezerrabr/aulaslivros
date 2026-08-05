# Exercício 7.8 - Página 209

# Escreva um programa para exibir todas as palavras de uma frase.
# Considere que uma palavra termina com um espaço em branco ou quando a string terminar.
# Exemplo: "O rato roeu a roupa" deve imprimir 5.

string = input("Digite uma frase: ")

separado = string.split()

print(separado)
print(f"Contem {len(separado)} palavras!")