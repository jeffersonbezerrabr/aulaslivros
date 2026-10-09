# Exercício 08-18:

# Modifique o Programa 8.26 para que receba dois parâmetros opcionais. 
# Um para indicar o caractere a imprimir antes do número, 
# sendo o espaço em branco o valor padrão, caso este não seja passado. 
# O segundo parâmetro opcional é quantos caracteres adicionar por nível, tendo 2 como valor padrão.

# Programa 8.26: Imprimindo uma lista de inteiros com multiplos níveis - Página 259

# def imprime_listas(lista, nivel=0):
#     for x in lista:
#         if isinstance(x, int):
#             print(f"{x:{nivel * 2}}")
#         else:
#             imprime_listas(x, nivel + 1)
            
# imprime_listas([1, [2, 3, 4], [5, 6, [7, 8, 9]], 10])

def imprime_listas(lista, nivel=0, caractere=" ", incremento=2):
    for x in lista:
        if isinstance(x, list):
            imprime_listas(x, nivel + 1, caractere, incremento)
        else:
            print(f"{caractere * (nivel * incremento)}{x}")
            
# Exemplo de uso:
imprime_listas([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10], caractere="*", incremento=4)